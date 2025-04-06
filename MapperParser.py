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
        4,1,49,323,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,2,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,90,8,4,10,4,12,4,93,9,4,3,4,95,8,
        4,1,4,1,4,1,4,5,4,100,8,4,10,4,12,4,103,9,4,1,4,1,4,1,5,1,5,1,5,
        3,5,110,8,5,1,5,1,5,1,6,1,6,1,6,5,6,117,8,6,10,6,12,6,120,9,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,132,8,7,1,8,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,5,9,142,8,9,10,9,12,9,145,9,9,1,10,1,10,1,10,1,
        10,1,10,1,10,3,10,153,8,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,3,14,171,8,14,1,15,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,4,17,186,
        8,17,11,17,12,17,187,1,18,1,18,1,18,1,18,1,18,3,18,195,8,18,1,19,
        1,19,3,19,199,8,19,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,
        1,21,5,21,211,8,21,10,21,12,21,214,9,21,1,21,1,21,1,21,1,21,4,21,
        220,8,21,11,21,12,21,221,3,21,224,8,21,1,22,1,22,1,22,1,22,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,239,8,23,1,24,1,24,
        3,24,243,8,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,251,8,25,10,25,
        12,25,254,9,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,5,26,268,8,26,10,26,12,26,271,9,26,1,26,1,26,1,27,1,27,
        1,27,1,27,1,27,1,27,5,27,281,8,27,10,27,12,27,284,9,27,1,27,1,27,
        1,27,1,27,5,27,290,8,27,10,27,12,27,293,9,27,1,27,3,27,296,8,27,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,306,8,28,1,28,1,28,
        1,28,1,28,1,28,1,28,5,28,314,8,28,10,28,12,28,317,9,28,1,29,1,29,
        1,29,1,29,1,29,0,1,56,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,4,1,0,1,3,1,0,36,
        37,2,0,15,15,38,38,1,0,39,44,335,0,63,1,0,0,0,2,76,1,0,0,0,4,78,
        1,0,0,0,6,81,1,0,0,0,8,83,1,0,0,0,10,106,1,0,0,0,12,113,1,0,0,0,
        14,131,1,0,0,0,16,133,1,0,0,0,18,138,1,0,0,0,20,152,1,0,0,0,22,154,
        1,0,0,0,24,159,1,0,0,0,26,163,1,0,0,0,28,170,1,0,0,0,30,172,1,0,
        0,0,32,176,1,0,0,0,34,180,1,0,0,0,36,194,1,0,0,0,38,198,1,0,0,0,
        40,203,1,0,0,0,42,223,1,0,0,0,44,225,1,0,0,0,46,229,1,0,0,0,48,242,
        1,0,0,0,50,244,1,0,0,0,52,257,1,0,0,0,54,274,1,0,0,0,56,305,1,0,
        0,0,58,318,1,0,0,0,60,62,3,2,1,0,61,60,1,0,0,0,62,65,1,0,0,0,63,
        61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,0,0,
        1,67,1,1,0,0,0,68,77,3,20,10,0,69,77,3,42,21,0,70,77,3,46,23,0,71,
        77,3,48,24,0,72,77,3,54,27,0,73,77,3,28,14,0,74,77,3,8,4,0,75,77,
        3,10,5,0,76,68,1,0,0,0,76,69,1,0,0,0,76,70,1,0,0,0,76,71,1,0,0,0,
        76,72,1,0,0,0,76,73,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,0,77,3,1,0,
        0,0,78,79,3,6,3,0,79,80,5,45,0,0,80,5,1,0,0,0,81,82,7,0,0,0,82,7,
        1,0,0,0,83,84,5,4,0,0,84,85,5,45,0,0,85,94,5,5,0,0,86,91,3,4,2,0,
        87,88,5,6,0,0,88,90,3,4,2,0,89,87,1,0,0,0,90,93,1,0,0,0,91,89,1,
        0,0,0,91,92,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,94,86,1,0,0,0,94,
        95,1,0,0,0,95,96,1,0,0,0,96,97,5,7,0,0,97,101,5,8,0,0,98,100,3,2,
        1,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,
        102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,9,0,0,105,9,1,0,0,0,106,
        107,5,45,0,0,107,109,5,5,0,0,108,110,3,12,6,0,109,108,1,0,0,0,109,
        110,1,0,0,0,110,111,1,0,0,0,111,112,5,7,0,0,112,11,1,0,0,0,113,118,
        3,56,28,0,114,115,5,6,0,0,115,117,3,56,28,0,116,114,1,0,0,0,117,
        120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,13,1,0,0,0,120,118,
        1,0,0,0,121,122,5,45,0,0,122,132,5,10,0,0,123,124,5,45,0,0,124,132,
        5,11,0,0,125,126,5,45,0,0,126,127,5,12,0,0,127,132,3,56,28,0,128,
        129,5,45,0,0,129,130,5,13,0,0,130,132,3,56,28,0,131,121,1,0,0,0,
        131,123,1,0,0,0,131,125,1,0,0,0,131,128,1,0,0,0,132,15,1,0,0,0,133,
        134,5,2,0,0,134,135,5,45,0,0,135,136,5,14,0,0,136,137,3,18,9,0,137,
        17,1,0,0,0,138,143,5,45,0,0,139,140,5,15,0,0,140,142,5,45,0,0,141,
        139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,
        19,1,0,0,0,145,143,1,0,0,0,146,153,3,16,8,0,147,153,3,22,11,0,148,
        153,3,26,13,0,149,153,3,14,7,0,150,153,3,34,17,0,151,153,3,24,12,
        0,152,146,1,0,0,0,152,147,1,0,0,0,152,148,1,0,0,0,152,149,1,0,0,
        0,152,150,1,0,0,0,152,151,1,0,0,0,153,21,1,0,0,0,154,155,5,1,0,0,
        155,156,5,45,0,0,156,157,5,14,0,0,157,158,3,56,28,0,158,23,1,0,0,
        0,159,160,5,45,0,0,160,161,5,14,0,0,161,162,3,56,28,0,162,25,1,0,
        0,0,163,164,5,16,0,0,164,165,5,45,0,0,165,166,5,14,0,0,166,167,3,
        56,28,0,167,27,1,0,0,0,168,171,3,30,15,0,169,171,3,32,16,0,170,168,
        1,0,0,0,170,169,1,0,0,0,171,29,1,0,0,0,172,173,5,17,0,0,173,174,
        5,45,0,0,174,175,5,18,0,0,175,31,1,0,0,0,176,177,5,17,0,0,177,178,
        5,45,0,0,178,179,5,19,0,0,179,33,1,0,0,0,180,181,5,3,0,0,181,182,
        5,45,0,0,182,183,5,14,0,0,183,185,3,36,18,0,184,186,3,38,19,0,185,
        184,1,0,0,0,186,187,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,
        35,1,0,0,0,189,190,5,20,0,0,190,195,5,46,0,0,191,192,5,21,0,0,192,
        193,5,46,0,0,193,195,5,46,0,0,194,189,1,0,0,0,194,191,1,0,0,0,195,
        37,1,0,0,0,196,199,5,45,0,0,197,199,3,18,9,0,198,196,1,0,0,0,198,
        197,1,0,0,0,199,200,1,0,0,0,200,201,5,46,0,0,201,202,5,22,0,0,202,
        39,1,0,0,0,203,204,5,23,0,0,204,205,5,45,0,0,205,41,1,0,0,0,206,
        207,5,24,0,0,207,212,5,45,0,0,208,209,5,15,0,0,209,211,5,45,0,0,
        210,208,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,
        213,224,1,0,0,0,214,212,1,0,0,0,215,216,5,24,0,0,216,217,5,25,0,
        0,217,219,5,46,0,0,218,220,3,44,22,0,219,218,1,0,0,0,220,221,1,0,
        0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,224,1,0,0,0,223,206,1,0,
        0,0,223,215,1,0,0,0,224,43,1,0,0,0,225,226,5,46,0,0,226,227,5,22,
        0,0,227,228,5,45,0,0,228,45,1,0,0,0,229,238,5,26,0,0,230,231,5,27,
        0,0,231,239,3,56,28,0,232,233,5,28,0,0,233,239,3,56,28,0,234,235,
        5,29,0,0,235,239,3,56,28,0,236,237,5,30,0,0,237,239,3,56,28,0,238,
        230,1,0,0,0,238,232,1,0,0,0,238,234,1,0,0,0,238,236,1,0,0,0,239,
        47,1,0,0,0,240,243,3,50,25,0,241,243,3,52,26,0,242,240,1,0,0,0,242,
        241,1,0,0,0,243,49,1,0,0,0,244,245,5,31,0,0,245,246,5,5,0,0,246,
        247,3,58,29,0,247,248,5,7,0,0,248,252,5,8,0,0,249,251,3,2,1,0,250,
        249,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,
        255,1,0,0,0,254,252,1,0,0,0,255,256,5,9,0,0,256,51,1,0,0,0,257,258,
        5,32,0,0,258,259,5,5,0,0,259,260,3,22,11,0,260,261,5,33,0,0,261,
        262,3,56,28,0,262,263,5,33,0,0,263,264,3,14,7,0,264,265,5,7,0,0,
        265,269,5,8,0,0,266,268,3,2,1,0,267,266,1,0,0,0,268,271,1,0,0,0,
        269,267,1,0,0,0,269,270,1,0,0,0,270,272,1,0,0,0,271,269,1,0,0,0,
        272,273,5,9,0,0,273,53,1,0,0,0,274,275,5,34,0,0,275,276,5,5,0,0,
        276,277,3,58,29,0,277,278,5,7,0,0,278,282,5,8,0,0,279,281,3,2,1,
        0,280,279,1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,
        0,283,285,1,0,0,0,284,282,1,0,0,0,285,295,5,9,0,0,286,287,5,35,0,
        0,287,291,5,8,0,0,288,290,3,2,1,0,289,288,1,0,0,0,290,293,1,0,0,
        0,291,289,1,0,0,0,291,292,1,0,0,0,292,294,1,0,0,0,293,291,1,0,0,
        0,294,296,5,9,0,0,295,286,1,0,0,0,295,296,1,0,0,0,296,55,1,0,0,0,
        297,298,6,28,-1,0,298,299,5,5,0,0,299,300,3,56,28,0,300,301,5,7,
        0,0,301,306,1,0,0,0,302,306,5,45,0,0,303,306,5,46,0,0,304,306,5,
        47,0,0,305,297,1,0,0,0,305,302,1,0,0,0,305,303,1,0,0,0,305,304,1,
        0,0,0,306,315,1,0,0,0,307,308,10,6,0,0,308,309,7,1,0,0,309,314,3,
        56,28,7,310,311,10,5,0,0,311,312,7,2,0,0,312,314,3,56,28,6,313,307,
        1,0,0,0,313,310,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,
        1,0,0,0,316,57,1,0,0,0,317,315,1,0,0,0,318,319,3,56,28,0,319,320,
        7,3,0,0,320,321,3,56,28,0,321,59,1,0,0,0,27,63,76,91,94,101,109,
        118,131,143,152,170,187,194,198,212,221,223,238,242,252,269,282,
        291,295,305,313,315
    ]

