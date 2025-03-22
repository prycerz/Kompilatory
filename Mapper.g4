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
tileAssign  : 'tile' IDENTIFIER '=' IDENTIFIER ('+' IDENTIFIER)?;
numberAssign : 'number' IDENTIFIER '=' expr;
boolAssign   : 'bool' IDENTIFIER '=' expr;
assignment  : tileAssign | numberAssign | boolAssign;

// Rysowanie płytek
draw        : 'draw' IDENTIFIER;

// Poruszanie wskaźnikiem
move        : 'pointer' ('up' INT | 'down' INT | 'left' INT | 'right' INT);

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
