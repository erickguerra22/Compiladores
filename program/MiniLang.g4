grammar MiniLang;

prog:   stat+ ;

stat:   expr NEWLINE                 # printExpr
    |   ID '=' expr NEWLINE          # assign
    |   NEWLINE                      # blank
    |   COMMENT NEWLINE?             # comentario
    |   ifstat                       # estructura_if
    |   whilestat                    # estructura_while
    |   funcdec                      # declaracion_de_funcion
    |   funccall                     # llamada_a_funcion
    ;

expr:   INT ('*'|'/') INT                               # MulDiv_INTs
    |   INT ('+'|'-') INT                               # AddSub_INTs
    |   INT ('=='|'!='|'<'|'>'|'>='|'<=') INT           # comparacion_INTs
    |   STRING ('*'|'/') STRING                         # MulDiv_STRINGs
    |   STRING ('+'|'-') STRING                         # AddSub_STRINGs
    |   STRING ('=='|'!='|'<'|'>'|'>='|'<=') STRING     # comparacion_STRINGs
    |   INT                                             # int
    |   STRING                                          # string
    |   ID                                              # id
    |   '(' expr ')'                                    # parens
    ;

ifstat: 'if' '(' expr ')' '{' prog '}' ('else' '{' prog '}')?;

whilestat: 'while' '(' expr ')' '{' prog '}';

funcdec: 'function' ID '(' params ')' '{' prog '}' ;

funccall: ID '(' args ')' ;

params: (ID (',' ID)*)? ;

args: (expr (',' expr)*)? ;

MUL : '*' ; // define token for multiplication
DIV : '/' ; // define token for division
ADD : '+' ; // define token for addition
SUB : '-' ; // define token for subtraction
EQUAL : '==' ; // token para igualdad
NOTEQUAL : '!=' ; // token para desigualdad
BTHAN : '>' ; // token para mayor que
LTHAN : '<' ; // token para menor que
BEQ : '>=' ; // token para mayor o igual
LEQ : '<=' ; // token para menor o igual
ID  : [a-zA-Z]+ ; // match identifiers
INT : [0-9]+ ; // match integers
STRING : ('"' | '\'') (~["\r\n])* ('"' | '\'') ; // match strings
NEWLINE:'\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS  : [ \t]+ -> skip ; // toss out whitespace

COMMENT : '//' ~[\r\n]* -> skip ; // comentario de una línea