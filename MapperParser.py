# Generated from Mapper.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,308,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,5,4,87,8,4,10,4,12,4,90,9,4,3,4,92,8,4,1,4,1,4,1,4,5,
        4,97,8,4,10,4,12,4,100,9,4,1,4,1,4,1,5,1,5,1,5,3,5,107,8,5,1,5,1,
        5,1,6,1,6,1,6,5,6,114,8,6,10,6,12,6,117,9,6,1,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,131,8,9,10,9,12,9,134,9,9,1,10,1,
        10,1,10,1,10,1,10,3,10,141,8,10,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,13,1,13,3,13,155,8,13,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,4,16,170,8,16,11,16,12,
        16,171,1,17,1,17,1,17,1,17,1,17,3,17,179,8,17,1,18,1,18,3,18,183,
        8,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,5,19,192,8,19,10,19,12,19,
        195,9,19,1,19,1,19,1,19,1,19,4,19,201,8,19,11,19,12,19,202,3,19,
        205,8,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,3,21,220,8,21,1,22,1,22,3,22,224,8,22,1,23,1,23,1,23,1,
        23,1,23,1,23,5,23,232,8,23,10,23,12,23,235,9,23,1,23,1,23,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,5,24,249,8,24,10,24,12,
        24,252,9,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,262,8,25,
        10,25,12,25,265,9,25,1,25,1,25,1,25,1,25,5,25,271,8,25,10,25,12,
        25,274,9,25,1,25,3,25,277,8,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,3,27,292,8,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,5,27,303,8,27,10,27,12,27,306,9,27,1,27,
        0,1,54,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,0,4,1,0,1,3,2,0,12,12,33,33,1,0,34,35,1,
        0,36,41,320,0,59,1,0,0,0,2,73,1,0,0,0,4,75,1,0,0,0,6,78,1,0,0,0,
        8,80,1,0,0,0,10,103,1,0,0,0,12,110,1,0,0,0,14,118,1,0,0,0,16,122,
        1,0,0,0,18,127,1,0,0,0,20,140,1,0,0,0,22,142,1,0,0,0,24,147,1,0,
        0,0,26,154,1,0,0,0,28,156,1,0,0,0,30,160,1,0,0,0,32,164,1,0,0,0,
        34,178,1,0,0,0,36,182,1,0,0,0,38,204,1,0,0,0,40,206,1,0,0,0,42,210,
        1,0,0,0,44,223,1,0,0,0,46,225,1,0,0,0,48,238,1,0,0,0,50,255,1,0,
        0,0,52,278,1,0,0,0,54,291,1,0,0,0,56,58,3,2,1,0,57,56,1,0,0,0,58,
        61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,
        0,62,63,5,0,0,1,63,1,1,0,0,0,64,74,3,20,10,0,65,74,3,38,19,0,66,
        74,3,42,21,0,67,74,3,44,22,0,68,74,3,50,25,0,69,74,3,26,13,0,70,
        74,3,52,26,0,71,74,3,8,4,0,72,74,3,10,5,0,73,64,1,0,0,0,73,65,1,
        0,0,0,73,66,1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,
        70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,3,1,0,0,0,75,76,3,6,3,
        0,76,77,5,42,0,0,77,5,1,0,0,0,78,79,7,0,0,0,79,7,1,0,0,0,80,81,5,
        4,0,0,81,82,5,42,0,0,82,91,5,5,0,0,83,88,3,4,2,0,84,85,5,6,0,0,85,
        87,3,4,2,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,
        0,89,92,1,0,0,0,90,88,1,0,0,0,91,83,1,0,0,0,91,92,1,0,0,0,92,93,
        1,0,0,0,93,94,5,7,0,0,94,98,5,8,0,0,95,97,3,2,1,0,96,95,1,0,0,0,
        97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,
        1,0,0,0,101,102,5,9,0,0,102,9,1,0,0,0,103,104,5,42,0,0,104,106,5,
        5,0,0,105,107,3,12,6,0,106,105,1,0,0,0,106,107,1,0,0,0,107,108,1,
        0,0,0,108,109,5,7,0,0,109,11,1,0,0,0,110,115,3,54,27,0,111,112,5,
        6,0,0,112,114,3,54,27,0,113,111,1,0,0,0,114,117,1,0,0,0,115,113,
        1,0,0,0,115,116,1,0,0,0,116,13,1,0,0,0,117,115,1,0,0,0,118,119,5,
        42,0,0,119,120,5,10,0,0,120,121,3,54,27,0,121,15,1,0,0,0,122,123,
        5,2,0,0,123,124,5,42,0,0,124,125,5,11,0,0,125,126,3,18,9,0,126,17,
        1,0,0,0,127,132,5,42,0,0,128,129,5,12,0,0,129,131,5,42,0,0,130,128,
        1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,19,1,
        0,0,0,134,132,1,0,0,0,135,141,3,16,8,0,136,141,3,22,11,0,137,141,
        3,24,12,0,138,141,3,14,7,0,139,141,3,32,16,0,140,135,1,0,0,0,140,
        136,1,0,0,0,140,137,1,0,0,0,140,138,1,0,0,0,140,139,1,0,0,0,141,
        21,1,0,0,0,142,143,5,1,0,0,143,144,5,42,0,0,144,145,5,11,0,0,145,
        146,3,54,27,0,146,23,1,0,0,0,147,148,5,13,0,0,148,149,5,42,0,0,149,
        150,5,11,0,0,150,151,3,54,27,0,151,25,1,0,0,0,152,155,3,28,14,0,
        153,155,3,30,15,0,154,152,1,0,0,0,154,153,1,0,0,0,155,27,1,0,0,0,
        156,157,5,14,0,0,157,158,5,42,0,0,158,159,5,15,0,0,159,29,1,0,0,
        0,160,161,5,14,0,0,161,162,5,42,0,0,162,163,5,16,0,0,163,31,1,0,
        0,0,164,165,5,3,0,0,165,166,5,42,0,0,166,167,5,11,0,0,167,169,3,
        34,17,0,168,170,3,36,18,0,169,168,1,0,0,0,170,171,1,0,0,0,171,169,
        1,0,0,0,171,172,1,0,0,0,172,33,1,0,0,0,173,174,5,17,0,0,174,179,
        5,43,0,0,175,176,5,18,0,0,176,177,5,43,0,0,177,179,5,43,0,0,178,
        173,1,0,0,0,178,175,1,0,0,0,179,35,1,0,0,0,180,183,5,42,0,0,181,
        183,3,18,9,0,182,180,1,0,0,0,182,181,1,0,0,0,183,184,1,0,0,0,184,
        185,5,43,0,0,185,186,5,19,0,0,186,37,1,0,0,0,187,188,5,20,0,0,188,
        193,5,42,0,0,189,190,5,12,0,0,190,192,5,42,0,0,191,189,1,0,0,0,192,
        195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,205,1,0,0,0,195,
        193,1,0,0,0,196,197,5,20,0,0,197,198,5,21,0,0,198,200,5,43,0,0,199,
        201,3,40,20,0,200,199,1,0,0,0,201,202,1,0,0,0,202,200,1,0,0,0,202,
        203,1,0,0,0,203,205,1,0,0,0,204,187,1,0,0,0,204,196,1,0,0,0,205,
        39,1,0,0,0,206,207,5,43,0,0,207,208,5,19,0,0,208,209,5,42,0,0,209,
        41,1,0,0,0,210,219,5,22,0,0,211,212,5,23,0,0,212,220,3,54,27,0,213,
        214,5,24,0,0,214,220,3,54,27,0,215,216,5,25,0,0,216,220,3,54,27,
        0,217,218,5,26,0,0,218,220,3,54,27,0,219,211,1,0,0,0,219,213,1,0,
        0,0,219,215,1,0,0,0,219,217,1,0,0,0,220,43,1,0,0,0,221,224,3,46,
        23,0,222,224,3,48,24,0,223,221,1,0,0,0,223,222,1,0,0,0,224,45,1,
        0,0,0,225,226,5,27,0,0,226,227,5,5,0,0,227,228,3,54,27,0,228,229,
        5,7,0,0,229,233,5,8,0,0,230,232,3,2,1,0,231,230,1,0,0,0,232,235,
        1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,233,
        1,0,0,0,236,237,5,9,0,0,237,47,1,0,0,0,238,239,5,28,0,0,239,240,
        5,5,0,0,240,241,3,22,11,0,241,242,5,29,0,0,242,243,3,54,27,0,243,
        244,5,29,0,0,244,245,3,14,7,0,245,246,5,7,0,0,246,250,5,8,0,0,247,
        249,3,2,1,0,248,247,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,
        251,1,0,0,0,251,253,1,0,0,0,252,250,1,0,0,0,253,254,5,9,0,0,254,
        49,1,0,0,0,255,256,5,30,0,0,256,257,5,5,0,0,257,258,3,54,27,0,258,
        259,5,7,0,0,259,263,5,8,0,0,260,262,3,2,1,0,261,260,1,0,0,0,262,
        265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,266,1,0,0,0,265,
        263,1,0,0,0,266,276,5,9,0,0,267,268,5,31,0,0,268,272,5,8,0,0,269,
        271,3,2,1,0,270,269,1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,
        273,1,0,0,0,273,275,1,0,0,0,274,272,1,0,0,0,275,277,5,9,0,0,276,
        267,1,0,0,0,276,277,1,0,0,0,277,51,1,0,0,0,278,279,5,32,0,0,279,
        280,5,5,0,0,280,281,5,45,0,0,281,282,5,7,0,0,282,53,1,0,0,0,283,
        284,6,27,-1,0,284,285,5,5,0,0,285,286,3,54,27,0,286,287,5,7,0,0,
        287,292,1,0,0,0,288,292,5,42,0,0,289,292,5,43,0,0,290,292,5,44,0,
        0,291,283,1,0,0,0,291,288,1,0,0,0,291,289,1,0,0,0,291,290,1,0,0,
        0,292,304,1,0,0,0,293,294,10,7,0,0,294,295,7,1,0,0,295,303,3,54,
        27,8,296,297,10,6,0,0,297,298,7,2,0,0,298,303,3,54,27,7,299,300,
        10,5,0,0,300,301,7,3,0,0,301,303,3,54,27,6,302,293,1,0,0,0,302,296,
        1,0,0,0,302,299,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,
        1,0,0,0,305,55,1,0,0,0,306,304,1,0,0,0,26,59,73,88,91,98,106,115,
        132,140,154,171,178,182,193,202,204,219,223,233,250,263,272,276,
        291,302,304
    ]

