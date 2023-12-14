from antlr4 import *
import typing
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from antlrFiles.pythonicvisitor import PythonicVisitor
from src.core.fsm import FSM
from src.core.transition import Transition, PredicateTransition
from src.core.state import State
from itertools import permutations

if "." in __name__:
    from antlrFiles.PythonicParser import PythonicParser
else:
    from antlrFiles.PythonicParser import PythonicParser

# FSMBuilder is responsible for building the FSM based on a parse tree produced from a specification by the PythonicParser. 
# The class inherits from PythonicVistor, which is auto-generated by antlr4 based on the grammar file.

class FSMbuilder(PythonicVisitor):

    def __init__(self):
        self.fsm: FSM = FSM()
        self.loop_dictionary: dict[str, State] = {}
        self.roles_in_fsm: set(str) = set()

    # Visits the protocol in the specification and returns the created FSM and all roles
    # that were used in the specification
    def visitSpecification(self, ctx: PythonicParser.SpecificationContext) -> tuple[FSM, set[str]]:
        self.visitProtocol(ctx.getChild(1))
        return self.fsm, self.roles_in_fsm

    # Gets the state of the FSM and visits the first expression found in the protocol
    def visitProtocol(self, ctx: PythonicParser.ProtocolContext) -> None:
        expression: str = ctx.getChild(1).getChild(1).getChild(0)
        expression.startState: State = self.fsm.getStates()[0]
        expression.endState: State = State()
        self.visitExpression(expression) 

    # Checks what expression is offered and continues in the respective visitor
    def visitExpression(self, ctx: PythonicParser.ExpressionContext) -> None:
        expression: str = ctx.getChild(1)
        expression.startState: State = ctx.startState
        expression.endState: State = ctx.endState
        match ctx.getChild(0).getText():
            case "sequence:":
                self.visitSequence(expression)
            case "choice:":
                self.visitChoice(expression)
            case "shuffle:":
                self.visitShuffle(expression)
            case "send":
                self.visitSend(ctx)
            case "close":
                self.visitClose(ctx)
            case "loop":
                self.visitLoop(ctx)

 
    # Builds the fsm sequence part, checks for repeat and end of sequence. Visits the expression that
    # is at each part in the sequence
    def visitSequence(self, ctx:PythonicParser.SequenceContext) -> None:
        repeat: bool = False
        expressionCount: int = ctx.getChildCount() - 2

        # check whether last child is a repeat expression
        lastChild: str = ctx.getChild(expressionCount).getChild(0)
        if lastChild.getChild(0).getText() == "repeat":
            repeat = True
            expressionCount -= 1    

        currentState: State = ctx.startState     
        expressionIndices: range = range(1, expressionCount + 1)
        for index in expressionIndices:
            if index == expressionCount:
                if repeat:
                    loopTag: str = lastChild.getChild(1).getText() 
                    nextState: State =  self.loop_dictionary[loopTag]
                else:
                    nextState: State = ctx.endState
            else:
                nextState: State = State()
            expression: str = ctx.getChild(index).getChild(0)
            expression.startState: State = currentState
            expression.endState: State = nextState
            self.visitExpression(expression)
            currentState = nextState

    # Builds a shuffle part of an fsm, where the expressions in the shuffle are allowed
    # to happen in any order.
    def visitShuffle(self, ctx: PythonicParser.ShuffleContext) -> None:
        expressionCount: int = ctx.getChildCount() - 2
        expressionIndices: range = range(1, expressionCount + 1)
        for indicesPermutation in permutations(expressionIndices):
            counter: int = 0
            currentState: State = ctx.startState
            for index in indicesPermutation:
                counter += 1
                if counter == expressionCount:
                    nextState: State = ctx.endState
                else:
                    nextState = State()
                expression: str = ctx.getChild(index).getChild(0)
                expression.startState: State = currentState
                expression.endState: State = nextState
                self.visitExpression(expression)
                currentState = nextState

    # Builds a choice part of an FSM, where one of two or more options is allowed
    def visitChoice(self, ctx:PythonicParser.ChoiceContext) -> None:
        expressionCount: int = ctx.getChildCount() - 2
        expressionIndices: range =  range(1, expressionCount + 1)
        for index in expressionIndices:
            expression: str = ctx.getChild(index).getChild(0)
            expression.startState: State = ctx.startState
            expression.endState: State = ctx.endState
            self.visitExpression(expression)
    
     # Builds the start of a loop in an FSM and adds the loop tag to the loop_dictionary,
     # so it can be found when the repeat tag is found in a sequence
    def visitLoop(self, ctx:PythonicParser.LoopContext) -> None:
        tag_with_semi_colon: str = ctx.getChild(1).getText()
        tag: str = tag_with_semi_colon[0:len(tag_with_semi_colon) - 1]
        self.loop_dictionary[tag] = ctx.startState
        expression: str = ctx.getChild(2).getChild(1).getChild(0)
        expression.startState: State = ctx.startState
        expression.endState: State = ctx.endState
        self.visitExpression(expression)

    # Builds the send part of an FSM, with three options: regular send, and predicate send 
    # with or without a comparator. Adds the sender and receiver to the used roles set.
    def visitSend(self, ctx: PythonicParser.SendContext) -> None:

        # build transition send without predicate
        if (ctx.getChild(2).getText() == 'from'):
            type: str = ctx.getChild(1).getText()
            sender: str = ctx.getChild(3).getText()
            receiver: str = ctx.getChild(5).getText()
            transition: Transition = Transition(type, sender, receiver)
        # build transition send with a non-equal predicate
        elif ctx.getChild(3).getText() in [">", "<", ">=", "<=", "!="]:
            type: str = ctx.getChild(1).getText()
            comparator: str = ctx.getChild(3).getText()
            value: str = ctx.getChild(4).getText()
            sender: str = ctx.getChild(7).getText()
            receiver: str = ctx.getChild(9).getText()
            value: any = self.stringToValue(type, value)
            transition: PredicateTransition = PredicateTransition(type, sender, receiver, comparator, value)
        # build transition send with an equal comparator
        else :
            type: str = ctx.getChild(1).getText()
            comparator: str = "=="
            valueString: str = ctx.getChild(3).getText()
            sender: str = ctx.getChild(6).getText()
            receiver: str = ctx.getChild(8).getText()
            value: any = self.stringToValue(type, valueString)
            transition: PredicateTransition = PredicateTransition(type, sender, receiver, comparator, value)
        # add transition to state
        ctx.startState.addTransitionToState(transition, ctx.endState)
        self.roles_in_fsm.add(sender)
        self.roles_in_fsm.add(receiver)

    # Transforms a string to a primitive value based on the given type.
    def stringToValue(self, type: str, string: str) -> any:
        match type:
            case "int":
                return int(string)
            case "float":
                return float(string)
            case "bool":
                return string == "True"
            case "str":
                # remove the additional first and last double quotes
                return string[1:len(string)-1]


    def dump(self, node, depth=0, ruleNames=None):
        depthStr = '. ' * depth
        if isinstance(node, TerminalNodeImpl):
            print(f'{depthStr}{node.symbol}')
        else:
            print(f'{depthStr}{Trees.getNodeText(node, ruleNames)}')
            for child in node.children:
                self.dump(child, depth + 1, ruleNames)
    
del PythonicParser
