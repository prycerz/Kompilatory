// Generated from c:/Users/pryce/Desktop/Kompilatory/Mapper.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MapperParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, IDENTIFIER=37, INT=38, 
		BOOL=39, STRING=40, WS=41;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_increment = 2, RULE_tileAssign = 3, 
		RULE_assignment = 4, RULE_numberAssign = 5, RULE_boolAssign = 6, RULE_blendAssign = 7, 
		RULE_figure = 8, RULE_blendOption = 9, RULE_draw = 10, RULE_percentagePair = 11, 
		RULE_move = 12, RULE_loop = 13, RULE_whileLoop = 14, RULE_forLoop = 15, 
		RULE_conditional = 16, RULE_errorHandling = 17, RULE_expr = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "increment", "tileAssign", "assignment", "numberAssign", 
			"boolAssign", "blendAssign", "figure", "blendOption", "draw", "percentagePair", 
			"move", "loop", "whileLoop", "forLoop", "conditional", "errorHandling", 
			"expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'+='", "'tile'", "'='", "'+'", "'number'", "'bool'", "'blend'", 
			"'circle'", "'rectangle'", "'%'", "'draw'", "'radius'", "'pointer'", 
			"'up'", "'down'", "'left'", "'right'", "'while'", "'('", "')'", "'{'", 
			"'}'", "'for'", "';'", "'if'", "'else'", "'Yapping'", "'-'", "'*'", "'/'", 
			"'=='", "'!='", "'>'", "'<'", "'>='", "'<='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "IDENTIFIER", "INT", "BOOL", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Mapper.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MapperParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MapperParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137615386852L) != 0)) {
				{
				{
				setState(38);
				statement();
				}
				}
				setState(43);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(44);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public DrawContext draw() {
			return getRuleContext(DrawContext.class,0);
		}
		public MoveContext move() {
			return getRuleContext(MoveContext.class,0);
		}
		public LoopContext loop() {
			return getRuleContext(LoopContext.class,0);
		}
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public ErrorHandlingContext errorHandling() {
			return getRuleContext(ErrorHandlingContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__4:
			case T__5:
			case T__6:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				assignment();
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 2);
				{
				setState(47);
				draw();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 3);
				{
				setState(48);
				move();
				}
				break;
			case T__17:
			case T__22:
				enterOuterAlt(_localctx, 4);
				{
				setState(49);
				loop();
				}
				break;
			case T__24:
				enterOuterAlt(_localctx, 5);
				{
				setState(50);
				conditional();
				}
				break;
			case T__26:
				enterOuterAlt(_localctx, 6);
				{
				setState(51);
				errorHandling();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IncrementContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MapperParser.IDENTIFIER, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IncrementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_increment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterIncrement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitIncrement(this);
		}
	}

	public final IncrementContext increment() throws RecognitionException {
		IncrementContext _localctx = new IncrementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_increment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(IDENTIFIER);
			setState(55);
			match(T__0);
			setState(56);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TileAssignContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(MapperParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(MapperParser.IDENTIFIER, i);
		}
		public TileAssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tileAssign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterTileAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitTileAssign(this);
		}
	}

	public final TileAssignContext tileAssign() throws RecognitionException {
		TileAssignContext _localctx = new TileAssignContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tileAssign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(T__1);
			setState(59);
			match(IDENTIFIER);
			setState(60);
			match(T__2);
			setState(61);
			match(IDENTIFIER);
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(62);
				match(T__3);
				setState(63);
				match(IDENTIFIER);
				}
				}
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TileAssignContext tileAssign() {
			return getRuleContext(TileAssignContext.class,0);
		}
		public NumberAssignContext numberAssign() {
			return getRuleContext(NumberAssignContext.class,0);
		}
		public BoolAssignContext boolAssign() {
			return getRuleContext(BoolAssignContext.class,0);
		}
		public IncrementContext increment() {
			return getRuleContext(IncrementContext.class,0);
		}
		public BlendAssignContext blendAssign() {
			return getRuleContext(BlendAssignContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assignment);
		try {
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				tileAssign();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				numberAssign();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 3);
				{
				setState(71);
				boolAssign();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 4);
				{
				setState(72);
				increment();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 5);
				{
				setState(73);
				blendAssign();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberAssignContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MapperParser.IDENTIFIER, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NumberAssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numberAssign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterNumberAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitNumberAssign(this);
		}
	}

	public final NumberAssignContext numberAssign() throws RecognitionException {
		NumberAssignContext _localctx = new NumberAssignContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_numberAssign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(T__4);
			setState(77);
			match(IDENTIFIER);
			setState(78);
			match(T__2);
			setState(79);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoolAssignContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MapperParser.IDENTIFIER, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public BoolAssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolAssign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterBoolAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitBoolAssign(this);
		}
	}

	public final BoolAssignContext boolAssign() throws RecognitionException {
		BoolAssignContext _localctx = new BoolAssignContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_boolAssign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__5);
			setState(82);
			match(IDENTIFIER);
			setState(83);
			match(T__2);
			setState(84);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlendAssignContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MapperParser.IDENTIFIER, 0); }
		public FigureContext figure() {
			return getRuleContext(FigureContext.class,0);
		}
		public List<BlendOptionContext> blendOption() {
			return getRuleContexts(BlendOptionContext.class);
		}
		public BlendOptionContext blendOption(int i) {
			return getRuleContext(BlendOptionContext.class,i);
		}
		public BlendAssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blendAssign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterBlendAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitBlendAssign(this);
		}
	}

	public final BlendAssignContext blendAssign() throws RecognitionException {
		BlendAssignContext _localctx = new BlendAssignContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_blendAssign);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(T__6);
			setState(87);
			match(IDENTIFIER);
			setState(88);
			match(T__2);
			setState(89);
			figure();
			setState(91); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(90);
					blendOption();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(93); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FigureContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(MapperParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(MapperParser.INT, i);
		}
		public FigureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_figure; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterFigure(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitFigure(this);
		}
	}

	public final FigureContext figure() throws RecognitionException {
		FigureContext _localctx = new FigureContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_figure);
		try {
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__7:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(95);
				match(T__7);
				setState(96);
				match(INT);
				}
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(97);
				match(T__8);
				setState(98);
				match(INT);
				setState(99);
				match(INT);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlendOptionContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MapperParser.IDENTIFIER, 0); }
		public TerminalNode INT() { return getToken(MapperParser.INT, 0); }
		public BlendOptionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blendOption; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterBlendOption(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitBlendOption(this);
		}
	}

	public final BlendOptionContext blendOption() throws RecognitionException {
		BlendOptionContext _localctx = new BlendOptionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_blendOption);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(IDENTIFIER);
			setState(103);
			match(INT);
			setState(104);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DrawContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(MapperParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(MapperParser.IDENTIFIER, i);
		}
		public TerminalNode INT() { return getToken(MapperParser.INT, 0); }
		public List<PercentagePairContext> percentagePair() {
			return getRuleContexts(PercentagePairContext.class);
		}
		public PercentagePairContext percentagePair(int i) {
			return getRuleContext(PercentagePairContext.class,i);
		}
		public DrawContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_draw; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterDraw(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitDraw(this);
		}
	}

	public final DrawContext draw() throws RecognitionException {
		DrawContext _localctx = new DrawContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_draw);
		int _la;
		try {
			setState(123);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				match(T__10);
				setState(107);
				match(IDENTIFIER);
				setState(112);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(108);
					match(T__3);
					setState(109);
					match(IDENTIFIER);
					}
					}
					setState(114);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(115);
				match(T__10);
				setState(116);
				match(T__11);
				setState(117);
				match(INT);
				setState(119); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(118);
					percentagePair();
					}
					}
					setState(121); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==INT );
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PercentagePairContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(MapperParser.INT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(MapperParser.IDENTIFIER, 0); }
		public PercentagePairContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_percentagePair; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterPercentagePair(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitPercentagePair(this);
		}
	}

	public final PercentagePairContext percentagePair() throws RecognitionException {
		PercentagePairContext _localctx = new PercentagePairContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_percentagePair);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(INT);
			setState(126);
			match(T__9);
			setState(127);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MoveContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MoveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_move; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterMove(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitMove(this);
		}
	}

	public final MoveContext move() throws RecognitionException {
		MoveContext _localctx = new MoveContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_move);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(T__12);
			setState(138);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__13:
				{
				setState(130);
				match(T__13);
				setState(131);
				expr(0);
				}
				break;
			case T__14:
				{
				setState(132);
				match(T__14);
				setState(133);
				expr(0);
				}
				break;
			case T__15:
				{
				setState(134);
				match(T__15);
				setState(135);
				expr(0);
				}
				break;
			case T__16:
				{
				setState(136);
				match(T__16);
				setState(137);
				expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoopContext extends ParserRuleContext {
		public WhileLoopContext whileLoop() {
			return getRuleContext(WhileLoopContext.class,0);
		}
		public ForLoopContext forLoop() {
			return getRuleContext(ForLoopContext.class,0);
		}
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitLoop(this);
		}
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_loop);
		try {
			setState(142);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__17:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				whileLoop();
				}
				break;
			case T__22:
				enterOuterAlt(_localctx, 2);
				{
				setState(141);
				forLoop();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileLoopContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public WhileLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileLoop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterWhileLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitWhileLoop(this);
		}
	}

	public final WhileLoopContext whileLoop() throws RecognitionException {
		WhileLoopContext _localctx = new WhileLoopContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_whileLoop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			match(T__17);
			setState(145);
			match(T__18);
			setState(146);
			expr(0);
			setState(147);
			match(T__19);
			setState(148);
			match(T__20);
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137615386852L) != 0)) {
				{
				{
				setState(149);
				statement();
				}
				}
				setState(154);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(155);
			match(T__21);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForLoopContext extends ParserRuleContext {
		public NumberAssignContext numberAssign() {
			return getRuleContext(NumberAssignContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IncrementContext increment() {
			return getRuleContext(IncrementContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ForLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forLoop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterForLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitForLoop(this);
		}
	}

	public final ForLoopContext forLoop() throws RecognitionException {
		ForLoopContext _localctx = new ForLoopContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_forLoop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(T__22);
			setState(158);
			match(T__18);
			setState(159);
			numberAssign();
			setState(160);
			match(T__23);
			setState(161);
			expr(0);
			setState(162);
			match(T__23);
			setState(163);
			increment();
			setState(164);
			match(T__19);
			setState(165);
			match(T__20);
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137615386852L) != 0)) {
				{
				{
				setState(166);
				statement();
				}
				}
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(172);
			match(T__21);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionalContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterConditional(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitConditional(this);
		}
	}

	public final ConditionalContext conditional() throws RecognitionException {
		ConditionalContext _localctx = new ConditionalContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_conditional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(T__24);
			setState(175);
			match(T__18);
			setState(176);
			expr(0);
			setState(177);
			match(T__19);
			setState(178);
			match(T__20);
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137615386852L) != 0)) {
				{
				{
				setState(179);
				statement();
				}
				}
				setState(184);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(185);
			match(T__21);
			setState(195);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25) {
				{
				setState(186);
				match(T__25);
				setState(187);
				match(T__20);
				setState(191);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137615386852L) != 0)) {
					{
					{
					setState(188);
					statement();
					}
					}
					setState(193);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(194);
				match(T__21);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ErrorHandlingContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(MapperParser.STRING, 0); }
		public ErrorHandlingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_errorHandling; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterErrorHandling(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitErrorHandling(this);
		}
	}

	public final ErrorHandlingContext errorHandling() throws RecognitionException {
		ErrorHandlingContext _localctx = new ErrorHandlingContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_errorHandling);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(T__26);
			setState(198);
			match(T__18);
			setState(199);
			match(STRING);
			setState(200);
			match(T__19);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode IDENTIFIER() { return getToken(MapperParser.IDENTIFIER, 0); }
		public TerminalNode INT() { return getToken(MapperParser.INT, 0); }
		public TerminalNode BOOL() { return getToken(MapperParser.BOOL, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MapperListener ) ((MapperListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__18:
				{
				setState(203);
				match(T__18);
				setState(204);
				expr(0);
				setState(205);
				match(T__19);
				}
				break;
			case IDENTIFIER:
				{
				setState(207);
				match(IDENTIFIER);
				}
				break;
			case INT:
				{
				setState(208);
				match(INT);
				}
				break;
			case BOOL:
				{
				setState(209);
				match(BOOL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(223);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(221);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(212);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(213);
						_la = _input.LA(1);
						if ( !(_la==T__3 || _la==T__27) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(214);
						expr(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(215);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(216);
						_la = _input.LA(1);
						if ( !(_la==T__28 || _la==T__29) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(217);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(218);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(219);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 135291469824L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(220);
						expr(6);
						}
						break;
					}
					} 
				}
				setState(225);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 18:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001)\u00e3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0005\u0000(\b\u0000\n\u0000\f\u0000+\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u00015\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0005\u0003A\b\u0003\n\u0003\f\u0003D\t\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004K\b\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0004\u0007\\\b\u0007\u000b\u0007"+
		"\f\u0007]\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\be\b\b\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0005\no\b\n"+
		"\n\n\f\nr\t\n\u0001\n\u0001\n\u0001\n\u0001\n\u0004\nx\b\n\u000b\n\f\n"+
		"y\u0003\n|\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003"+
		"\f\u008b\b\f\u0001\r\u0001\r\u0003\r\u008f\b\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u0097\b\u000e"+
		"\n\u000e\f\u000e\u009a\t\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00a8\b\u000f\n\u000f\f\u000f"+
		"\u00ab\t\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00b5\b\u0010\n\u0010"+
		"\f\u0010\u00b8\t\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0005\u0010\u00be\b\u0010\n\u0010\f\u0010\u00c1\t\u0010\u0001\u0010\u0003"+
		"\u0010\u00c4\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00d3\b\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0005\u0012\u00de\b\u0012\n\u0012\f\u0012\u00e1\t\u0012"+
		"\u0001\u0012\u0000\u0001$\u0013\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$\u0000\u0003\u0002\u0000"+
		"\u0004\u0004\u001c\u001c\u0001\u0000\u001d\u001e\u0001\u0000\u001f$\u00ee"+
		"\u0000)\u0001\u0000\u0000\u0000\u00024\u0001\u0000\u0000\u0000\u00046"+
		"\u0001\u0000\u0000\u0000\u0006:\u0001\u0000\u0000\u0000\bJ\u0001\u0000"+
		"\u0000\u0000\nL\u0001\u0000\u0000\u0000\fQ\u0001\u0000\u0000\u0000\u000e"+
		"V\u0001\u0000\u0000\u0000\u0010d\u0001\u0000\u0000\u0000\u0012f\u0001"+
		"\u0000\u0000\u0000\u0014{\u0001\u0000\u0000\u0000\u0016}\u0001\u0000\u0000"+
		"\u0000\u0018\u0081\u0001\u0000\u0000\u0000\u001a\u008e\u0001\u0000\u0000"+
		"\u0000\u001c\u0090\u0001\u0000\u0000\u0000\u001e\u009d\u0001\u0000\u0000"+
		"\u0000 \u00ae\u0001\u0000\u0000\u0000\"\u00c5\u0001\u0000\u0000\u0000"+
		"$\u00d2\u0001\u0000\u0000\u0000&(\u0003\u0002\u0001\u0000\'&\u0001\u0000"+
		"\u0000\u0000(+\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001"+
		"\u0000\u0000\u0000*,\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000"+
		",-\u0005\u0000\u0000\u0001-\u0001\u0001\u0000\u0000\u0000.5\u0003\b\u0004"+
		"\u0000/5\u0003\u0014\n\u000005\u0003\u0018\f\u000015\u0003\u001a\r\u0000"+
		"25\u0003 \u0010\u000035\u0003\"\u0011\u00004.\u0001\u0000\u0000\u0000"+
		"4/\u0001\u0000\u0000\u000040\u0001\u0000\u0000\u000041\u0001\u0000\u0000"+
		"\u000042\u0001\u0000\u0000\u000043\u0001\u0000\u0000\u00005\u0003\u0001"+
		"\u0000\u0000\u000067\u0005%\u0000\u000078\u0005\u0001\u0000\u000089\u0003"+
		"$\u0012\u00009\u0005\u0001\u0000\u0000\u0000:;\u0005\u0002\u0000\u0000"+
		";<\u0005%\u0000\u0000<=\u0005\u0003\u0000\u0000=B\u0005%\u0000\u0000>"+
		"?\u0005\u0004\u0000\u0000?A\u0005%\u0000\u0000@>\u0001\u0000\u0000\u0000"+
		"AD\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000"+
		"\u0000C\u0007\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000EK\u0003"+
		"\u0006\u0003\u0000FK\u0003\n\u0005\u0000GK\u0003\f\u0006\u0000HK\u0003"+
		"\u0004\u0002\u0000IK\u0003\u000e\u0007\u0000JE\u0001\u0000\u0000\u0000"+
		"JF\u0001\u0000\u0000\u0000JG\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000"+
		"\u0000JI\u0001\u0000\u0000\u0000K\t\u0001\u0000\u0000\u0000LM\u0005\u0005"+
		"\u0000\u0000MN\u0005%\u0000\u0000NO\u0005\u0003\u0000\u0000OP\u0003$\u0012"+
		"\u0000P\u000b\u0001\u0000\u0000\u0000QR\u0005\u0006\u0000\u0000RS\u0005"+
		"%\u0000\u0000ST\u0005\u0003\u0000\u0000TU\u0003$\u0012\u0000U\r\u0001"+
		"\u0000\u0000\u0000VW\u0005\u0007\u0000\u0000WX\u0005%\u0000\u0000XY\u0005"+
		"\u0003\u0000\u0000Y[\u0003\u0010\b\u0000Z\\\u0003\u0012\t\u0000[Z\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000"+
		"]^\u0001\u0000\u0000\u0000^\u000f\u0001\u0000\u0000\u0000_`\u0005\b\u0000"+
		"\u0000`e\u0005&\u0000\u0000ab\u0005\t\u0000\u0000bc\u0005&\u0000\u0000"+
		"ce\u0005&\u0000\u0000d_\u0001\u0000\u0000\u0000da\u0001\u0000\u0000\u0000"+
		"e\u0011\u0001\u0000\u0000\u0000fg\u0005%\u0000\u0000gh\u0005&\u0000\u0000"+
		"hi\u0005\n\u0000\u0000i\u0013\u0001\u0000\u0000\u0000jk\u0005\u000b\u0000"+
		"\u0000kp\u0005%\u0000\u0000lm\u0005\u0004\u0000\u0000mo\u0005%\u0000\u0000"+
		"nl\u0001\u0000\u0000\u0000or\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000"+
		"\u0000pq\u0001\u0000\u0000\u0000q|\u0001\u0000\u0000\u0000rp\u0001\u0000"+
		"\u0000\u0000st\u0005\u000b\u0000\u0000tu\u0005\f\u0000\u0000uw\u0005&"+
		"\u0000\u0000vx\u0003\u0016\u000b\u0000wv\u0001\u0000\u0000\u0000xy\u0001"+
		"\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000"+
		"z|\u0001\u0000\u0000\u0000{j\u0001\u0000\u0000\u0000{s\u0001\u0000\u0000"+
		"\u0000|\u0015\u0001\u0000\u0000\u0000}~\u0005&\u0000\u0000~\u007f\u0005"+
		"\n\u0000\u0000\u007f\u0080\u0005%\u0000\u0000\u0080\u0017\u0001\u0000"+
		"\u0000\u0000\u0081\u008a\u0005\r\u0000\u0000\u0082\u0083\u0005\u000e\u0000"+
		"\u0000\u0083\u008b\u0003$\u0012\u0000\u0084\u0085\u0005\u000f\u0000\u0000"+
		"\u0085\u008b\u0003$\u0012\u0000\u0086\u0087\u0005\u0010\u0000\u0000\u0087"+
		"\u008b\u0003$\u0012\u0000\u0088\u0089\u0005\u0011\u0000\u0000\u0089\u008b"+
		"\u0003$\u0012\u0000\u008a\u0082\u0001\u0000\u0000\u0000\u008a\u0084\u0001"+
		"\u0000\u0000\u0000\u008a\u0086\u0001\u0000\u0000\u0000\u008a\u0088\u0001"+
		"\u0000\u0000\u0000\u008b\u0019\u0001\u0000\u0000\u0000\u008c\u008f\u0003"+
		"\u001c\u000e\u0000\u008d\u008f\u0003\u001e\u000f\u0000\u008e\u008c\u0001"+
		"\u0000\u0000\u0000\u008e\u008d\u0001\u0000\u0000\u0000\u008f\u001b\u0001"+
		"\u0000\u0000\u0000\u0090\u0091\u0005\u0012\u0000\u0000\u0091\u0092\u0005"+
		"\u0013\u0000\u0000\u0092\u0093\u0003$\u0012\u0000\u0093\u0094\u0005\u0014"+
		"\u0000\u0000\u0094\u0098\u0005\u0015\u0000\u0000\u0095\u0097\u0003\u0002"+
		"\u0001\u0000\u0096\u0095\u0001\u0000\u0000\u0000\u0097\u009a\u0001\u0000"+
		"\u0000\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000"+
		"\u0000\u0000\u0099\u009b\u0001\u0000\u0000\u0000\u009a\u0098\u0001\u0000"+
		"\u0000\u0000\u009b\u009c\u0005\u0016\u0000\u0000\u009c\u001d\u0001\u0000"+
		"\u0000\u0000\u009d\u009e\u0005\u0017\u0000\u0000\u009e\u009f\u0005\u0013"+
		"\u0000\u0000\u009f\u00a0\u0003\n\u0005\u0000\u00a0\u00a1\u0005\u0018\u0000"+
		"\u0000\u00a1\u00a2\u0003$\u0012\u0000\u00a2\u00a3\u0005\u0018\u0000\u0000"+
		"\u00a3\u00a4\u0003\u0004\u0002\u0000\u00a4\u00a5\u0005\u0014\u0000\u0000"+
		"\u00a5\u00a9\u0005\u0015\u0000\u0000\u00a6\u00a8\u0003\u0002\u0001\u0000"+
		"\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a8\u00ab\u0001\u0000\u0000\u0000"+
		"\u00a9\u00a7\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000\u0000\u0000"+
		"\u00aa\u00ac\u0001\u0000\u0000\u0000\u00ab\u00a9\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0005\u0016\u0000\u0000\u00ad\u001f\u0001\u0000\u0000\u0000"+
		"\u00ae\u00af\u0005\u0019\u0000\u0000\u00af\u00b0\u0005\u0013\u0000\u0000"+
		"\u00b0\u00b1\u0003$\u0012\u0000\u00b1\u00b2\u0005\u0014\u0000\u0000\u00b2"+
		"\u00b6\u0005\u0015\u0000\u0000\u00b3\u00b5\u0003\u0002\u0001\u0000\u00b4"+
		"\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b8\u0001\u0000\u0000\u0000\u00b6"+
		"\u00b4\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7"+
		"\u00b9\u0001\u0000\u0000\u0000\u00b8\u00b6\u0001\u0000\u0000\u0000\u00b9"+
		"\u00c3\u0005\u0016\u0000\u0000\u00ba\u00bb\u0005\u001a\u0000\u0000\u00bb"+
		"\u00bf\u0005\u0015\u0000\u0000\u00bc\u00be\u0003\u0002\u0001\u0000\u00bd"+
		"\u00bc\u0001\u0000\u0000\u0000\u00be\u00c1\u0001\u0000\u0000\u0000\u00bf"+
		"\u00bd\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0"+
		"\u00c2\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000\u0000\u00c2"+
		"\u00c4\u0005\u0016\u0000\u0000\u00c3\u00ba\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c4\u0001\u0000\u0000\u0000\u00c4!\u0001\u0000\u0000\u0000\u00c5\u00c6"+
		"\u0005\u001b\u0000\u0000\u00c6\u00c7\u0005\u0013\u0000\u0000\u00c7\u00c8"+
		"\u0005(\u0000\u0000\u00c8\u00c9\u0005\u0014\u0000\u0000\u00c9#\u0001\u0000"+
		"\u0000\u0000\u00ca\u00cb\u0006\u0012\uffff\uffff\u0000\u00cb\u00cc\u0005"+
		"\u0013\u0000\u0000\u00cc\u00cd\u0003$\u0012\u0000\u00cd\u00ce\u0005\u0014"+
		"\u0000\u0000\u00ce\u00d3\u0001\u0000\u0000\u0000\u00cf\u00d3\u0005%\u0000"+
		"\u0000\u00d0\u00d3\u0005&\u0000\u0000\u00d1\u00d3\u0005\'\u0000\u0000"+
		"\u00d2\u00ca\u0001\u0000\u0000\u0000\u00d2\u00cf\u0001\u0000\u0000\u0000"+
		"\u00d2\u00d0\u0001\u0000\u0000\u0000\u00d2\u00d1\u0001\u0000\u0000\u0000"+
		"\u00d3\u00df\u0001\u0000\u0000\u0000\u00d4\u00d5\n\u0007\u0000\u0000\u00d5"+
		"\u00d6\u0007\u0000\u0000\u0000\u00d6\u00de\u0003$\u0012\b\u00d7\u00d8"+
		"\n\u0006\u0000\u0000\u00d8\u00d9\u0007\u0001\u0000\u0000\u00d9\u00de\u0003"+
		"$\u0012\u0007\u00da\u00db\n\u0005\u0000\u0000\u00db\u00dc\u0007\u0002"+
		"\u0000\u0000\u00dc\u00de\u0003$\u0012\u0006\u00dd\u00d4\u0001\u0000\u0000"+
		"\u0000\u00dd\u00d7\u0001\u0000\u0000\u0000\u00dd\u00da\u0001\u0000\u0000"+
		"\u0000\u00de\u00e1\u0001\u0000\u0000\u0000\u00df\u00dd\u0001\u0000\u0000"+
		"\u0000\u00df\u00e0\u0001\u0000\u0000\u0000\u00e0%\u0001\u0000\u0000\u0000"+
		"\u00e1\u00df\u0001\u0000\u0000\u0000\u0013)4BJ]dpy{\u008a\u008e\u0098"+
		"\u00a9\u00b6\u00bf\u00c3\u00d2\u00dd\u00df";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}