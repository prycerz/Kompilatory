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
        4,1,46,315,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,2,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,3,4,94,8,4,1,4,
        1,4,1,4,5,4,99,8,4,10,4,12,4,102,9,4,1,4,1,4,1,5,1,5,1,5,3,5,109,
        8,5,1,5,1,5,1,6,1,6,1,6,5,6,116,8,6,10,6,12,6,119,9,6,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,133,8,9,10,9,12,9,136,
        9,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,144,8,10,1,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,3,
        14,162,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,
        17,1,17,1,17,4,17,177,8,17,11,17,12,17,178,1,18,1,18,1,18,1,18,1,
        18,3,18,186,8,18,1,19,1,19,3,19,190,8,19,1,19,1,19,1,19,1,20,1,20,
        1,20,1,20,5,20,199,8,20,10,20,12,20,202,9,20,1,20,1,20,1,20,1,20,
        4,20,208,8,20,11,20,12,20,209,3,20,212,8,20,1,21,1,21,1,21,1,21,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,227,8,22,1,23,
        1,23,3,23,231,8,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,239,8,24,10,
        24,12,24,242,9,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,5,25,256,8,25,10,25,12,25,259,9,25,1,25,1,25,1,26,1,
        26,1,26,1,26,1,26,1,26,5,26,269,8,26,10,26,12,26,272,9,26,1,26,1,
        26,1,26,1,26,5,26,278,8,26,10,26,12,26,281,9,26,1,26,3,26,284,8,
        26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,3,28,299,8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,
        28,310,8,28,10,28,12,28,313,9,28,1,28,0,1,56,29,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        0,4,1,0,1,3,1,0,33,38,1,0,39,40,2,0,12,12,41,41,327,0,61,1,0,0,0,
        2,75,1,0,0,0,4,77,1,0,0,0,6,80,1,0,0,0,8,82,1,0,0,0,10,105,1,0,0,
        0,12,112,1,0,0,0,14,120,1,0,0,0,16,124,1,0,0,0,18,129,1,0,0,0,20,
        143,1,0,0,0,22,145,1,0,0,0,24,150,1,0,0,0,26,154,1,0,0,0,28,161,
        1,0,0,0,30,163,1,0,0,0,32,167,1,0,0,0,34,171,1,0,0,0,36,185,1,0,
        0,0,38,189,1,0,0,0,40,211,1,0,0,0,42,213,1,0,0,0,44,217,1,0,0,0,
        46,230,1,0,0,0,48,232,1,0,0,0,50,245,1,0,0,0,52,262,1,0,0,0,54,285,
        1,0,0,0,56,298,1,0,0,0,58,60,3,2,1,0,59,58,1,0,0,0,60,63,1,0,0,0,
        61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,
        0,0,1,65,1,1,0,0,0,66,76,3,20,10,0,67,76,3,40,20,0,68,76,3,44,22,
        0,69,76,3,46,23,0,70,76,3,52,26,0,71,76,3,28,14,0,72,76,3,54,27,
        0,73,76,3,8,4,0,74,76,3,10,5,0,75,66,1,0,0,0,75,67,1,0,0,0,75,68,
        1,0,0,0,75,69,1,0,0,0,75,70,1,0,0,0,75,71,1,0,0,0,75,72,1,0,0,0,
        75,73,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,0,77,78,3,6,3,0,78,79,5,42,
        0,0,79,5,1,0,0,0,80,81,7,0,0,0,81,7,1,0,0,0,82,83,5,4,0,0,83,84,
        5,42,0,0,84,93,5,5,0,0,85,90,3,4,2,0,86,87,5,6,0,0,87,89,3,4,2,0,
        88,86,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,94,1,
        0,0,0,92,90,1,0,0,0,93,85,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,
        96,5,7,0,0,96,100,5,8,0,0,97,99,3,2,1,0,98,97,1,0,0,0,99,102,1,0,
        0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,
        0,103,104,5,9,0,0,104,9,1,0,0,0,105,106,5,42,0,0,106,108,5,5,0,0,
        107,109,3,12,6,0,108,107,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,
        110,111,5,7,0,0,111,11,1,0,0,0,112,117,3,56,28,0,113,114,5,6,0,0,
        114,116,3,56,28,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,
        0,117,118,1,0,0,0,118,13,1,0,0,0,119,117,1,0,0,0,120,121,5,42,0,
        0,121,122,5,10,0,0,122,123,3,56,28,0,123,15,1,0,0,0,124,125,5,2,
        0,0,125,126,5,42,0,0,126,127,5,11,0,0,127,128,3,18,9,0,128,17,1,
        0,0,0,129,134,5,42,0,0,130,131,5,12,0,0,131,133,5,42,0,0,132,130,
        1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,19,1,
        0,0,0,136,134,1,0,0,0,137,144,3,16,8,0,138,144,3,22,11,0,139,144,
        3,26,13,0,140,144,3,14,7,0,141,144,3,34,17,0,142,144,3,24,12,0,143,
        137,1,0,0,0,143,138,1,0,0,0,143,139,1,0,0,0,143,140,1,0,0,0,143,
        141,1,0,0,0,143,142,1,0,0,0,144,21,1,0,0,0,145,146,5,1,0,0,146,147,
        5,42,0,0,147,148,5,11,0,0,148,149,3,56,28,0,149,23,1,0,0,0,150,151,
        5,42,0,0,151,152,5,11,0,0,152,153,3,56,28,0,153,25,1,0,0,0,154,155,
        5,13,0,0,155,156,5,42,0,0,156,157,5,11,0,0,157,158,3,56,28,0,158,
        27,1,0,0,0,159,162,3,30,15,0,160,162,3,32,16,0,161,159,1,0,0,0,161,
        160,1,0,0,0,162,29,1,0,0,0,163,164,5,14,0,0,164,165,5,42,0,0,165,
        166,5,15,0,0,166,31,1,0,0,0,167,168,5,14,0,0,168,169,5,42,0,0,169,
        170,5,16,0,0,170,33,1,0,0,0,171,172,5,3,0,0,172,173,5,42,0,0,173,
        174,5,11,0,0,174,176,3,36,18,0,175,177,3,38,19,0,176,175,1,0,0,0,
        177,178,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,35,1,0,0,0,180,
        181,5,17,0,0,181,186,5,43,0,0,182,183,5,18,0,0,183,184,5,43,0,0,
        184,186,5,43,0,0,185,180,1,0,0,0,185,182,1,0,0,0,186,37,1,0,0,0,
        187,190,5,42,0,0,188,190,3,18,9,0,189,187,1,0,0,0,189,188,1,0,0,
        0,190,191,1,0,0,0,191,192,5,43,0,0,192,193,5,19,0,0,193,39,1,0,0,
        0,194,195,5,20,0,0,195,200,5,42,0,0,196,197,5,12,0,0,197,199,5,42,
        0,0,198,196,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,
        0,0,201,212,1,0,0,0,202,200,1,0,0,0,203,204,5,20,0,0,204,205,5,21,
        0,0,205,207,5,43,0,0,206,208,3,42,21,0,207,206,1,0,0,0,208,209,1,
        0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,194,1,
        0,0,0,211,203,1,0,0,0,212,41,1,0,0,0,213,214,5,43,0,0,214,215,5,
        19,0,0,215,216,5,42,0,0,216,43,1,0,0,0,217,226,5,22,0,0,218,219,
        5,23,0,0,219,227,3,56,28,0,220,221,5,24,0,0,221,227,3,56,28,0,222,
        223,5,25,0,0,223,227,3,56,28,0,224,225,5,26,0,0,225,227,3,56,28,
        0,226,218,1,0,0,0,226,220,1,0,0,0,226,222,1,0,0,0,226,224,1,0,0,
        0,227,45,1,0,0,0,228,231,3,48,24,0,229,231,3,50,25,0,230,228,1,0,
        0,0,230,229,1,0,0,0,231,47,1,0,0,0,232,233,5,27,0,0,233,234,5,5,
        0,0,234,235,3,56,28,0,235,236,5,7,0,0,236,240,5,8,0,0,237,239,3,
        2,1,0,238,237,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,241,1,
        0,0,0,241,243,1,0,0,0,242,240,1,0,0,0,243,244,5,9,0,0,244,49,1,0,
        0,0,245,246,5,28,0,0,246,247,5,5,0,0,247,248,3,22,11,0,248,249,5,
        29,0,0,249,250,3,56,28,0,250,251,5,29,0,0,251,252,3,14,7,0,252,253,
        5,7,0,0,253,257,5,8,0,0,254,256,3,2,1,0,255,254,1,0,0,0,256,259,
        1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,0,258,260,1,0,0,0,259,257,
        1,0,0,0,260,261,5,9,0,0,261,51,1,0,0,0,262,263,5,30,0,0,263,264,
        5,5,0,0,264,265,3,56,28,0,265,266,5,7,0,0,266,270,5,8,0,0,267,269,
        3,2,1,0,268,267,1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,271,
        1,0,0,0,271,273,1,0,0,0,272,270,1,0,0,0,273,283,5,9,0,0,274,275,
        5,31,0,0,275,279,5,8,0,0,276,278,3,2,1,0,277,276,1,0,0,0,278,281,
        1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,282,1,0,0,0,281,279,
        1,0,0,0,282,284,5,9,0,0,283,274,1,0,0,0,283,284,1,0,0,0,284,53,1,
        0,0,0,285,286,5,32,0,0,286,287,5,5,0,0,287,288,5,45,0,0,288,289,
        5,7,0,0,289,55,1,0,0,0,290,291,6,28,-1,0,291,292,5,5,0,0,292,293,
        3,56,28,0,293,294,5,7,0,0,294,299,1,0,0,0,295,299,5,42,0,0,296,299,
        5,43,0,0,297,299,5,44,0,0,298,290,1,0,0,0,298,295,1,0,0,0,298,296,
        1,0,0,0,298,297,1,0,0,0,299,311,1,0,0,0,300,301,10,7,0,0,301,302,
        7,1,0,0,302,310,3,56,28,8,303,304,10,6,0,0,304,305,7,2,0,0,305,310,
        3,56,28,7,306,307,10,5,0,0,307,308,7,3,0,0,308,310,3,56,28,6,309,
        300,1,0,0,0,309,303,1,0,0,0,309,306,1,0,0,0,310,313,1,0,0,0,311,
        309,1,0,0,0,311,312,1,0,0,0,312,57,1,0,0,0,313,311,1,0,0,0,26,61,
        75,90,93,100,108,117,134,143,161,178,185,189,200,209,211,226,230,
        240,257,270,279,283,298,309,311
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
                     "';'", "'if'", "'else'", "'Yapping'", "'=='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='", "'*'", "'/'", "'-'" ]

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
    RULE_varAssign = 12
    RULE_boolAssign = 13
    RULE_roadPlacement = 14
    RULE_roadStart = 15
    RULE_roadEnd = 16
    RULE_blendAssign = 17
    RULE_figure = 18
    RULE_blendOption = 19
    RULE_draw = 20
    RULE_percentagePair = 21
    RULE_move = 22
    RULE_loop = 23
    RULE_whileLoop = 24
    RULE_forLoop = 25
    RULE_conditional = 26
    RULE_errorHandling = 27
    RULE_expr = 28

    ruleNames =  [ "program", "statement", "param", "type", "functionDecl", 
                   "functionCall", "exprList", "increment", "tileAssign", 
                   "tileSum", "assignment", "numberAssign", "varAssign", 
                   "boolAssign", "roadPlacement", "roadStart", "roadEnd", 
                   "blendAssign", "figure", "blendOption", "draw", "percentagePair", 
                   "move", "loop", "whileLoop", "forLoop", "conditional", 
                   "errorHandling", "expr" ]

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
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
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
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.draw()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.move()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.conditional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.roadPlacement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.errorHandling()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 73
                self.functionDecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 74
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
            self.state = 77
            self.type_()
            self.state = 78
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
            self.state = 80
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
            self.state = 82
            self.match(MapperParser.T__3)
            self.state = 83
            self.match(MapperParser.IDENTIFIER)
            self.state = 84
            self.match(MapperParser.T__4)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 85
                self.param()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 86
                    self.match(MapperParser.T__5)
                    self.state = 87
                    self.param()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 95
            self.match(MapperParser.T__6)
            self.state = 96
            self.match(MapperParser.T__7)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 97
                self.statement()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
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
            self.state = 105
            self.match(MapperParser.IDENTIFIER)
            self.state = 106
            self.match(MapperParser.T__4)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30786325577760) != 0):
                self.state = 107
                self.exprList()


            self.state = 110
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
            self.state = 112
            self.expr(0)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 113
                self.match(MapperParser.T__5)
                self.state = 114
                self.expr(0)
                self.state = 119
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
            self.state = 120
            self.match(MapperParser.IDENTIFIER)
            self.state = 121
            self.match(MapperParser.T__9)
            self.state = 122
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
            self.state = 124
            self.match(MapperParser.T__1)
            self.state = 125
            self.match(MapperParser.IDENTIFIER)
            self.state = 126
            self.match(MapperParser.T__10)
            self.state = 127
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
            self.state = 129
            self.match(MapperParser.IDENTIFIER)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 130
                self.match(MapperParser.T__11)
                self.state = 131
                self.match(MapperParser.IDENTIFIER)
                self.state = 136
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.tileAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.numberAssign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.boolAssign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.increment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.blendAssign()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 142
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
            self.state = 145
            self.match(MapperParser.T__0)
            self.state = 146
            self.match(MapperParser.IDENTIFIER)
            self.state = 147
            self.match(MapperParser.T__10)
            self.state = 148
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
            self.state = 150
            self.match(MapperParser.IDENTIFIER)
            self.state = 151
            self.match(MapperParser.T__10)
            self.state = 152
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
            self.state = 154
            self.match(MapperParser.T__12)
            self.state = 155
            self.match(MapperParser.IDENTIFIER)
            self.state = 156
            self.match(MapperParser.T__10)
            self.state = 157
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
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.roadStart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
            self.state = 163
            self.match(MapperParser.T__13)
            self.state = 164
            self.match(MapperParser.IDENTIFIER)
            self.state = 165
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
        self.enterRule(localctx, 32, self.RULE_roadEnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MapperParser.T__13)
            self.state = 168
            self.match(MapperParser.IDENTIFIER)
            self.state = 169
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
        self.enterRule(localctx, 34, self.RULE_blendAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MapperParser.T__2)
            self.state = 172
            self.match(MapperParser.IDENTIFIER)
            self.state = 173
            self.match(MapperParser.T__10)
            self.state = 174
            self.figure()
            self.state = 176 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 175
                    self.blendOption()

                else:
                    raise NoViableAltException(self)
                self.state = 178 
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
        self.enterRule(localctx, 36, self.RULE_figure)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(MapperParser.T__16)
                self.state = 181
                self.match(MapperParser.INT)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(MapperParser.T__17)
                self.state = 183
                self.match(MapperParser.INT)
                self.state = 184
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
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 187
                self.match(MapperParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 188
                self.tileSum()
                pass


            self.state = 191
            self.match(MapperParser.INT)
            self.state = 192
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
        self.enterRule(localctx, 40, self.RULE_draw)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(MapperParser.T__19)
                self.state = 195
                self.match(MapperParser.IDENTIFIER)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 196
                    self.match(MapperParser.T__11)
                    self.state = 197
                    self.match(MapperParser.IDENTIFIER)
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(MapperParser.T__19)
                self.state = 204
                self.match(MapperParser.T__20)
                self.state = 205
                self.match(MapperParser.INT)
                self.state = 207 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 206
                    self.percentagePair()
                    self.state = 209 
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
        self.enterRule(localctx, 42, self.RULE_percentagePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MapperParser.INT)
            self.state = 214
            self.match(MapperParser.T__18)
            self.state = 215
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
        self.enterRule(localctx, 44, self.RULE_move)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MapperParser.T__21)
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 218
                self.match(MapperParser.T__22)
                self.state = 219
                self.expr(0)
                pass
            elif token in [24]:
                self.state = 220
                self.match(MapperParser.T__23)
                self.state = 221
                self.expr(0)
                pass
            elif token in [25]:
                self.state = 222
                self.match(MapperParser.T__24)
                self.state = 223
                self.expr(0)
                pass
            elif token in [26]:
                self.state = 224
                self.match(MapperParser.T__25)
                self.state = 225
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
        self.enterRule(localctx, 46, self.RULE_loop)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.whileLoop()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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
        self.enterRule(localctx, 48, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MapperParser.T__26)
            self.state = 233
            self.match(MapperParser.T__4)
            self.state = 234
            self.expr(0)
            self.state = 235
            self.match(MapperParser.T__6)
            self.state = 236
            self.match(MapperParser.T__7)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 237
                self.statement()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
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
        self.enterRule(localctx, 50, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MapperParser.T__27)
            self.state = 246
            self.match(MapperParser.T__4)
            self.state = 247
            self.numberAssign()
            self.state = 248
            self.match(MapperParser.T__28)
            self.state = 249
            self.expr(0)
            self.state = 250
            self.match(MapperParser.T__28)
            self.state = 251
            self.increment()
            self.state = 252
            self.match(MapperParser.T__6)
            self.state = 253
            self.match(MapperParser.T__7)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 254
                self.statement()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
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
        self.enterRule(localctx, 52, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(MapperParser.T__29)
            self.state = 263
            self.match(MapperParser.T__4)
            self.state = 264
            self.expr(0)
            self.state = 265
            self.match(MapperParser.T__6)
            self.state = 266
            self.match(MapperParser.T__7)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                self.state = 267
                self.statement()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 273
            self.match(MapperParser.T__8)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 274
                self.match(MapperParser.T__30)
                self.state = 275
                self.match(MapperParser.T__7)
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4403823140894) != 0):
                    self.state = 276
                    self.statement()
                    self.state = 281
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 282
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
        self.enterRule(localctx, 54, self.RULE_errorHandling)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MapperParser.T__31)
            self.state = 286
            self.match(MapperParser.T__4)
            self.state = 287
            self.match(MapperParser.STRING)
            self.state = 288
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


    class ExprCompContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapperParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapperParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapperParser.ExprContext,i)


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
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = MapperParser.ExprParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 291
                self.match(MapperParser.T__4)
                self.state = 292
                self.expr(0)
                self.state = 293
                self.match(MapperParser.T__6)
                pass
            elif token in [42]:
                localctx = MapperParser.ExprVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 295
                self.match(MapperParser.IDENTIFIER)
                pass
            elif token in [43]:
                localctx = MapperParser.ExprIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 296
                self.match(MapperParser.INT)
                pass
            elif token in [44]:
                localctx = MapperParser.ExprBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 297
                self.match(MapperParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 309
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MapperParser.ExprCompContext(self, MapperParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 300
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 301
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 541165879296) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 302
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = MapperParser.ExprMulDivContext(self, MapperParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 303
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 304
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==40):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 305
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = MapperParser.ExprAddSubContext(self, MapperParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 306
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 307
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==41):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 308
                        self.expr(6)
                        pass

             
                self.state = 313
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
        self._predicates[28] = self.expr_sempred
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
         




