# Generated from Mapper.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapperParser import MapperParser
else:
    from MapperParser import MapperParser

# This class defines a complete generic visitor for a parse tree produced by MapperParser.

class MapperVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MapperParser#program.
    def visitProgram(self, ctx:MapperParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#statement.
    def visitStatement(self, ctx:MapperParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#increment.
    def visitIncrement(self, ctx:MapperParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#tileAssign.
    def visitTileAssign(self, ctx:MapperParser.TileAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#numberAssign.
    def visitNumberAssign(self, ctx:MapperParser.NumberAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#boolAssign.
    def visitBoolAssign(self, ctx:MapperParser.BoolAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#assignment.
    def visitAssignment(self, ctx:MapperParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#draw.
    def visitDraw(self, ctx:MapperParser.DrawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#percentagePair.
    def visitPercentagePair(self, ctx:MapperParser.PercentagePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#move.
    def visitMove(self, ctx:MapperParser.MoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#loop.
    def visitLoop(self, ctx:MapperParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#conditional.
    def visitConditional(self, ctx:MapperParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#errorHandling.
    def visitErrorHandling(self, ctx:MapperParser.ErrorHandlingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#expr.
    def visitExpr(self, ctx:MapperParser.ExprContext):
        return self.visitChildren(ctx)



del MapperParser