class MapperParser ( Parser ):

    grammarFileName = "Mapper.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'tile'", "'blend'", "'function'", 
                     "'('", "','", "')'", "'{'", "'}'", "'++'", "'--'", 
                     "'+='", "'-='", "'='", "'+'", "'bool'", "'road'", "'start'", 
                     "'end'", "'circle'", "'rectangle'", "'%'", "'drawRoad'", 
                     "'draw'", "'radius'", "'pointer'", "'up'", "'down'", 
                     "'left'", "'right'", "'while'", "'for'", "';'", "'if'", 
                     "'else'", "'*'", "'/'", "'-'", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='" ]

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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "INT", "BOOL", "STRING", 
                      "WS" ]

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
    RULE_varAssign = 12
    RULE_boolAssign = 13
    RULE_roadPlacement = 14
    RULE_roadStart = 15
    RULE_roadEnd = 16
    RULE_blendAssign = 17
    RULE_figure = 18
    RULE_blendOption = 19
    RULE_drawRoad = 20
    RULE_draw = 21
    RULE_percentagePair = 22
    RULE_move = 23
    RULE_loop = 24
    RULE_whileLoop = 25
    RULE_forLoop = 26
    RULE_conditional = 27
    RULE_expr = 28
    RULE_exprComp = 29

    ruleNames =  [ "program", "statement", "param", "type", "functionDecl", 
                   "functionCall", "exprList", "increment", "tileAssign", 
                   "tileSum", "assignment", "numberAssign", "varAssign", 
                   "boolAssign", "roadPlacement", "roadStart", "roadEnd", 
                   "blendAssign", "figure", "blendOption", "drawRoad", "draw", 
                   "percentagePair", "move", "loop", "whileLoop", "forLoop", 
                   "conditional", "expr", "exprComp" ]

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
    T__41=42
    T__42=43
    T__43=44
    IDENTIFIER=45
    INT=46
    BOOL=47
    STRING=48
    WS=49

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
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35208078491678) != 0):
                self.state = 60
                self.statement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.draw()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.move()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.conditional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.roadPlacement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.functionDecl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
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
            self.state = 78
            self.type_()
            self.state = 79
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
            self.state = 81
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
            self.state = 83
            self.match(MapperParser.T__3)
            self.state = 84
            self.match(MapperParser.IDENTIFIER)
            self.state = 85
            self.match(MapperParser.T__4)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 86
                self.param()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 87
                    self.match(MapperParser.T__5)
                    self.state = 88
                    self.param()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 96
            self.match(MapperParser.T__6)
            self.state = 97
            self.match(MapperParser.T__7)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35208078491678) != 0):
                self.state = 98
                self.statement()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
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
            self.state = 106
            self.match(MapperParser.IDENTIFIER)
            self.state = 107
            self.match(MapperParser.T__4)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 246290604621856) != 0):
                self.state = 108
                self.exprList()


            self.state = 111
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
            self.state = 113
            self.expr(0)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 114
                self.match(MapperParser.T__5)
                self.state = 115
                self.expr(0)
                self.state = 120
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(MapperParser.IDENTIFIER)
                self.state = 122
                self.match(MapperParser.T__9)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(MapperParser.IDENTIFIER)
                self.state = 124
                self.match(MapperParser.T__10)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.match(MapperParser.IDENTIFIER)
                self.state = 126
                self.match(MapperParser.T__11)
                self.state = 127
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.match(MapperParser.IDENTIFIER)
                self.state = 129
                self.match(MapperParser.T__12)
                self.state = 130
                self.expr(0)
                pass


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
            self.state = 133
            self.match(MapperParser.T__1)
            self.state = 134
            self.match(MapperParser.IDENTIFIER)
            self.state = 135
            self.match(MapperParser.T__13)
            self.state = 136
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
            self.state = 138
            self.match(MapperParser.IDENTIFIER)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 139
                self.match(MapperParser.T__14)
                self.state = 140
                self.match(MapperParser.IDENTIFIER)
                self.state = 145
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


        def varAssign(self):
            return self.getTypedRuleContext(MapperParser.VarAssignContext,0)


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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.tileAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.numberAssign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.boolAssign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.increment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.blendAssign()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
                self.varAssign()
                pass


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
            self.state = 154
            self.match(MapperParser.T__0)
            self.state = 155
            self.match(MapperParser.IDENTIFIER)
            self.state = 156
            self.match(MapperParser.T__13)
            self.state = 157
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def getRuleIndex(self):
            return MapperParser.RULE_varAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarAssign" ):
                listener.enterVarAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarAssign" ):
                listener.exitVarAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarAssign" ):
                return visitor.visitVarAssign(self)
            else:
                return visitor.visitChildren(self)




    def varAssign(self):

        localctx = MapperParser.VarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(MapperParser.IDENTIFIER)
            self.state = 160
            self.match(MapperParser.T__13)
            self.state = 161
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
        self.enterRule(localctx, 26, self.RULE_boolAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MapperParser.T__15)
            self.state = 164
            self.match(MapperParser.IDENTIFIER)
            self.state = 165
            self.match(MapperParser.T__13)
            self.state = 166
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
        self.enterRule(localctx, 28, self.RULE_roadPlacement)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.roadStart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
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
        self.enterRule(localctx, 30, self.RULE_roadStart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MapperParser.T__16)
            self.state = 173
            self.match(MapperParser.IDENTIFIER)
            self.state = 174
            self.match(MapperParser.T__17)
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
        self.enterRule(localctx, 32, self.RULE_roadEnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MapperParser.T__16)
            self.state = 177
            self.match(MapperParser.IDENTIFIER)
            self.state = 178
            self.match(MapperParser.T__18)
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
        self.enterRule(localctx, 34, self.RULE_blendAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MapperParser.T__2)
            self.state = 181
            self.match(MapperParser.IDENTIFIER)
            self.state = 182
            self.match(MapperParser.T__13)
            self.state = 183
            self.figure()
            self.state = 185 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 184
                    self.blendOption()

                else:
                    raise NoViableAltException(self)
                self.state = 187 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_figure)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(MapperParser.T__19)
                self.state = 190
                self.match(MapperParser.INT)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(MapperParser.T__20)
                self.state = 192
                self.match(MapperParser.INT)
                self.state = 193
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
        self.enterRule(localctx, 38, self.RULE_blendOption)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 196
                self.match(MapperParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 197
                self.tileSum()
                pass


            self.state = 200
            self.match(MapperParser.INT)
            self.state = 201
            self.match(MapperParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DrawRoadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MapperParser.RULE_drawRoad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawRoad" ):
                listener.enterDrawRoad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawRoad" ):
                listener.exitDrawRoad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawRoad" ):
                return visitor.visitDrawRoad(self)
            else:
                return visitor.visitChildren(self)




    def drawRoad(self):

        localctx = MapperParser.DrawRoadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_drawRoad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(MapperParser.T__22)
            self.state = 204
            self.match(MapperParser.IDENTIFIER)
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
        self.enterRule(localctx, 42, self.RULE_draw)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(MapperParser.T__23)
                self.state = 207
                self.match(MapperParser.IDENTIFIER)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 208
                    self.match(MapperParser.T__14)
                    self.state = 209
                    self.match(MapperParser.IDENTIFIER)
                    self.state = 214
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(MapperParser.T__23)
                self.state = 216
                self.match(MapperParser.T__24)
                self.state = 217
                self.match(MapperParser.INT)
                self.state = 219 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 218
                    self.percentagePair()
                    self.state = 221 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==46):
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
        self.enterRule(localctx, 44, self.RULE_percentagePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MapperParser.INT)
            self.state = 226
            self.match(MapperParser.T__21)
            self.state = 227
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
        self.enterRule(localctx, 46, self.RULE_move)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MapperParser.T__25)
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 230
                self.match(MapperParser.T__26)
                self.state = 231
                self.expr(0)
                pass
            elif token in [28]:
                self.state = 232
                self.match(MapperParser.T__27)
                self.state = 233
                self.expr(0)
                pass
            elif token in [29]:
                self.state = 234
                self.match(MapperParser.T__28)
                self.state = 235
                self.expr(0)
                pass
            elif token in [30]:
                self.state = 236
                self.match(MapperParser.T__29)
                self.state = 237
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
        self.enterRule(localctx, 48, self.RULE_loop)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.whileLoop()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
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

        def exprComp(self):
            return self.getTypedRuleContext(MapperParser.ExprCompContext,0)


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
        self.enterRule(localctx, 50, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MapperParser.T__30)
            self.state = 245
            self.match(MapperParser.T__4)
            self.state = 246
            self.exprComp()
            self.state = 247
            self.match(MapperParser.T__6)
            self.state = 248
            self.match(MapperParser.T__7)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35208078491678) != 0):
                self.state = 249
                self.statement()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
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
        self.enterRule(localctx, 52, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(MapperParser.T__31)
            self.state = 258
            self.match(MapperParser.T__4)
            self.state = 259
            self.numberAssign()
            self.state = 260
            self.match(MapperParser.T__32)
            self.state = 261
            self.expr(0)
            self.state = 262
            self.match(MapperParser.T__32)
            self.state = 263
            self.increment()
            self.state = 264
            self.match(MapperParser.T__6)
            self.state = 265
            self.match(MapperParser.T__7)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35208078491678) != 0):
                self.state = 266
                self.statement()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
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

        def exprComp(self):
            return self.getTypedRuleContext(MapperParser.ExprCompContext,0)


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
        self.enterRule(localctx, 54, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MapperParser.T__33)
            self.state = 275
            self.match(MapperParser.T__4)
            self.state = 276
            self.exprComp()
            self.state = 277
            self.match(MapperParser.T__6)
            self.state = 278
            self.match(MapperParser.T__7)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35208078491678) != 0):
                self.state = 279
                self.statement()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 285
            self.match(MapperParser.T__8)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 286
                self.match(MapperParser.T__34)
                self.state = 287
                self.match(MapperParser.T__7)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35208078491678) != 0):
                    self.state = 288
                    self.statement()
                    self.state = 293
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 294
                self.match(MapperParser.T__8)


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


        def getRuleIndex(self):
            return MapperParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprVarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapperParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(MapperParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprVar" ):
                listener.enterExprVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprVar" ):
                listener.exitExprVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprVar" ):
                return visitor.visitExprVar(self)
            else:
                return visitor.visitChildren(self)


    class ExprAddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapperParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapperParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAddSub" ):
                listener.enterExprAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAddSub" ):
                listener.exitExprAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddSub" ):
                return visitor.visitExprAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ExprMulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapperParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapperParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMulDiv" ):
                listener.enterExprMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMulDiv" ):
                listener.exitExprMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMulDiv" ):
                return visitor.visitExprMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapperParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MapperParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParens" ):
                listener.enterExprParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParens" ):
                listener.exitExprParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParens" ):
                return visitor.visitExprParens(self)
            else:
                return visitor.visitChildren(self)


    class ExprIntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapperParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MapperParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprInt" ):
                listener.enterExprInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprInt" ):
                listener.exitExprInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprInt" ):
                return visitor.visitExprInt(self)
            else:
                return visitor.visitChildren(self)


    class ExprBoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapperParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(MapperParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBool" ):
                listener.enterExprBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBool" ):
                listener.exitExprBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBool" ):
                return visitor.visitExprBool(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MapperParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = MapperParser.ExprParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 298
                self.match(MapperParser.T__4)
                self.state = 299
                self.expr(0)
                self.state = 300
                self.match(MapperParser.T__6)
                pass
            elif token in [45]:
                localctx = MapperParser.ExprVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 302
                self.match(MapperParser.IDENTIFIER)
                pass
            elif token in [46]:
                localctx = MapperParser.ExprIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 303
                self.match(MapperParser.INT)
                pass
            elif token in [47]:
                localctx = MapperParser.ExprBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 304
                self.match(MapperParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 313
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = MapperParser.ExprMulDivContext(self, MapperParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 307
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 308
                        _la = self._input.LA(1)
                        if not(_la==36 or _la==37):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 309
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MapperParser.ExprAddSubContext(self, MapperParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 310
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 311
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==38):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 312
                        self.expr(6)
                        pass

             
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprCompContext(ParserRuleContext):
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
            return MapperParser.RULE_exprComp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprComp" ):
                listener.enterExprComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprComp" ):
                listener.exitExprComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprComp" ):
                return visitor.visitExprComp(self)
            else:
                return visitor.visitChildren(self)




    def exprComp(self):

        localctx = MapperParser.ExprCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exprComp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expr(0)
            self.state = 319
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34634616274944) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 320
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




