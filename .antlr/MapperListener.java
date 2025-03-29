// Generated from c:/Users/pryce/Desktop/Kompilatory/Mapper.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MapperParser}.
 */
public interface MapperListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MapperParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MapperParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MapperParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(MapperParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(MapperParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#increment}.
	 * @param ctx the parse tree
	 */
	void enterIncrement(MapperParser.IncrementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#increment}.
	 * @param ctx the parse tree
	 */
	void exitIncrement(MapperParser.IncrementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#tileAssign}.
	 * @param ctx the parse tree
	 */
	void enterTileAssign(MapperParser.TileAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#tileAssign}.
	 * @param ctx the parse tree
	 */
	void exitTileAssign(MapperParser.TileAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#tileSum}.
	 * @param ctx the parse tree
	 */
	void enterTileSum(MapperParser.TileSumContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#tileSum}.
	 * @param ctx the parse tree
	 */
	void exitTileSum(MapperParser.TileSumContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(MapperParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(MapperParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#numberAssign}.
	 * @param ctx the parse tree
	 */
	void enterNumberAssign(MapperParser.NumberAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#numberAssign}.
	 * @param ctx the parse tree
	 */
	void exitNumberAssign(MapperParser.NumberAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#boolAssign}.
	 * @param ctx the parse tree
	 */
	void enterBoolAssign(MapperParser.BoolAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#boolAssign}.
	 * @param ctx the parse tree
	 */
	void exitBoolAssign(MapperParser.BoolAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#roadPlacement}.
	 * @param ctx the parse tree
	 */
	void enterRoadPlacement(MapperParser.RoadPlacementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#roadPlacement}.
	 * @param ctx the parse tree
	 */
	void exitRoadPlacement(MapperParser.RoadPlacementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#roadStart}.
	 * @param ctx the parse tree
	 */
	void enterRoadStart(MapperParser.RoadStartContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#roadStart}.
	 * @param ctx the parse tree
	 */
	void exitRoadStart(MapperParser.RoadStartContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#roadEnd}.
	 * @param ctx the parse tree
	 */
	void enterRoadEnd(MapperParser.RoadEndContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#roadEnd}.
	 * @param ctx the parse tree
	 */
	void exitRoadEnd(MapperParser.RoadEndContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#blendAssign}.
	 * @param ctx the parse tree
	 */
	void enterBlendAssign(MapperParser.BlendAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#blendAssign}.
	 * @param ctx the parse tree
	 */
	void exitBlendAssign(MapperParser.BlendAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#figure}.
	 * @param ctx the parse tree
	 */
	void enterFigure(MapperParser.FigureContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#figure}.
	 * @param ctx the parse tree
	 */
	void exitFigure(MapperParser.FigureContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#blendOption}.
	 * @param ctx the parse tree
	 */
	void enterBlendOption(MapperParser.BlendOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#blendOption}.
	 * @param ctx the parse tree
	 */
	void exitBlendOption(MapperParser.BlendOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#draw}.
	 * @param ctx the parse tree
	 */
	void enterDraw(MapperParser.DrawContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#draw}.
	 * @param ctx the parse tree
	 */
	void exitDraw(MapperParser.DrawContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#percentagePair}.
	 * @param ctx the parse tree
	 */
	void enterPercentagePair(MapperParser.PercentagePairContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#percentagePair}.
	 * @param ctx the parse tree
	 */
	void exitPercentagePair(MapperParser.PercentagePairContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#move}.
	 * @param ctx the parse tree
	 */
	void enterMove(MapperParser.MoveContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#move}.
	 * @param ctx the parse tree
	 */
	void exitMove(MapperParser.MoveContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#loop}.
	 * @param ctx the parse tree
	 */
	void enterLoop(MapperParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#loop}.
	 * @param ctx the parse tree
	 */
	void exitLoop(MapperParser.LoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void enterWhileLoop(MapperParser.WhileLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void exitWhileLoop(MapperParser.WhileLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void enterForLoop(MapperParser.ForLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void exitForLoop(MapperParser.ForLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#conditional}.
	 * @param ctx the parse tree
	 */
	void enterConditional(MapperParser.ConditionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#conditional}.
	 * @param ctx the parse tree
	 */
	void exitConditional(MapperParser.ConditionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#errorHandling}.
	 * @param ctx the parse tree
	 */
	void enterErrorHandling(MapperParser.ErrorHandlingContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#errorHandling}.
	 * @param ctx the parse tree
	 */
	void exitErrorHandling(MapperParser.ErrorHandlingContext ctx);
	/**
	 * Enter a parse tree produced by {@link MapperParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MapperParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MapperParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MapperParser.ExprContext ctx);
}