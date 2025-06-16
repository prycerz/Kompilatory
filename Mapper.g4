grammar Mapper;

// Program składa się z wielu instrukcji
program     : statement* EOF;

// Możliwe instrukcje
statement   : printStatement
            | reasignment
            | assignment
            | draw
            | move
            | loop
            | conditional
            | roadPlacement
            | functionDecl
            | functionCall
            | returnStatement
            | block
            ;

block : '{' statement* '}' ;

// Deklaracja zmiennej
printStatement : 'print' exprList?;  // np. print x; print x, y, 42

//funkcje
param     : type IDENTIFIER ;
type : 'number'|'tile'|'blend'|'bool'|'void';

functionDecl :type 'function' IDENTIFIER '(' (param (',' param)*)? ')' '{' statement* '}';

exprOrExprComp : expr | exprComp;

functionCall : IDENTIFIER '(' exprList? ')';
returnStatement : 'return' exprOrExprComp?  ;
exprList     : exprOrExprComp (',' exprOrExprComp)*;


// Przypisania zmiennych
increment
    : scopedIdentifier '++'
    | scopedIdentifier '--'
    | scopedIdentifier '+=' expr
    | scopedIdentifier '-=' expr
    ;

tileSum      : TILE_KEYWORD ('+' TILE_KEYWORD)*;

reasignment  : scopedIdentifier '=' (expr | exprComp);
assignment   : tileAssign | numberAssign | boolAssign | increment | blendAssign | noValueAssign | reasignment | roadStart;
noValueAssign: type IDENTIFIER;


tileAssign   : 'tile' IDENTIFIER '=' (tileSum | expr | tileCast); // atrybuty foreground i background są nadpisywane przez kolejne argumenty
tileCast     : '(tile)' IDENTIFIER;

numberAssign : 'number' IDENTIFIER '=' expr;
boolAssign   : 'bool' IDENTIFIER '=' (expr | exprComp);
blendAssign  : 'blend' IDENTIFIER '=' figure blendOption+; 
roadStart    : 'road' IDENTIFIER 'start';


roadPlacement: roadStart | roadEnd;
roadEnd      : 'road' IDENTIFIER 'end';

figure       : ('circle' INT) | ('rectangle' INT INT);
blendOption  : (IDENTIFIER | tileSum) INT '%';


// Rysowanie płytek
drawRoad    : 'drawRoad' IDENTIFIER;
draw        : 'draw' scopedIdentifier ('+' scopedIdentifier)*
            | 'draw' 'radius' INT percentagePair+;
percentagePair : INT '%' IDENTIFIER;

// Poruszanie wskaźnikiem
move        : 'pointer' ('up' expr | 'down' expr | 'left' expr | 'right' expr);

// Pętle
loop        : whileLoop | forLoop; 
whileLoop   : 'while' '(' exprComp ')' '{' statement* '}';
forLoop     : 'for' '(' assignment ';' exprComp ';' increment ')' '{' statement* '}';


// Instrukcja warunkowa
conditional : 'if' '(' (exprComp) ')' '{' ifConditionStatements '}' ('else' '{' elseConditionStatements '}')?;

ifConditionStatements : statement*;
elseConditionStatements : statement*;

scopedIdentifier : (SCOPE)? IDENTIFIER ;
// Wyrażenia arytmetyczne i logiczne
expr
            : '-' expr                                 # ExprUnaryMinus
            | expr ('*'|'/') expr                      # ExprMulDiv
            | expr ('+'|'-') expr                      # ExprAddSub
            | '(' expr ')'                             # ExprParens
            | INT                                      # ExprInt
//            | IDENTIFIER                               # ExprVar
            | scopedIdentifier                         # ScopedExprVar
            | functionCall                             # ExprFUnctionCall
            | TILE_KEYWORD                             # ExprTileKeyword
            ;

exprComp    : NOT exprComp                             # ExprNot
            | exprComp AND exprComp                    # ExprAnd
            | exprComp OR exprComp                     # ExprOr
            | expr ('=='|'!='|'>'|'<'|'>='|'<=') expr  # ExprCompRel
            | '(' exprComp ')'                         # ExprCompParens
            | exprComp ('==' | '!=') exprComp          # ExprCompBools
            | BOOL                                     # ExprCompBool
            | scopedIdentifier                         # ExprCompVar
            | '(bool)' expr                            # ExprCompCastToBool
            ;
            
TILE_KEYWORD
    : 'cabin'
    | 'church'
    | 'grass'
    | 'soil'
    | 'sand'
    | 'water'
    | 'rocks'
    | 'tree'
    | 'bush'
    | 'stones'
    | 'mountains'
    ;

AND         : 'and';
OR          : 'or';
NOT         : 'not';
INT         : [0-9]+;
BOOL        : 'true' | 'false';
SCOPE      : ':'+ ;
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
WS          : [ \t\r\n]+ -> skip;

SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' .*? '*/' -> skip;