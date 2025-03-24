grammar Mapper;

// Program składa się z wielu instrukcji
program     : statement* EOF;

// Możliwe instrukcje
statement   : assignment
            | draw
            | move
            | loop
            | conditional
            | errorHandling
            ;

// Przypisania zmiennych
increment    : IDENTIFIER '+=' expr; // problem bo chyba to dziala dla kazdej zmiennej nie tylko number
tileAssign   : 'tile' IDENTIFIER '=' IDENTIFIER ('+' IDENTIFIER)*; // atrybuty foreground i background są nadpisywane przez kolejne argumenty
assignment   : tileAssign | numberAssign | boolAssign | increment | blendAssign;
numberAssign : 'number' IDENTIFIER '=' expr;
boolAssign   : 'bool' IDENTIFIER '=' expr;


blendAssign  : 'blend' IDENTIFIER '=' figure blendOption+; 
figure       : ('circle' INT) | ('rectangle' INT INT);
blendOption  : IDENTIFIER INT '%';


// Rysowanie płytek
draw        : 'draw' IDENTIFIER ('+' IDENTIFIER)*
            | 'draw' 'radius' INT percentagePair+;
percentagePair : INT '%' IDENTIFIER;

// Poruszanie wskaźnikiem
move        : 'pointer' ('up' expr | 'down' expr | 'left' expr | 'right' expr);

// Pętla while
loop        : 'while' '(' expr ')' '{' statement* '}';

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

// Tokeny
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;
INT         : [0-9]+;
BOOL        : 'true' | 'false';
STRING      : '"' .*? '"';
WS          : [ \t\r\n]+ -> skip;
