from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from antlrFiles.pythonicvisitor import PythonicVisitor


if "." in __name__:
    from antlrFiles.PythonicParser import PythonicParser
else:
    from antlrFiles.PythonicParser import PythonicParser

# This class builds an FSM using a visitor for a parse tree produced by PythonicParser.

class Rolebuilder(PythonicVisitor):

    def __init__(self):
        self.roles = set()

    # Visit a parse tree produced by PythonicParser#specification.
    def visitSpecification(self, ctx:PythonicParser.SpecificationContext):
        self.visitRoles(ctx.getChild(0))
        return self.roles
    
    # Visit a parse tree produced by PythonicParser#role.
    def visitRole(self, ctx:PythonicParser.RoleContext):
        return ctx.getChild(0).getText()

    # Visit a parse tree produced by PythonicParser#roles.
    def visitRoles(self, ctx:PythonicParser.RolesContext):
        roleCount = ctx.getChild(1).getChildCount() - 2
        roleNodes =  range(1, roleCount + 1)
        for roleNode in roleNodes:
            role = self.visitRole(ctx.getChild(1).getChild(roleNode))
            self.roles.add(role)

    def dump(self, node, depth=0, ruleNames=None):
        depthStr = '. ' * depth
        if isinstance(node, TerminalNodeImpl):
            print(f'{depthStr}{node.symbol}')
        else:
            print(f'{depthStr}{Trees.getNodeText(node, ruleNames)}')
            for child in node.children:
                self.dump(child, depth + 1, ruleNames)