import builtins
import antlrFiles
from customs import customs
from antlr4 import FileStream, CommonTokenStream
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.pythonicvisitor import PythonicVisitor
from src.core.fsm import FSM
from src.core.transition import Transition, PredicateTransition
from src.core.state import State
from src.core.exceptions.illegaltypeexception import IllegalTypeException
from src.core.exceptions.illegalvalueexception import IllegalValueException
from src.core.exceptions.subtypingexception import SubtypingException
from src.core.exceptions.rolemismatchexception import RoleMismatchException
from itertools import permutations
from antlrFiles.PythonicParser import PythonicParser

'''
The FsmBuilder class is responsible for building the FSM, via the buildFSM method from the given specification. 
The class inherits from PythonicVistor, which is auto-generated by antlr4 based on the grammar file.
'''  

class FsmBuilder(PythonicVisitor):

    def __init__(self):
        self.fsm: FSM = FSM()
        self.loop_dictionary: dict[str, State] = {}
        self.used_roles: set(str) = set()
        self.defined_roles: set(str) = set()

    # Builds an FSM based on the parse tree generated from the specification at the given file path.
    # Checks if the defined and used roles match and returns the fsm if so, else raises 
    # a RoleMismatchException
    def buildFsm(self, filePath: str) -> tuple[FSM, set[str]]:
        ast = self.buildParseTree(filePath)
        self.visitSpecification(ast)
        if not self.used_roles == self.defined_roles:
            raise RoleMismatchException(self.used_roles, self.defined_roles)
        return self.fsm     
        
    # Visits the roles and the protocol to determine the defined roles and to build the FSM.
    def visitSpecification(self, ctx: PythonicParser.SpecificationContext):
        self.visitRoles(ctx.getChild(0))
        self.visitProtocol(ctx.getChild(1))
        
    # Creates a start and end state and visits the first expression with both states.
    def visitProtocol(self, ctx: PythonicParser.ProtocolContext) -> None:
        expression: str = ctx.getChild(1).getChild(1).getChild(0)
        startState: State = self.fsm.getStates()[0]
        endState: State = State()
        self.visitExpression(expression, startState, endState) 

    # Checks which expression is offered and continues in the respective visitor.
    def visitExpression(self, ctx: PythonicParser.ExpressionContext, startState: State, endState: State) -> None:
        expression: str = ctx.getChild(1)
        match ctx.getChild(0).getText():
            case "sequence:":
                self.visitSequence(expression, startState, endState)
            case "choice:":
                self.visitChoice(expression, startState, endState)
            case "shuffle:":
                self.visitShuffle(expression, startState, endState)
            case "send":
                self.visitSend(ctx, startState, endState)
            case "loop":
                self.visitLoop(ctx, startState, endState)

    # Builds the fsm sequence part, checks for repeat and end of sequence. Visits the expression that
    # is at each part in the sequence.
    def visitSequence(self, ctx:PythonicParser.SequenceContext, startState: State, endState: State) -> None:
        repeat: bool = False
        expressionCount: int = ctx.getChildCount() - 2

        # check whether last child is a repeat expression
        lastChild: str = ctx.getChild(expressionCount).getChild(0)
        if lastChild.getChild(0).getText() == "repeat":
            repeat = True
            expressionCount -= 1    

        currentState: State = startState     
        expressionIndices: range = range(1, expressionCount + 1)
        for index in expressionIndices:
            if index == expressionCount:
                if repeat:
                    loopTag: str = lastChild.getChild(1).getText() 
                    nextState: State =  self.loop_dictionary[loopTag]
                else:
                    nextState: State = endState
            else:
                nextState: State = State()
            expression: str = ctx.getChild(index).getChild(0)
            self.visitExpression(expression, currentState, nextState)
            currentState = nextState

    # Builds a shuffle part of an fsm, where the expressions in the shuffle are allowed
    # to happen in any order.
    def visitShuffle(self, ctx: PythonicParser.ShuffleContext, startState: State, endState: State) -> None:
        expressionCount: int = ctx.getChildCount() - 2
        expressionIndices: range = range(1, expressionCount + 1)
        for indicesPermutation in permutations(expressionIndices):
            counter: int = 0
            currentState: State = startState
            for index in indicesPermutation:
                counter += 1
                if counter == expressionCount:
                    nextState: State = endState
                else:
                    nextState: State = State()
                expression: str = ctx.getChild(index).getChild(0)
                self.visitExpression(expression, currentState, nextState)
                currentState = nextState

    # Builds a choice part of an FSM, where one of multiple options is allowed.
    def visitChoice(self, ctx:PythonicParser.ChoiceContext, startState: State, endState: State) -> None:
        expressionCount: int = ctx.getChildCount() - 2
        expressionIndices: range =  range(1, expressionCount + 1)
        for index in expressionIndices:
            expression: str = ctx.getChild(index).getChild(0)
            self.visitExpression(expression, startState, endState)
    
    # Builds the start of a loop in an FSM and adds the loop tag to the loop_dictionary.
    def visitLoop(self, ctx:PythonicParser.LoopContext, startState: State, endState: State) -> None:
        tag_with_semi_colon: str = ctx.getChild(1).getText()
        tag: str = tag_with_semi_colon[0:len(tag_with_semi_colon) - 1]
        self.loop_dictionary[tag] = startState
        expression: str = ctx.getChild(2).getChild(1).getChild(0)
        self.visitExpression(expression, startState, endState)

    # Builds a transition from the given SendContext and adds it to the FSM.
    def visitSend(self, ctx: PythonicParser.SendContext, startState: State, endState: State) -> None:
        if self.isNonPredicateSend(ctx):
            transition = self.buildNonPredicateTransition(ctx)
        elif self.containsNonEqualPredicate(ctx):
            if self.containsCustomType(ctx):
                transition = self.buildCustomTypeNonEqualPredicateTransition(ctx)
            else:
                transition = self.buildPrimitiveTypeNonEqualPredicateTransition(ctx)
        elif self.containsCustomType(ctx):
            transition = self.buildCustomTypeEqualPredicateTransition(ctx)
        else:
            transition = self.buildPrimitiveTypeEqualPredicateTransition(ctx)

        startState.addTransitionToState(transition, endState)
        self.used_roles.add(transition.getSender())
        self.used_roles.add(transition.getReceiver())

    # Checks whether the given SendContext concerns a non-predicate send.
    def isNonPredicateSend(self, ctx: PythonicParser.SendContext) -> bool:
        return ctx.getChild(2).getText() == 'from'

    # Checks whether the given SendContext contains a custom type.
    def containsCustomType(self, ctx: PythonicParser.SendContext) -> bool:
        return (ctx.getChild(ctx.getChildCount() - 6).getText() == ")" and ctx.getChild(ctx.getChildCount() - 7).getText() == ")")
    
    # Checks whether the given SendContext contains a non-equal predicate.
    def containsNonEqualPredicate(self, ctx: PythonicParser.SendContext) -> bool:
        return ctx.getChild(3).getText() in [">", "<", ">=", "<=", "!="]

    # Builds a non-predicate transition from the given SendContext.
    def buildNonPredicateTransition(self, ctx: PythonicParser.SendContext) -> Transition:
        object_type: any = self.convert_string_to_type(ctx.getChild(1).getText())
        sender: str = ctx.getChild(3).getText()
        receiver: str = ctx.getChild(5).getText()
        return Transition(object_type, sender, receiver)

    # Builds a predicate transition with a custom type and a non-equal comparator from the given SendContext.
    def buildCustomTypeNonEqualPredicateTransition(self, ctx: PythonicParser.SendContext) -> PredicateTransition:
        object_type: any = self.convert_string_to_type(ctx.getChild(1).getText())
        constructor: any = self.convert_string_to_type(ctx.getChild(4).getText())
        comparator: str = ctx.getChild(3).getText()
        sender: str = ctx.getChild(ctx.getChildCount() - 4).getText()
        receiver: str = ctx.getChild(ctx.getChildCount() - 2).getText()
        value_string: str = ""
        for i in range(4, ctx.getChildCount() - 6):
            value_string += ctx.getChild(i).getText()
        value: any = self.convert_string_to_custom_object(object_type, constructor, value_string)
        return PredicateTransition(object_type, sender, receiver, comparator, value)
    
    # Builds a predicate transition with a custom type and the "==" comparator from the given SendContext.
    def buildCustomTypeEqualPredicateTransition(self, ctx: PythonicParser.SendContext) -> PredicateTransition:
        object_type: any = self.convert_string_to_type(ctx.getChild(1).getText())
        constructor: any = self.convert_string_to_type(ctx.getChild(3).getText())
        sender: str = ctx.getChild(ctx.getChildCount() - 4).getText()
        receiver: str = ctx.getChild(ctx.getChildCount() - 2).getText()
        value_string: str = ""
        for i in range(3, ctx.getChildCount() - 6):
            value_string += ctx.getChild(i).getText()
        value: any = self.convert_string_to_custom_object(object_type, constructor, value_string)
        return PredicateTransition(object_type, sender, receiver, "==", value)
    
    # Builds a predicate transition with a non-custom type and a non-equal comparator from the given SendContext.
    def buildPrimitiveTypeNonEqualPredicateTransition(self, ctx: PythonicParser.SendContext) -> PredicateTransition:
        object_type: any = self.convert_string_to_type(ctx.getChild(1).getText())
        comparator: str = ctx.getChild(3).getText()
        sender: str = ctx.getChild(7).getText()
        receiver: str = ctx.getChild(9).getText()
        value_string: str = ctx.getChild(4).getText()
        value: any = self.convert_string_to_primitive_object(object_type, value_string)
        return PredicateTransition(object_type, sender, receiver, comparator, value)
    
    # Builds a predicate transition with a non-custom type and the "==" comparator from the given SendContext.
    def buildPrimitiveTypeEqualPredicateTransition(self, ctx: PythonicParser.SendContext) -> PredicateTransition:
        object_type: any = self.convert_string_to_type(ctx.getChild(1).getText())
        sender: str = ctx.getChild(6).getText()
        receiver: str = ctx.getChild(8).getText()
        value_string: str = ctx.getChild(3).getText()
        value: any = self.convert_string_to_primitive_object(object_type, value_string)
        return PredicateTransition(object_type, sender, receiver, "==", value)

    # Transforms the given string to a custom object with help of the given 
    # constructor. In case the given string cannot be evaluated to an object,
    # an IllegalValueException is raised. In case the evaluated object is not 
    # an instance of the given type, an SubtypingException is raised.
    def convert_string_to_custom_object(self, object_type: type, constructor: type, value_string: str) -> any:
        try:
            custom_object = eval(value_string, {}, {constructor.__name__: constructor})   
        except TypeError:
            raise IllegalValueException(value_string, object_type)
        if not isinstance(custom_object, object_type):
            raise SubtypingException(object_type, constructor)      
        return custom_object
        
    # Transforms the given string to a primitive object of the given type. 
    def convert_string_to_primitive_object(self, object_type: type, value_string: str) -> any:        
        if object_type == str:
            return value_string[1:len(value_string)-1]
        if object_type == bool:
            return value_string == "True"
        if object_type == int:
            return int(value_string)
        if object_type == float:
            return float(value_string) 
    
    # Transforms the given string to the corresponding type. If the string does not match with the string 
    # representation of either a built-in type or a user-defined type, an IllegalTypeException is raised.
    def convert_string_to_type(self, type_string) -> type:
        # check if the given type is a built-in type
        if type_string in ['int','str','float','bool']:
            return getattr(builtins, type_string)
        # check if the given type is a user-defined type
        elif hasattr(customs, type_string):
            return getattr(customs, type_string)
        # type not found
        else:
            raise IllegalTypeException(type_string)
        
    # Determines the count of defined roles and adds each role to the set of roles.
    def visitRoles(self, ctx:PythonicParser.RolesContext) -> None:
        roleCount: int = ctx.getChild(1).getChildCount() - 2
        roleNodes: range =  range(1, roleCount + 1)
        for roleNode in roleNodes:
            role: str = self.visitRole(ctx.getChild(1).getChild(roleNode))
            self.defined_roles.add(role)

    # Returns the role found in the context.
    def visitRole(self, ctx: PythonicParser.RoleContext) -> str:
        return ctx.getChild(0).getText()
        
    # Parses the given specification in the filePath to a parse tree.
    def buildParseTree(self, filePath: str):
        input = FileStream(filePath)
        lexer = PythonicLexer(input)
        stream = CommonTokenStream(lexer)
        parser = antlrFiles.PythonicParser.PythonicParser(stream)
        return parser.specification() 

del PythonicParser