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


    # Enter a parse tree produced by MapperParser#block.
    def enterBlock(self, ctx:MapperParser.BlockContext):
        pass

    # Exit a parse tree produced by MapperParser#block.
    def exitBlock(self, ctx:MapperParser.BlockContext):
        pass


    # Enter a parse tree produced by MapperParser#printStatement.
    def enterPrintStatement(self, ctx:MapperParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MapperParser#printStatement.
    def exitPrintStatement(self, ctx:MapperParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MapperParser#param.
    def enterParam(self, ctx:MapperParser.ParamContext):
        pass

    # Exit a parse tree produced by MapperParser#param.
    def exitParam(self, ctx:MapperParser.ParamContext):
        pass


    # Enter a parse tree produced by MapperParser#type.
    def enterType(self, ctx:MapperParser.TypeContext):
        pass

    # Exit a parse tree produced by MapperParser#type.
    def exitType(self, ctx:MapperParser.TypeContext):
        pass


    # Enter a parse tree produced by MapperParser#functionDecl.
    def enterFunctionDecl(self, ctx:MapperParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by MapperParser#functionDecl.
    def exitFunctionDecl(self, ctx:MapperParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by MapperParser#exprOrExprComp.
    def enterExprOrExprComp(self, ctx:MapperParser.ExprOrExprCompContext):
        pass

    # Exit a parse tree produced by MapperParser#exprOrExprComp.
    def exitExprOrExprComp(self, ctx:MapperParser.ExprOrExprCompContext):
        pass


    # Enter a parse tree produced by MapperParser#functionCall.
    def enterFunctionCall(self, ctx:MapperParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MapperParser#functionCall.
    def exitFunctionCall(self, ctx:MapperParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MapperParser#returnStatement.
    def enterReturnStatement(self, ctx:MapperParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MapperParser#returnStatement.
    def exitReturnStatement(self, ctx:MapperParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MapperParser#exprList.
    def enterExprList(self, ctx:MapperParser.ExprListContext):
        pass

    # Exit a parse tree produced by MapperParser#exprList.
    def exitExprList(self, ctx:MapperParser.ExprListContext):
        pass


    # Enter a parse tree produced by MapperParser#increment.
    def enterIncrement(self, ctx:MapperParser.IncrementContext):
        pass

    # Exit a parse tree produced by MapperParser#increment.
    def exitIncrement(self, ctx:MapperParser.IncrementContext):
        pass


    # Enter a parse tree produced by MapperParser#tileSum.
    def enterTileSum(self, ctx:MapperParser.TileSumContext):
        pass

    # Exit a parse tree produced by MapperParser#tileSum.
    def exitTileSum(self, ctx:MapperParser.TileSumContext):
        pass


    # Enter a parse tree produced by MapperParser#reasignment.
    def enterReasignment(self, ctx:MapperParser.ReasignmentContext):
        pass

    # Exit a parse tree produced by MapperParser#reasignment.
    def exitReasignment(self, ctx:MapperParser.ReasignmentContext):
        pass


    # Enter a parse tree produced by MapperParser#assignment.
    def enterAssignment(self, ctx:MapperParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MapperParser#assignment.
    def exitAssignment(self, ctx:MapperParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MapperParser#noValueAssign.
    def enterNoValueAssign(self, ctx:MapperParser.NoValueAssignContext):
        pass

    # Exit a parse tree produced by MapperParser#noValueAssign.
    def exitNoValueAssign(self, ctx:MapperParser.NoValueAssignContext):
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


    # Enter a parse tree produced by MapperParser#blendAssign.
    def enterBlendAssign(self, ctx:MapperParser.BlendAssignContext):
        pass

    # Exit a parse tree produced by MapperParser#blendAssign.
    def exitBlendAssign(self, ctx:MapperParser.BlendAssignContext):
        pass


    # Enter a parse tree produced by MapperParser#roadStart.
    def enterRoadStart(self, ctx:MapperParser.RoadStartContext):
        pass

    # Exit a parse tree produced by MapperParser#roadStart.
    def exitRoadStart(self, ctx:MapperParser.RoadStartContext):
        pass


    # Enter a parse tree produced by MapperParser#roadPlacement.
    def enterRoadPlacement(self, ctx:MapperParser.RoadPlacementContext):
        pass

    # Exit a parse tree produced by MapperParser#roadPlacement.
    def exitRoadPlacement(self, ctx:MapperParser.RoadPlacementContext):
        pass


    # Enter a parse tree produced by MapperParser#roadEnd.
    def enterRoadEnd(self, ctx:MapperParser.RoadEndContext):
        pass

    # Exit a parse tree produced by MapperParser#roadEnd.
    def exitRoadEnd(self, ctx:MapperParser.RoadEndContext):
        pass


    # Enter a parse tree produced by MapperParser#figure.
    def enterFigure(self, ctx:MapperParser.FigureContext):
        pass

    # Exit a parse tree produced by MapperParser#figure.
    def exitFigure(self, ctx:MapperParser.FigureContext):
        pass


    # Enter a parse tree produced by MapperParser#blendOption.
    def enterBlendOption(self, ctx:MapperParser.BlendOptionContext):
        pass

    # Exit a parse tree produced by MapperParser#blendOption.
    def exitBlendOption(self, ctx:MapperParser.BlendOptionContext):
        pass


    # Enter a parse tree produced by MapperParser#drawRoad.
    def enterDrawRoad(self, ctx:MapperParser.DrawRoadContext):
        pass

    # Exit a parse tree produced by MapperParser#drawRoad.
    def exitDrawRoad(self, ctx:MapperParser.DrawRoadContext):
        pass


    # Enter a parse tree produced by MapperParser#draw.
    def enterDraw(self, ctx:MapperParser.DrawContext):
        pass

    # Exit a parse tree produced by MapperParser#draw.
    def exitDraw(self, ctx:MapperParser.DrawContext):
        pass


    # Enter a parse tree produced by MapperParser#percentagePair.
    def enterPercentagePair(self, ctx:MapperParser.PercentagePairContext):
        pass

    # Exit a parse tree produced by MapperParser#percentagePair.
    def exitPercentagePair(self, ctx:MapperParser.PercentagePairContext):
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


    # Enter a parse tree produced by MapperParser#whileLoop.
    def enterWhileLoop(self, ctx:MapperParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by MapperParser#whileLoop.
    def exitWhileLoop(self, ctx:MapperParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by MapperParser#forLoop.
    def enterForLoop(self, ctx:MapperParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MapperParser#forLoop.
    def exitForLoop(self, ctx:MapperParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MapperParser#conditional.
    def enterConditional(self, ctx:MapperParser.ConditionalContext):
        pass

    # Exit a parse tree produced by MapperParser#conditional.
    def exitConditional(self, ctx:MapperParser.ConditionalContext):
        pass


    # Enter a parse tree produced by MapperParser#ifConditionStatements.
    def enterIfConditionStatements(self, ctx:MapperParser.IfConditionStatementsContext):
        pass

    # Exit a parse tree produced by MapperParser#ifConditionStatements.
    def exitIfConditionStatements(self, ctx:MapperParser.IfConditionStatementsContext):
        pass


    # Enter a parse tree produced by MapperParser#elseConditionStatements.
    def enterElseConditionStatements(self, ctx:MapperParser.ElseConditionStatementsContext):
        pass

    # Exit a parse tree produced by MapperParser#elseConditionStatements.
    def exitElseConditionStatements(self, ctx:MapperParser.ElseConditionStatementsContext):
        pass


    # Enter a parse tree produced by MapperParser#scopedIdentifier.
    def enterScopedIdentifier(self, ctx:MapperParser.ScopedIdentifierContext):
        pass

    # Exit a parse tree produced by MapperParser#scopedIdentifier.
    def exitScopedIdentifier(self, ctx:MapperParser.ScopedIdentifierContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprAddSub.
    def enterExprAddSub(self, ctx:MapperParser.ExprAddSubContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprAddSub.
    def exitExprAddSub(self, ctx:MapperParser.ExprAddSubContext):
        pass


    # Enter a parse tree produced by MapperParser#ScopedExprVar.
    def enterScopedExprVar(self, ctx:MapperParser.ScopedExprVarContext):
        pass

    # Exit a parse tree produced by MapperParser#ScopedExprVar.
    def exitScopedExprVar(self, ctx:MapperParser.ScopedExprVarContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprMulDiv.
    def enterExprMulDiv(self, ctx:MapperParser.ExprMulDivContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprMulDiv.
    def exitExprMulDiv(self, ctx:MapperParser.ExprMulDivContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprParens.
    def enterExprParens(self, ctx:MapperParser.ExprParensContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprParens.
    def exitExprParens(self, ctx:MapperParser.ExprParensContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprInt.
    def enterExprInt(self, ctx:MapperParser.ExprIntContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprInt.
    def exitExprInt(self, ctx:MapperParser.ExprIntContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprFUnctionCall.
    def enterExprFUnctionCall(self, ctx:MapperParser.ExprFUnctionCallContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprFUnctionCall.
    def exitExprFUnctionCall(self, ctx:MapperParser.ExprFUnctionCallContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprUnaryMinus.
    def enterExprUnaryMinus(self, ctx:MapperParser.ExprUnaryMinusContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprUnaryMinus.
    def exitExprUnaryMinus(self, ctx:MapperParser.ExprUnaryMinusContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprAnd.
    def enterExprAnd(self, ctx:MapperParser.ExprAndContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprAnd.
    def exitExprAnd(self, ctx:MapperParser.ExprAndContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprCompRel.
    def enterExprCompRel(self, ctx:MapperParser.ExprCompRelContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprCompRel.
    def exitExprCompRel(self, ctx:MapperParser.ExprCompRelContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprCompBool.
    def enterExprCompBool(self, ctx:MapperParser.ExprCompBoolContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprCompBool.
    def exitExprCompBool(self, ctx:MapperParser.ExprCompBoolContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprCompVar.
    def enterExprCompVar(self, ctx:MapperParser.ExprCompVarContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprCompVar.
    def exitExprCompVar(self, ctx:MapperParser.ExprCompVarContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprCompBools.
    def enterExprCompBools(self, ctx:MapperParser.ExprCompBoolsContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprCompBools.
    def exitExprCompBools(self, ctx:MapperParser.ExprCompBoolsContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprOr.
    def enterExprOr(self, ctx:MapperParser.ExprOrContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprOr.
    def exitExprOr(self, ctx:MapperParser.ExprOrContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprNot.
    def enterExprNot(self, ctx:MapperParser.ExprNotContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprNot.
    def exitExprNot(self, ctx:MapperParser.ExprNotContext):
        pass


    # Enter a parse tree produced by MapperParser#ExprCompParens.
    def enterExprCompParens(self, ctx:MapperParser.ExprCompParensContext):
        pass

    # Exit a parse tree produced by MapperParser#ExprCompParens.
    def exitExprCompParens(self, ctx:MapperParser.ExprCompParensContext):
        pass



del MapperParser