# Generated from Expr.g4 by ANTLR 4.13.1
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
        4,1,21,110,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,45,8,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,9,
        3,1,3,1,3,1,3,5,3,61,8,3,10,3,12,3,64,9,3,1,3,1,3,1,4,1,4,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,83,8,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,5,6,93,8,6,10,6,12,6,96,9,6,1,7,1,7,1,7,
        1,7,1,7,5,7,103,8,7,10,7,12,7,106,9,7,1,7,1,7,1,7,0,1,12,8,0,2,4,
        6,8,10,12,14,0,2,2,0,8,8,10,12,1,0,1,2,115,0,19,1,0,0,0,2,29,1,0,
        0,0,4,31,1,0,0,0,6,46,1,0,0,0,8,67,1,0,0,0,10,69,1,0,0,0,12,82,1,
        0,0,0,14,97,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,21,1,0,0,0,19,
        17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,
        1,23,1,1,0,0,0,24,30,3,4,2,0,25,30,3,6,3,0,26,27,3,12,6,0,27,28,
        5,14,0,0,28,30,1,0,0,0,29,24,1,0,0,0,29,25,1,0,0,0,29,26,1,0,0,0,
        30,3,1,0,0,0,31,32,5,4,0,0,32,33,5,15,0,0,33,34,3,12,6,0,34,35,5,
        16,0,0,35,36,5,17,0,0,36,37,3,2,1,0,37,38,5,18,0,0,38,44,1,0,0,0,
        39,40,5,5,0,0,40,41,5,17,0,0,41,42,3,2,1,0,42,43,5,18,0,0,43,45,
        1,0,0,0,44,39,1,0,0,0,44,45,1,0,0,0,45,5,1,0,0,0,46,47,5,6,0,0,47,
        48,5,21,0,0,48,49,5,15,0,0,49,54,5,21,0,0,50,51,5,13,0,0,51,53,5,
        21,0,0,52,50,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,
        57,1,0,0,0,56,54,1,0,0,0,57,58,5,16,0,0,58,62,5,17,0,0,59,61,3,2,
        1,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,
        1,0,0,0,64,62,1,0,0,0,65,66,5,18,0,0,66,7,1,0,0,0,67,68,7,0,0,0,
        68,9,1,0,0,0,69,70,7,1,0,0,70,11,1,0,0,0,71,72,6,6,-1,0,72,83,5,
        19,0,0,73,83,5,21,0,0,74,83,3,14,7,0,75,76,5,21,0,0,76,77,5,7,0,
        0,77,83,3,12,6,5,78,79,5,3,0,0,79,83,3,12,6,4,80,81,5,9,0,0,81,83,
        3,12,6,1,82,71,1,0,0,0,82,73,1,0,0,0,82,74,1,0,0,0,82,75,1,0,0,0,
        82,78,1,0,0,0,82,80,1,0,0,0,83,94,1,0,0,0,84,85,10,3,0,0,85,86,3,
        8,4,0,86,87,3,12,6,4,87,93,1,0,0,0,88,89,10,2,0,0,89,90,3,10,5,0,
        90,91,3,12,6,3,91,93,1,0,0,0,92,84,1,0,0,0,92,88,1,0,0,0,93,96,1,
        0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,13,1,0,0,0,96,94,1,0,0,0,97,
        98,5,21,0,0,98,99,5,15,0,0,99,104,3,12,6,0,100,101,5,13,0,0,101,
        103,3,12,6,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,
        105,1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,108,5,16,0,0,108,
        15,1,0,0,0,9,19,29,44,54,62,82,92,94,104
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'if'", "'else'", 
                     "'def'", "'='", "'*'", "'return'", "'=='", "'+'", "'-'", 
                     "','", "';'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "IF", "ELSE", "DEF", 
                      "ASING", "MULT", "RETURN", "EQ", "SUM", "LESS", "COMMA", 
                      "SEMI", "LPAREN", "RPAREN", "LCURLY", "RCURLY", "INT", 
                      "WS", "ID" ]

    RULE_program = 0
    RULE_statment = 1
    RULE_ifstat = 2
    RULE_funcstat = 3
    RULE_operator = 4
    RULE_logic_operator = 5
    RULE_expr = 6
    RULE_func = 7

    ruleNames =  [ "program", "statment", "ifstat", "funcstat", "operator", 
                   "logic_operator", "expr", "func" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    IF=4
    ELSE=5
    DEF=6
    ASING=7
    MULT=8
    RETURN=9
    EQ=10
    SUM=11
    LESS=12
    COMMA=13
    SEMI=14
    LPAREN=15
    RPAREN=16
    LCURLY=17
    RCURLY=18
    INT=19
    WS=20
    ID=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def statment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatmentContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

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

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2622040) != 0):
                self.state = 16
                self.statment()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstat(self):
            return self.getTypedRuleContext(ExprParser.IfstatContext,0)


        def funcstat(self):
            return self.getTypedRuleContext(ExprParser.FuncstatContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_statment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatment" ):
                listener.enterStatment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatment" ):
                listener.exitStatment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatment" ):
                return visitor.visitStatment(self)
            else:
                return visitor.visitChildren(self)




    def statment(self):

        localctx = ExprParser.StatmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statment)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.ifstat()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.funcstat()
                pass
            elif token in [3, 9, 19, 21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(ExprParser.SEMI)
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


    class IfstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LCURLY)
            else:
                return self.getToken(ExprParser.LCURLY, i)

        def statment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatmentContext,i)


        def RCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RCURLY)
            else:
                return self.getToken(ExprParser.RCURLY, i)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_ifstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstat" ):
                listener.enterIfstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstat" ):
                listener.exitIfstat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstat" ):
                return visitor.visitIfstat(self)
            else:
                return visitor.visitChildren(self)




    def ifstat(self):

        localctx = ExprParser.IfstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ExprParser.IF)
            self.state = 32
            self.match(ExprParser.LPAREN)
            self.state = 33
            self.expr(0)
            self.state = 34
            self.match(ExprParser.RPAREN)
            self.state = 35
            self.match(ExprParser.LCURLY)
            self.state = 36
            self.statment()
            self.state = 37
            self.match(ExprParser.RCURLY)


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 39
                self.match(ExprParser.ELSE)
                self.state = 40
                self.match(ExprParser.LCURLY)
                self.state = 41
                self.statment()
                self.state = 42
                self.match(ExprParser.RCURLY)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(ExprParser.DEF, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def statment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatmentContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_funcstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncstat" ):
                listener.enterFuncstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncstat" ):
                listener.exitFuncstat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncstat" ):
                return visitor.visitFuncstat(self)
            else:
                return visitor.visitChildren(self)




    def funcstat(self):

        localctx = ExprParser.FuncstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ExprParser.DEF)
            self.state = 47
            self.match(ExprParser.ID)
            self.state = 48
            self.match(ExprParser.LPAREN)
            self.state = 49
            self.match(ExprParser.ID)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 50
                self.match(ExprParser.COMMA)
                self.state = 51
                self.match(ExprParser.ID)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(ExprParser.RPAREN)
            self.state = 58
            self.match(ExprParser.LCURLY)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2622040) != 0):
                self.state = 59
                self.statment()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(ExprParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(ExprParser.LESS, 0)

        def SUM(self):
            return self.getToken(ExprParser.SUM, 0)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = ExprParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7424) != 0)):
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


    class Logic_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_logic_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_operator" ):
                listener.enterLogic_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_operator" ):
                listener.exitLogic_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_operator" ):
                return visitor.visitLogic_operator(self)
            else:
                return visitor.visitChildren(self)




    def logic_operator(self):

        localctx = ExprParser.Logic_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_logic_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(ExprParser.FuncContext,0)


        def ASING(self):
            return self.getToken(ExprParser.ASING, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def operator(self):
            return self.getTypedRuleContext(ExprParser.OperatorContext,0)


        def logic_operator(self):
            return self.getTypedRuleContext(ExprParser.Logic_operatorContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 72
                self.match(ExprParser.INT)
                pass

            elif la_ == 2:
                self.state = 73
                self.match(ExprParser.ID)
                pass

            elif la_ == 3:
                self.state = 74
                self.func()
                pass

            elif la_ == 4:
                self.state = 75
                self.match(ExprParser.ID)
                self.state = 76
                self.match(ExprParser.ASING)
                self.state = 77
                self.expr(5)
                pass

            elif la_ == 5:
                self.state = 78
                self.match(ExprParser.NOT)
                self.state = 79
                self.expr(4)
                pass

            elif la_ == 6:
                self.state = 80
                self.match(ExprParser.RETURN)
                self.state = 81
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 85
                        self.operator()
                        self.state = 86
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 89
                        self.logic_operator()
                        self.state = 90
                        self.expr(3)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ExprParser.ID)
            self.state = 98
            self.match(ExprParser.LPAREN)
            self.state = 99
            self.expr(0)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 100
                self.match(ExprParser.COMMA)
                self.state = 101
                self.expr(0)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