class MapperParser ( Parser ):

    grammarFileName = "Mapper.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'tile'", "'blend'", "'function'", 
                     "'('", "','", "')'", "'{'", "'}'", "'+='", "'='", "'+'", 
                     "'bool'", "'road'", "'start'", "'end'", "'circle'", 
                     "'rectangle'", "'%'", "'draw'", "'radius'", "'pointer'", 
                     "'up'", "'down'", "'left'", "'right'", "'while'", "'for'", 
                     "';'", "'if'", "'else'", "'Yapping'", "'-'", "'*'", 
                     "'/'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "INT", "BOOL", 
                      "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_param = 2
    RULE_type = 3
    RULE_functionDecl = 4
    RULE_functionCall = 5
    RULE_exprList = 6
    RULE_increment = 7
    RULE_tileAssign = 8
    RULE_tileSum = 9
    RULE_assignment = 10
    RULE_numberAssign = 11
    RULE_boolAssign = 12
    RULE_roadPlacement = 13
    RULE_roadStart = 14
    RULE_roadEnd = 15
    RULE_blendAssign = 16
    RULE_figure = 17
    RULE_blendOption = 18
    RULE_draw = 19
    RULE_percentagePair = 20
    RULE_move = 21
    RULE_loop = 22
    RULE_whileLoop = 23
    RULE_forLoop = 24
    RULE_conditional = 25
    RULE_errorHandling = 26
    RULE_expr = 27

    ruleNames =  [ "program", "statement", "param", "type", "functionDecl", 
                   "functionCall", "exprList", "increment", "tileAssign", 
                   "tileSum", "assignment", "numberAssign", "boolAssign", 
                   "roadPlacement", "roadStart", "roadEnd", "blendAssign", 
                   "figure", "blendOption", "draw", "percentagePair", "move", 
                   "loop", "whileLoop", "forLoop", "conditional", "errorHandling", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    IDENTIFIER=42
    INT=43
    BOOL=44
    STRING=45
    WS=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MapperParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.StatementContext)
            else:
                return self.getTypedRuleContext(MapperParser.StatementContext,i)


        def getRuleIndex(self):
            return MapperParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MapperParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 56
                self.statement()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(MapperParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MapperParser.AssignmentContext,0)


        def draw(self):
            return self.getTypedRuleContext(MapperParser.DrawContext,0)


        def move(self):
            return self.getTypedRuleContext(MapperParser.MoveContext,0)


        def loop(self):
            return self.getTypedRuleContext(MapperParser.LoopContext,0)


        def conditional(self):
            return self.getTypedRuleContext(MapperParser.ConditionalContext,0)


        def roadPlacement(self):
            return self.getTypedRuleContext(MapperParser.RoadPlacementContext,0)


        def errorHandling(self):
            return self.getTypedRuleContext(MapperParser.ErrorHandlingContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(MapperParser.FunctionDeclContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MapperParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MapperParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.draw()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.move()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.conditional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.roadPlacement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.errorHandling()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.functionDecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 72
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MapperParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MapperParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MapperParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.type_()
            self.state = 76
            self.match(MapperParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MapperParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MapperParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.ParamContext)
            else:
                return self.getTypedRuleContext(MapperParser.ParamContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.StatementContext)
            else:
                return self.getTypedRuleContext(MapperParser.StatementContext,i)


        def getRuleIndex(self):
            return MapperParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = MapperParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(MapperParser.T__3)
            self.state = 81
            self.match(MapperParser.IDENTIFIER)
            self.state = 82
            self.match(MapperParser.T__4)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 83
                self.param()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 84
                    self.match(MapperParser.T__5)
                    self.state = 85
                    self.param()
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 93
            self.match(MapperParser.T__6)
            self.state = 94
            self.match(MapperParser.T__7)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 95
                self.statement()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(MapperParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def exprList(self):
            return self.getTypedRuleContext(MapperParser.ExprListContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MapperParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(MapperParser.IDENTIFIER)
            self.state = 104
            self.match(MapperParser.T__4)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30786325577760) != 0):
                self.state = 105
                self.exprList()


            self.state = 108
            self.match(MapperParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapperParser.ExprContext,i)


        def getRuleIndex(self):
            return MapperParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = MapperParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.expr(0)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 111
                self.match(MapperParser.T__5)
                self.state = 112
                self.expr(0)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_increment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrement" ):
                listener.enterIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrement" ):
                listener.exitIncrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrement" ):
                return visitor.visitIncrement(self)
            else:
                return visitor.visitChildren(self)




    def increment(self):

        localctx = MapperParser.IncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_increment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MapperParser.IDENTIFIER)
            self.state = 119
            self.match(MapperParser.T__9)
            self.state = 120
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TileAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def tileSum(self):
            return self.getTypedRuleContext(MapperParser.TileSumContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_tileAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTileAssign" ):
                listener.enterTileAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTileAssign" ):
                listener.exitTileAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTileAssign" ):
                return visitor.visitTileAssign(self)
            else:
                return visitor.visitChildren(self)




    def tileAssign(self):

        localctx = MapperParser.TileAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tileAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(MapperParser.T__1)
            self.state = 123
            self.match(MapperParser.IDENTIFIER)
            self.state = 124
            self.match(MapperParser.T__10)
            self.state = 125
            self.tileSum()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TileSumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MapperParser.IDENTIFIER)
            else:
                return self.getToken(MapperParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return MapperParser.RULE_tileSum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTileSum" ):
                listener.enterTileSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTileSum" ):
                listener.exitTileSum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTileSum" ):
                return visitor.visitTileSum(self)
            else:
                return visitor.visitChildren(self)




    def tileSum(self):

        localctx = MapperParser.TileSumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tileSum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MapperParser.IDENTIFIER)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 128
                self.match(MapperParser.T__11)
                self.state = 129
                self.match(MapperParser.IDENTIFIER)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tileAssign(self):
            return self.getTypedRuleContext(MapperParser.TileAssignContext,0)


        def numberAssign(self):
            return self.getTypedRuleContext(MapperParser.NumberAssignContext,0)


        def boolAssign(self):
            return self.getTypedRuleContext(MapperParser.BoolAssignContext,0)


        def increment(self):
            return self.getTypedRuleContext(MapperParser.IncrementContext,0)


        def blendAssign(self):
            return self.getTypedRuleContext(MapperParser.BlendAssignContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MapperParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.tileAssign()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.numberAssign()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.boolAssign()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.increment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.blendAssign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_numberAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAssign" ):
                listener.enterNumberAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAssign" ):
                listener.exitNumberAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAssign" ):
                return visitor.visitNumberAssign(self)
            else:
                return visitor.visitChildren(self)




    def numberAssign(self):

        localctx = MapperParser.NumberAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_numberAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MapperParser.T__0)
            self.state = 143
            self.match(MapperParser.IDENTIFIER)
            self.state = 144
            self.match(MapperParser.T__10)
            self.state = 145
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_boolAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolAssign" ):
                listener.enterBoolAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolAssign" ):
                listener.exitBoolAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolAssign" ):
                return visitor.visitBoolAssign(self)
            else:
                return visitor.visitChildren(self)




    def boolAssign(self):

        localctx = MapperParser.BoolAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_boolAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MapperParser.T__12)
            self.state = 148
            self.match(MapperParser.IDENTIFIER)
            self.state = 149
            self.match(MapperParser.T__10)
            self.state = 150
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoadPlacementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def roadStart(self):
            return self.getTypedRuleContext(MapperParser.RoadStartContext,0)


        def roadEnd(self):
            return self.getTypedRuleContext(MapperParser.RoadEndContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_roadPlacement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoadPlacement" ):
                listener.enterRoadPlacement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoadPlacement" ):
                listener.exitRoadPlacement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoadPlacement" ):
                return visitor.visitRoadPlacement(self)
            else:
                return visitor.visitChildren(self)




    def roadPlacement(self):

        localctx = MapperParser.RoadPlacementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_roadPlacement)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.roadStart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.roadEnd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoadStartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MapperParser.RULE_roadStart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoadStart" ):
                listener.enterRoadStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoadStart" ):
                listener.exitRoadStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoadStart" ):
                return visitor.visitRoadStart(self)
            else:
                return visitor.visitChildren(self)




    def roadStart(self):

        localctx = MapperParser.RoadStartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_roadStart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MapperParser.T__13)
            self.state = 157
            self.match(MapperParser.IDENTIFIER)
            self.state = 158
            self.match(MapperParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoadEndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MapperParser.RULE_roadEnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoadEnd" ):
                listener.enterRoadEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoadEnd" ):
                listener.exitRoadEnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoadEnd" ):
                return visitor.visitRoadEnd(self)
            else:
                return visitor.visitChildren(self)




    def roadEnd(self):

        localctx = MapperParser.RoadEndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_roadEnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MapperParser.T__13)
            self.state = 161
            self.match(MapperParser.IDENTIFIER)
            self.state = 162
            self.match(MapperParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlendAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def figure(self):
            return self.getTypedRuleContext(MapperParser.FigureContext,0)


        def blendOption(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.BlendOptionContext)
            else:
                return self.getTypedRuleContext(MapperParser.BlendOptionContext,i)


        def getRuleIndex(self):
            return MapperParser.RULE_blendAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlendAssign" ):
                listener.enterBlendAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlendAssign" ):
                listener.exitBlendAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlendAssign" ):
                return visitor.visitBlendAssign(self)
            else:
                return visitor.visitChildren(self)




    def blendAssign(self):

        localctx = MapperParser.BlendAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_blendAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MapperParser.T__2)
            self.state = 165
            self.match(MapperParser.IDENTIFIER)
            self.state = 166
            self.match(MapperParser.T__10)
            self.state = 167
            self.figure()
            self.state = 169 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 168
                    self.blendOption()

                else:
                    raise NoViableAltException(self)
                self.state = 171 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FigureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MapperParser.INT)
            else:
                return self.getToken(MapperParser.INT, i)

        def getRuleIndex(self):
            return MapperParser.RULE_figure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFigure" ):
                listener.enterFigure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFigure" ):
                listener.exitFigure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFigure" ):
                return visitor.visitFigure(self)
            else:
                return visitor.visitChildren(self)




    def figure(self):

        localctx = MapperParser.FigureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_figure)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(MapperParser.T__16)
                self.state = 174
                self.match(MapperParser.INT)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(MapperParser.T__17)
                self.state = 176
                self.match(MapperParser.INT)
                self.state = 177
                self.match(MapperParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlendOptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MapperParser.INT, 0)

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def tileSum(self):
            return self.getTypedRuleContext(MapperParser.TileSumContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_blendOption

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlendOption" ):
                listener.enterBlendOption(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlendOption" ):
                listener.exitBlendOption(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlendOption" ):
                return visitor.visitBlendOption(self)
            else:
                return visitor.visitChildren(self)




    def blendOption(self):

        localctx = MapperParser.BlendOptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_blendOption)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 180
                self.match(MapperParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 181
                self.tileSum()
                pass


            self.state = 184
            self.match(MapperParser.INT)
            self.state = 185
            self.match(MapperParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DrawContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MapperParser.IDENTIFIER)
            else:
                return self.getToken(MapperParser.IDENTIFIER, i)

        def INT(self):
            return self.getToken(MapperParser.INT, 0)

        def percentagePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.PercentagePairContext)
            else:
                return self.getTypedRuleContext(MapperParser.PercentagePairContext,i)


        def getRuleIndex(self):
            return MapperParser.RULE_draw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDraw" ):
                listener.enterDraw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDraw" ):
                listener.exitDraw(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDraw" ):
                return visitor.visitDraw(self)
            else:
                return visitor.visitChildren(self)




    def draw(self):

        localctx = MapperParser.DrawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_draw)
        self._la = 0 # Token type
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(MapperParser.T__19)
                self.state = 188
                self.match(MapperParser.IDENTIFIER)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 189
                    self.match(MapperParser.T__11)
                    self.state = 190
                    self.match(MapperParser.IDENTIFIER)
                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(MapperParser.T__19)
                self.state = 197
                self.match(MapperParser.T__20)
                self.state = 198
                self.match(MapperParser.INT)
                self.state = 200 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 199
                    self.percentagePair()
                    self.state = 202 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==43):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PercentagePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MapperParser.INT, 0)

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MapperParser.RULE_percentagePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPercentagePair" ):
                listener.enterPercentagePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPercentagePair" ):
                listener.exitPercentagePair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPercentagePair" ):
                return visitor.visitPercentagePair(self)
            else:
                return visitor.visitChildren(self)




    def percentagePair(self):

        localctx = MapperParser.PercentagePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_percentagePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MapperParser.INT)
            self.state = 207
            self.match(MapperParser.T__18)
            self.state = 208
            self.match(MapperParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_move

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove" ):
                listener.enterMove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove" ):
                listener.exitMove(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMove" ):
                return visitor.visitMove(self)
            else:
                return visitor.visitChildren(self)




    def move(self):

        localctx = MapperParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_move)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(MapperParser.T__21)
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 211
                self.match(MapperParser.T__22)
                self.state = 212
                self.expr(0)
                pass
            elif token in [24]:
                self.state = 213
                self.match(MapperParser.T__23)
                self.state = 214
                self.expr(0)
                pass
            elif token in [25]:
                self.state = 215
                self.match(MapperParser.T__24)
                self.state = 216
                self.expr(0)
                pass
            elif token in [26]:
                self.state = 217
                self.match(MapperParser.T__25)
                self.state = 218
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whileLoop(self):
            return self.getTypedRuleContext(MapperParser.WhileLoopContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(MapperParser.ForLoopContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = MapperParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_loop)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.whileLoop()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.forLoop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.StatementContext)
            else:
                return self.getTypedRuleContext(MapperParser.StatementContext,i)


        def getRuleIndex(self):
            return MapperParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = MapperParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MapperParser.T__26)
            self.state = 226
            self.match(MapperParser.T__4)
            self.state = 227
            self.expr(0)
            self.state = 228
            self.match(MapperParser.T__6)
            self.state = 229
            self.match(MapperParser.T__7)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 230
                self.statement()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 236
            self.match(MapperParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numberAssign(self):
            return self.getTypedRuleContext(MapperParser.NumberAssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def increment(self):
            return self.getTypedRuleContext(MapperParser.IncrementContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.StatementContext)
            else:
                return self.getTypedRuleContext(MapperParser.StatementContext,i)


        def getRuleIndex(self):
            return MapperParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = MapperParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MapperParser.T__27)
            self.state = 239
            self.match(MapperParser.T__4)
            self.state = 240
            self.numberAssign()
            self.state = 241
            self.match(MapperParser.T__28)
            self.state = 242
            self.expr(0)
            self.state = 243
            self.match(MapperParser.T__28)
            self.state = 244
            self.increment()
            self.state = 245
            self.match(MapperParser.T__6)
            self.state = 246
            self.match(MapperParser.T__7)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 247
                self.statement()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
            self.match(MapperParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.StatementContext)
            else:
                return self.getTypedRuleContext(MapperParser.StatementContext,i)


        def getRuleIndex(self):
            return MapperParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = MapperParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(MapperParser.T__29)
            self.state = 256
            self.match(MapperParser.T__4)
            self.state = 257
            self.expr(0)
            self.state = 258
            self.match(MapperParser.T__6)
            self.state = 259
            self.match(MapperParser.T__7)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 260
                self.statement()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
            self.match(MapperParser.T__8)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 267
                self.match(MapperParser.T__30)
                self.state = 268
                self.match(MapperParser.T__7)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                    self.state = 269
                    self.statement()
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 275
                self.match(MapperParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ErrorHandlingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MapperParser.STRING, 0)

        def getRuleIndex(self):
            return MapperParser.RULE_errorHandling

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErrorHandling" ):
                listener.enterErrorHandling(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErrorHandling" ):
                listener.exitErrorHandling(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitErrorHandling" ):
                return visitor.visitErrorHandling(self)
            else:
                return visitor.visitChildren(self)




    def errorHandling(self):

        localctx = MapperParser.ErrorHandlingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_errorHandling)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MapperParser.T__31)
            self.state = 279
            self.match(MapperParser.T__4)
            self.state = 280
            self.match(MapperParser.STRING)
            self.state = 281
            self.match(MapperParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapperParser.ExprContext,i)


        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def INT(self):
            return self.getToken(MapperParser.INT, 0)

        def BOOL(self):
            return self.getToken(MapperParser.BOOL, 0)

        def getRuleIndex(self):
            return MapperParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MapperParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 284
                self.match(MapperParser.T__4)
                self.state = 285
                self.expr(0)
                self.state = 286
                self.match(MapperParser.T__6)
                pass
            elif token in [42]:
                self.state = 288
                self.match(MapperParser.IDENTIFIER)
                pass
            elif token in [43]:
                self.state = 289
                self.match(MapperParser.INT)
                pass
            elif token in [44]:
                self.state = 290
                self.match(MapperParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 302
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MapperParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 293
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 294
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==33):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 295
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = MapperParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 296
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 297
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 298
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = MapperParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 299
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 300
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4329327034368) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 301
                        self.expr(6)
                        pass

             
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




