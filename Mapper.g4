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
            | errorStatement
            ;

// Deklaracja zmiennej
errorStatement : ERROR expr DOT;
printStatement : 'print' exprList?;  // np. print x; print x, y, 42

//funkcje
param     : type IDENTIFIER ;
type : 'number'|'tile'|'blend';

functionDecl : 'function' IDENTIFIER '(' (param (',' param)*)? ')' '{' statement* '}';

functionCall : IDENTIFIER '(' exprList? ')';
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
assignment   : tileAssign | numberAssign | boolAssign | increment | blendAssign | noValueAssign | reasignment;
noValueAssign: type IDENTIFIER;

tileAssign   : 'tile' IDENTIFIER '=' tileSum; // atrybuty foreground i background są nadpisywane przez kolejne argumenty
numberAssign : 'number' IDENTIFIER '=' expr;
boolAssign   : 'bool' IDENTIFIER '=' expr;
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
conditional : 'if' '(' exprComp ')' '{' statement* '}' ('else' '{' statement* '}')?;



// Wyrażenia arytmetyczne i logiczne
expr
            : expr ('*'|'/') expr                      # ExprMulDiv
            | expr ('+'|'-') expr                      # ExprAddSub
            | '(' expr ')'                             # ExprParens
            | IDENTIFIER                               # ExprVar
            | INT                                      # ExprInt
            | BOOL                                     # ExprBool;

exprComp    : expr ('=='|'!='|'>'|'<'|'>='|'<=') expr;

IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
INT         : [0-9]+;
BOOL        : 'true' | 'false';
STRING      : '"' .*? '"';
WS          : [ \t\r\n]+ -> skip;
DOT         :'.';
ERROR       :'YAPPING';
