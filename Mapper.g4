grammar Mapper;

// Program składa się z wielu instrukcji
program     : statement* EOF;

// Możliwe instrukcje
statement   : assignment
            | draw
            | move
            | loop
            | conditional
            | roadPlacement
            | errorHandling
            | functionDecl
            | functionCall
            ;

//funkcje
param     : type IDENTIFIER ;
type : 'number'|'tile'|'blend';

functionDecl : 'function' IDENTIFIER '(' (param (',' param)*)? ')' '{' statement* '}';


functionCall : IDENTIFIER '(' exprList? ')';
exprList     : expr (',' expr)*;
// Przypisania zmiennych
increment    : IDENTIFIER '+=' expr; // problem bo chyba to dziala dla kazdej zmiennej nie tylko number

tileAssign   : 'tile' IDENTIFIER '=' tileSum; // atrybuty foreground i background są nadpisywane przez kolejne argumenty
tileSum      : IDENTIFIER ('+' IDENTIFIER)*;

assignment   : tileAssign | numberAssign | boolAssign | increment | blendAssign;
numberAssign : 'number' IDENTIFIER '=' expr;
boolAssign   : 'bool' IDENTIFIER '=' expr;

roadPlacement: roadStart | roadEnd;
roadStart    : 'road' IDENTIFIER 'start';
roadEnd      : 'road' IDENTIFIER 'end';

blendAssign  : 'blend' IDENTIFIER '=' figure blendOption+; 
figure       : ('circle' INT) | ('rectangle' INT INT);
blendOption  : (IDENTIFIER | tileSum) INT '%';


// Rysowanie płytek
draw        : 'draw' IDENTIFIER ('+' IDENTIFIER)*
            | 'draw' 'radius' INT percentagePair+;
percentagePair : INT '%' IDENTIFIER;

// Poruszanie wskaźnikiem
move        : 'pointer' ('up' expr | 'down' expr | 'left' expr | 'right' expr);

// Pętle
loop        : whileLoop | forLoop; 
whileLoop   : 'while' '(' expr ')' '{' statement* '}';
forLoop     : 'for' '(' numberAssign ';' expr ';' increment ')' '{' statement* '}';

// Instrukcja warunkowa
conditional : 'if' '(' expr ')' '{' statement* '}' ('else' '{' statement* '}')?;

// Obsługa błędów
errorHandling : 'Yapping' '(' STRING ')';

// Wyrażenia arytmetyczne i logiczne
expr        : expr ('+'|'-') expr
            | expr ('*'|'/') expr
            | expr ('=='|'!='|'>'|'<'|'>='|'<=') expr
            | '(' expr ')'
            | IDENTIFIER
            | INT
            | BOOL;



IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
INT         : [0-9]+;
BOOL        : 'true' | 'false';
STRING      : '"' .*? '"';
WS          : [ \t\r\n]+ -> skip;
