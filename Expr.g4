grammar Expr;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
IF : 'if' ;
ELSE: 'else';
DEF : 'def' ;
ASING : '=' ;
MULT : '*' ;
RETURN : 'return';
EQ : '==' ;
SUM: '+';
LESS: '-';
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;


INT : [0-9]+ ;

WS: [ \t\n\r\f]+ -> skip ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;

program: statment* EOF;

statment: ifstat
    | funcstat
    | expr SEMI
    ;
    
ifstat: IF '(' expr ')' LCURLY statment RCURLY ()
(ELSE LCURLY statment RCURLY)?
;

funcstat : 
    DEF ID '(' ID (',' ID)* ')' LCURLY statment* RCURLY
;

operator
    : LESS
    | SUM
    | MULT
    | EQ
    ;
logic_operator
    :OR
    |AND
;
    
expr: INT
    | ID
    | func
    | ID ASING expr
    | 'not' expr
    | expr operator expr
    | expr logic_operator expr
    | RETURN expr
    ;


func : ID '(' expr (',' expr)* ')' ;

