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
            | block
            ;

block : '{' statement* '}' ;

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
            | INT                         # ExprInt
            | BOOL                                     # ExprBool
            | IDENTIFIER                               # ExprVar;

exprComp    : 'not' exprComp                           # ExprNot
            | exprComp 'and' exprComp                  # ExprAnd
            | exprComp 'or' exprComp                   # ExprOr
            | expr ('=='|'!='|'>'|'<'|'>='|'<=') expr  # ExprCompRel
            | '(' exprComp ')'                         # ExprCompParens
            | BOOL                                     # ExprCompBool
            | IDENTIFIER                               # ExprCompVar;

INT         : [0-9]+;
BOOL        : 'true' | 'false';
// Nowe tokeny dla operatorów logicznych
AND         : 'and';
OR          : 'or';
NOT         : 'not';
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
STRING      : '"' .*? '"';
WS          : [ \t\r\n]+ -> skip;
DOT         :'.';
ERROR       :'YAPPING';



// Reguły dla komentarzy
SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' .*? '*/' -> skip;
