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
            | errorStatement
            | block
            ;

block : '{' statement* '}' ;

// Deklaracja zmiennej
errorStatement : ERROR expr DOT;
printStatement : 'print' exprList?;  // np. print x; print x, y, 42

//funkcje
param     : type IDENTIFIER ;
type : 'number'|'tile'|'blend'|'bool'|'void';

functionDecl :type 'function' IDENTIFIER '(' (param (',' param)*)? ')' '{' statement* '}';

functionCall : IDENTIFIER '(' exprList? ')';
returnStatement : 'return' expr?  ;
exprList     : expr (',' expr)*;


// Przypisania zmiennych
increment
    : IDENTIFIER '++'
    | IDENTIFIER '--'
    | IDENTIFIER '+=' expr
    | IDENTIFIER '-=' expr
    ;

tileSum      : IDENTIFIER ('+' IDENTIFIER)*;

reasignment  : IDENTIFIER '=' expr;
assignment   : tileAssign | numberAssign | boolAssign | increment | blendAssign | noValueAssign | reasignment | roadStart;
noValueAssign: type IDENTIFIER;

tileAssign   : 'tile' IDENTIFIER '=' tileSum; // atrybuty foreground i background są nadpisywane przez kolejne argumenty
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
draw        : 'draw' IDENTIFIER ('+' IDENTIFIER)*
            | 'draw' 'radius' INT percentagePair+;
percentagePair : INT '%' IDENTIFIER;

// Poruszanie wskaźnikiem
move        : 'pointer' ('up' expr | 'down' expr | 'left' expr | 'right' expr);

// Pętle
loop        : whileLoop | forLoop; 
whileLoop   : 'while' '(' exprComp ')' '{' statement* '}';
forLoop     : 'for' '(' numberAssign ';' expr ';' increment ')' '{' statement* '}';


// Instrukcja warunkowa
conditional : 'if' '(' (exprComp  | expr) ')' '{' ifConditionStatements '}' ('else' '{' elseConditionStatements '}')?;

ifConditionStatements : statement*;
elseConditionStatements : statement*;


// Wyrażenia arytmetyczne i logiczne
expr
            : expr ('*'|'/') expr                      # ExprMulDiv
            | expr ('+'|'-') expr                      # ExprAddSub
            | '(' expr ')'                             # ExprParens
            | INT                                      # ExprInt
            | BOOL                                     # ExprBool
            | IDENTIFIER                               # ExprVar
            | functionCall                             # ExprFUnctionCall;

exprComp    : expr ('=='|'!='|'>'|'<'|'>='|'<=') expr;

INT         : [0-9]+;
BOOL        : 'true' | 'false';
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
STRING      : '"' .*? '"';
WS          : [ \t\r\n]+ -> skip;
DOT         :'.';
ERROR       :'YAPPING';
