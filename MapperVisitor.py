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


    # Visit a parse tree produced by MapperParser#block.
    def visitBlock(self, ctx:MapperParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#errorStatement.
    def visitErrorStatement(self, ctx:MapperParser.ErrorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#printStatement.
    def visitPrintStatement(self, ctx:MapperParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#param.
    def visitParam(self, ctx:MapperParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#type.
    def visitType(self, ctx:MapperParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#functionDecl.
    def visitFunctionDecl(self, ctx:MapperParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#functionCall.
    def visitFunctionCall(self, ctx:MapperParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#exprList.
    def visitExprList(self, ctx:MapperParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#increment.
    def visitIncrement(self, ctx:MapperParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#tileSum.
    def visitTileSum(self, ctx:MapperParser.TileSumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#reasignment.
    def visitReasignment(self, ctx:MapperParser.ReasignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#assignment.
    def visitAssignment(self, ctx:MapperParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#noValueAssign.
    def visitNoValueAssign(self, ctx:MapperParser.NoValueAssignContext):
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


    # Visit a parse tree produced by MapperParser#blendAssign.
    def visitBlendAssign(self, ctx:MapperParser.BlendAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#roadStart.
    def visitRoadStart(self, ctx:MapperParser.RoadStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#roadPlacement.
    def visitRoadPlacement(self, ctx:MapperParser.RoadPlacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#roadEnd.
    def visitRoadEnd(self, ctx:MapperParser.RoadEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#figure.
    def visitFigure(self, ctx:MapperParser.FigureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#blendOption.
    def visitBlendOption(self, ctx:MapperParser.BlendOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#drawRoad.
    def visitDrawRoad(self, ctx:MapperParser.DrawRoadContext):
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


    # Visit a parse tree produced by MapperParser#whileLoop.
    def visitWhileLoop(self, ctx:MapperParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#forLoop.
    def visitForLoop(self, ctx:MapperParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#conditional.
    def visitConditional(self, ctx:MapperParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ifConditionStatements.
    def visitIfConditionStatements(self, ctx:MapperParser.IfConditionStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#elseConditionStatements.
    def visitElseConditionStatements(self, ctx:MapperParser.ElseConditionStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprVar.
    def visitExprVar(self, ctx:MapperParser.ExprVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprAddSub.
    def visitExprAddSub(self, ctx:MapperParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprMulDiv.
    def visitExprMulDiv(self, ctx:MapperParser.ExprMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprParens.
    def visitExprParens(self, ctx:MapperParser.ExprParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprInt.
    def visitExprInt(self, ctx:MapperParser.ExprIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprUnaryMinus.
    def visitExprUnaryMinus(self, ctx:MapperParser.ExprUnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprAnd.
    def visitExprAnd(self, ctx:MapperParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprCompRel.
    def visitExprCompRel(self, ctx:MapperParser.ExprCompRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprCompBool.
    def visitExprCompBool(self, ctx:MapperParser.ExprCompBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprCompVar.
    def visitExprCompVar(self, ctx:MapperParser.ExprCompVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprCompBools.
    def visitExprCompBools(self, ctx:MapperParser.ExprCompBoolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprOr.
    def visitExprOr(self, ctx:MapperParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprNot.
    def visitExprNot(self, ctx:MapperParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapperParser#ExprCompParens.
    def visitExprCompParens(self, ctx:MapperParser.ExprCompParensContext):
        return self.visitChildren(ctx)



del MapperParser