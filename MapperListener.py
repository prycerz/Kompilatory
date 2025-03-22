# Generated from Mapper.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapperParser import MapperParser
else:
    from MapperParser import MapperParser

# This class defines a complete listener for a parse tree produced by MapperParser.
class MapperListener(ParseTreeListener):

    # Enter a parse tree produced by MapperParser#program.
    def enterProgram(self, ctx:MapperParser.ProgramContext):
        pass

    # Exit a parse tree produced by MapperParser#program.
    def exitProgram(self, ctx:MapperParser.ProgramContext):
        pass


    # Enter a parse tree produced by MapperParser#statement.
    def enterStatement(self, ctx:MapperParser.StatementContext):
        pass

    # Exit a parse tree produced by MapperParser#statement.
    def exitStatement(self, ctx:MapperParser.StatementContext):
        pass


    # Enter a parse tree produced by MapperParser#tileAssign.
    def enterTileAssign(self, ctx:MapperParser.TileAssignContext):
        pass

    # Exit a parse tree produced by MapperParser#tileAssign.
    def exitTileAssign(self, ctx:MapperParser.TileAssignContext):
        pass


    # Enter a parse tree produced by MapperParser#numberAssign.
    def enterNumberAssign(self, ctx:MapperParser.NumberAssignContext):
        pass

    # Exit a parse tree produced by MapperParser#numberAssign.
    def exitNumberAssign(self, ctx:MapperParser.NumberAssignContext):
        pass


    # Enter a parse tree produced by MapperParser#boolAssign.
    def enterBoolAssign(self, ctx:MapperParser.BoolAssignContext):
        pass

    # Exit a parse tree produced by MapperParser#boolAssign.
    def exitBoolAssign(self, ctx:MapperParser.BoolAssignContext):
        pass


    # Enter a parse tree produced by MapperParser#assignment.
    def enterAssignment(self, ctx:MapperParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MapperParser#assignment.
    def exitAssignment(self, ctx:MapperParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MapperParser#draw.
    def enterDraw(self, ctx:MapperParser.DrawContext):
        pass

    # Exit a parse tree produced by MapperParser#draw.
    def exitDraw(self, ctx:MapperParser.DrawContext):
        pass


    # Enter a parse tree produced by MapperParser#move.
    def enterMove(self, ctx:MapperParser.MoveContext):
        pass

    # Exit a parse tree produced by MapperParser#move.
    def exitMove(self, ctx:MapperParser.MoveContext):
        pass


    # Enter a parse tree produced by MapperParser#loop.
    def enterLoop(self, ctx:MapperParser.LoopContext):
        pass

    # Exit a parse tree produced by MapperParser#loop.
    def exitLoop(self, ctx:MapperParser.LoopContext):
        pass


    # Enter a parse tree produced by MapperParser#conditional.
    def enterConditional(self, ctx:MapperParser.ConditionalContext):
        pass

    # Exit a parse tree produced by MapperParser#conditional.
    def exitConditional(self, ctx:MapperParser.ConditionalContext):
        pass


    # Enter a parse tree produced by MapperParser#errorHandling.
    def enterErrorHandling(self, ctx:MapperParser.ErrorHandlingContext):
        pass

    # Exit a parse tree produced by MapperParser#errorHandling.
    def exitErrorHandling(self, ctx:MapperParser.ErrorHandlingContext):
        pass


    # Enter a parse tree produced by MapperParser#expr.
    def enterExpr(self, ctx:MapperParser.ExprContext):
        pass

    # Exit a parse tree produced by MapperParser#expr.
    def exitExpr(self, ctx:MapperParser.ExprContext):
        pass



del MapperParser