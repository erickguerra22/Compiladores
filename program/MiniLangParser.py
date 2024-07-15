# Generated from MiniLang.g4 by ANTLR 4.13.1
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
        4,1,26,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,1,1,1,1,1,1,1,3,1,41,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,68,8,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,82,8,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,5,7,109,8,7,10,7,12,7,112,9,7,3,7,114,8,7,1,8,1,8,1,
        8,5,8,119,8,8,10,8,12,8,122,9,8,3,8,124,8,8,1,8,0,0,9,0,2,4,6,8,
        10,12,14,16,0,3,1,0,11,12,1,0,13,14,1,0,15,20,139,0,19,1,0,0,0,2,
        40,1,0,0,0,4,67,1,0,0,0,6,69,1,0,0,0,8,83,1,0,0,0,10,91,1,0,0,0,
        12,100,1,0,0,0,14,113,1,0,0,0,16,123,1,0,0,0,18,20,3,2,1,0,19,18,
        1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,
        24,3,4,2,0,24,25,5,24,0,0,25,41,1,0,0,0,26,27,5,21,0,0,27,28,5,1,
        0,0,28,29,3,4,2,0,29,30,5,24,0,0,30,41,1,0,0,0,31,41,5,24,0,0,32,
        34,5,26,0,0,33,35,5,24,0,0,34,33,1,0,0,0,34,35,1,0,0,0,35,41,1,0,
        0,0,36,41,3,6,3,0,37,41,3,8,4,0,38,41,3,10,5,0,39,41,3,12,6,0,40,
        23,1,0,0,0,40,26,1,0,0,0,40,31,1,0,0,0,40,32,1,0,0,0,40,36,1,0,0,
        0,40,37,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,5,
        22,0,0,43,44,7,0,0,0,44,68,5,22,0,0,45,46,5,22,0,0,46,47,7,1,0,0,
        47,68,5,22,0,0,48,49,5,22,0,0,49,50,7,2,0,0,50,68,5,22,0,0,51,52,
        5,23,0,0,52,53,7,0,0,0,53,68,5,23,0,0,54,55,5,23,0,0,55,56,7,1,0,
        0,56,68,5,23,0,0,57,58,5,23,0,0,58,59,7,2,0,0,59,68,5,23,0,0,60,
        68,5,22,0,0,61,68,5,23,0,0,62,68,5,21,0,0,63,64,5,2,0,0,64,65,3,
        4,2,0,65,66,5,3,0,0,66,68,1,0,0,0,67,42,1,0,0,0,67,45,1,0,0,0,67,
        48,1,0,0,0,67,51,1,0,0,0,67,54,1,0,0,0,67,57,1,0,0,0,67,60,1,0,0,
        0,67,61,1,0,0,0,67,62,1,0,0,0,67,63,1,0,0,0,68,5,1,0,0,0,69,70,5,
        4,0,0,70,71,5,2,0,0,71,72,3,4,2,0,72,73,5,3,0,0,73,74,5,5,0,0,74,
        75,3,0,0,0,75,81,5,6,0,0,76,77,5,7,0,0,77,78,5,5,0,0,78,79,3,0,0,
        0,79,80,5,6,0,0,80,82,1,0,0,0,81,76,1,0,0,0,81,82,1,0,0,0,82,7,1,
        0,0,0,83,84,5,8,0,0,84,85,5,2,0,0,85,86,3,4,2,0,86,87,5,3,0,0,87,
        88,5,5,0,0,88,89,3,0,0,0,89,90,5,6,0,0,90,9,1,0,0,0,91,92,5,9,0,
        0,92,93,5,21,0,0,93,94,5,2,0,0,94,95,3,14,7,0,95,96,5,3,0,0,96,97,
        5,5,0,0,97,98,3,0,0,0,98,99,5,6,0,0,99,11,1,0,0,0,100,101,5,21,0,
        0,101,102,5,2,0,0,102,103,3,16,8,0,103,104,5,3,0,0,104,13,1,0,0,
        0,105,110,5,21,0,0,106,107,5,10,0,0,107,109,5,21,0,0,108,106,1,0,
        0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,114,1,0,
        0,0,112,110,1,0,0,0,113,105,1,0,0,0,113,114,1,0,0,0,114,15,1,0,0,
        0,115,120,3,4,2,0,116,117,5,10,0,0,117,119,3,4,2,0,118,116,1,0,0,
        0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,124,1,0,0,
        0,122,120,1,0,0,0,123,115,1,0,0,0,123,124,1,0,0,0,124,17,1,0,0,0,
        9,21,34,40,67,81,110,113,120,123
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'if'", "'{'", "'}'", 
                     "'else'", "'while'", "'function'", "','", "'*'", "'/'", 
                     "'+'", "'-'", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "EQUAL", "NOTEQUAL", "BTHAN", "LTHAN", 
                      "BEQ", "LEQ", "ID", "INT", "STRING", "NEWLINE", "WS", 
                      "COMMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_ifstat = 3
    RULE_whilestat = 4
    RULE_funcdec = 5
    RULE_funccall = 6
    RULE_params = 7
    RULE_args = 8

    ruleNames =  [ "prog", "stat", "expr", "ifstat", "whilestat", "funcdec", 
                   "funccall", "params", "args" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    MUL=11
    DIV=12
    ADD=13
    SUB=14
    EQUAL=15
    NOTEQUAL=16
    BTHAN=17
    LTHAN=18
    BEQ=19
    LEQ=20
    ID=21
    INT=22
    STRING=23
    NEWLINE=24
    WS=25
    COMMENT=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MiniLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.stat()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 98566932) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class Declaracion_de_funcionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcdec(self):
            return self.getTypedRuleContext(MiniLangParser.FuncdecContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_de_funcion" ):
                listener.enterDeclaracion_de_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_de_funcion" ):
                listener.exitDeclaracion_de_funcion(self)


    class ComentarioContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMMENT(self):
            return self.getToken(MiniLangParser.COMMENT, 0)
        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComentario" ):
                listener.enterComentario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComentario" ):
                listener.exitComentario(self)


    class Llamada_a_funcionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funccall(self):
            return self.getTypedRuleContext(MiniLangParser.FunccallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_a_funcion" ):
                listener.enterLlamada_a_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_a_funcion" ):
                listener.exitLlamada_a_funcion(self)


    class Estructura_whileContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whilestat(self):
            return self.getTypedRuleContext(MiniLangParser.WhilestatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstructura_while" ):
                listener.enterEstructura_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstructura_while" ):
                listener.exitEstructura_while(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)


    class Estructura_ifContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifstat(self):
            return self.getTypedRuleContext(MiniLangParser.IfstatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstructura_if" ):
                listener.enterEstructura_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstructura_if" ):
                listener.exitEstructura_if(self)



    def stat(self):

        localctx = MiniLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.expr()
                self.state = 24
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(MiniLangParser.ID)
                self.state = 27
                self.match(MiniLangParser.T__0)
                self.state = 28
                self.expr()
                self.state = 29
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.ComentarioContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.match(MiniLangParser.COMMENT)
                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 33
                    self.match(MiniLangParser.NEWLINE)


                pass

            elif la_ == 5:
                localctx = MiniLangParser.Estructura_ifContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.ifstat()
                pass

            elif la_ == 6:
                localctx = MiniLangParser.Estructura_whileContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 37
                self.whilestat()
                pass

            elif la_ == 7:
                localctx = MiniLangParser.Declaracion_de_funcionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 38
                self.funcdec()
                pass

            elif la_ == 8:
                localctx = MiniLangParser.Llamada_a_funcionContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 39
                self.funccall()
                pass


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


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MiniLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class MulDiv_STRINGsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.STRING)
            else:
                return self.getToken(MiniLangParser.STRING, i)
        def MUL(self):
            return self.getToken(MiniLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv_STRINGs" ):
                listener.enterMulDiv_STRINGs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv_STRINGs" ):
                listener.exitMulDiv_STRINGs(self)


    class MulDiv_INTsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.INT)
            else:
                return self.getToken(MiniLangParser.INT, i)
        def MUL(self):
            return self.getToken(MiniLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv_INTs" ):
                listener.enterMulDiv_INTs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv_INTs" ):
                listener.exitMulDiv_INTs(self)


    class AddSub_INTsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.INT)
            else:
                return self.getToken(MiniLangParser.INT, i)
        def ADD(self):
            return self.getToken(MiniLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub_INTs" ):
                listener.enterAddSub_INTs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub_INTs" ):
                listener.exitAddSub_INTs(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class AddSub_STRINGsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.STRING)
            else:
                return self.getToken(MiniLangParser.STRING, i)
        def ADD(self):
            return self.getToken(MiniLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub_STRINGs" ):
                listener.enterAddSub_STRINGs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub_STRINGs" ):
                listener.exitAddSub_STRINGs(self)


    class Comparacion_INTsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.INT)
            else:
                return self.getToken(MiniLangParser.INT, i)
        def EQUAL(self):
            return self.getToken(MiniLangParser.EQUAL, 0)
        def NOTEQUAL(self):
            return self.getToken(MiniLangParser.NOTEQUAL, 0)
        def LTHAN(self):
            return self.getToken(MiniLangParser.LTHAN, 0)
        def BTHAN(self):
            return self.getToken(MiniLangParser.BTHAN, 0)
        def BEQ(self):
            return self.getToken(MiniLangParser.BEQ, 0)
        def LEQ(self):
            return self.getToken(MiniLangParser.LEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion_INTs" ):
                listener.enterComparacion_INTs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion_INTs" ):
                listener.exitComparacion_INTs(self)


    class Comparacion_STRINGsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.STRING)
            else:
                return self.getToken(MiniLangParser.STRING, i)
        def EQUAL(self):
            return self.getToken(MiniLangParser.EQUAL, 0)
        def NOTEQUAL(self):
            return self.getToken(MiniLangParser.NOTEQUAL, 0)
        def LTHAN(self):
            return self.getToken(MiniLangParser.LTHAN, 0)
        def BTHAN(self):
            return self.getToken(MiniLangParser.BTHAN, 0)
        def BEQ(self):
            return self.getToken(MiniLangParser.BEQ, 0)
        def LEQ(self):
            return self.getToken(MiniLangParser.LEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion_STRINGs" ):
                listener.enterComparacion_STRINGs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion_STRINGs" ):
                listener.exitComparacion_STRINGs(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self):

        localctx = MiniLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.MulDiv_INTsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(MiniLangParser.INT)
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.match(MiniLangParser.INT)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.AddSub_INTsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(MiniLangParser.INT)
                self.state = 46
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.match(MiniLangParser.INT)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.Comparacion_INTsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(MiniLangParser.INT)
                self.state = 49
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 50
                self.match(MiniLangParser.INT)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.MulDiv_STRINGsContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.match(MiniLangParser.STRING)
                self.state = 52
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 53
                self.match(MiniLangParser.STRING)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.AddSub_STRINGsContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.match(MiniLangParser.STRING)
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.match(MiniLangParser.STRING)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.Comparacion_STRINGsContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.match(MiniLangParser.STRING)
                self.state = 58
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 59
                self.match(MiniLangParser.STRING)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.match(MiniLangParser.INT)
                pass

            elif la_ == 8:
                localctx = MiniLangParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 61
                self.match(MiniLangParser.STRING)
                pass

            elif la_ == 9:
                localctx = MiniLangParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 62
                self.match(MiniLangParser.ID)
                pass

            elif la_ == 10:
                localctx = MiniLangParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 63
                self.match(MiniLangParser.T__1)
                self.state = 64
                self.expr()
                self.state = 65
                self.match(MiniLangParser.T__2)
                pass


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

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def prog(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ProgContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ProgContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_ifstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstat" ):
                listener.enterIfstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstat" ):
                listener.exitIfstat(self)




    def ifstat(self):

        localctx = MiniLangParser.IfstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MiniLangParser.T__3)
            self.state = 70
            self.match(MiniLangParser.T__1)
            self.state = 71
            self.expr()
            self.state = 72
            self.match(MiniLangParser.T__2)
            self.state = 73
            self.match(MiniLangParser.T__4)
            self.state = 74
            self.prog()
            self.state = 75
            self.match(MiniLangParser.T__5)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 76
                self.match(MiniLangParser.T__6)
                self.state = 77
                self.match(MiniLangParser.T__4)
                self.state = 78
                self.prog()
                self.state = 79
                self.match(MiniLangParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def prog(self):
            return self.getTypedRuleContext(MiniLangParser.ProgContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_whilestat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilestat" ):
                listener.enterWhilestat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilestat" ):
                listener.exitWhilestat(self)




    def whilestat(self):

        localctx = MiniLangParser.WhilestatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whilestat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(MiniLangParser.T__7)
            self.state = 84
            self.match(MiniLangParser.T__1)
            self.state = 85
            self.expr()
            self.state = 86
            self.match(MiniLangParser.T__2)
            self.state = 87
            self.match(MiniLangParser.T__4)
            self.state = 88
            self.prog()
            self.state = 89
            self.match(MiniLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def params(self):
            return self.getTypedRuleContext(MiniLangParser.ParamsContext,0)


        def prog(self):
            return self.getTypedRuleContext(MiniLangParser.ProgContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_funcdec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdec" ):
                listener.enterFuncdec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdec" ):
                listener.exitFuncdec(self)




    def funcdec(self):

        localctx = MiniLangParser.FuncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(MiniLangParser.T__8)
            self.state = 92
            self.match(MiniLangParser.ID)
            self.state = 93
            self.match(MiniLangParser.T__1)
            self.state = 94
            self.params()
            self.state = 95
            self.match(MiniLangParser.T__2)
            self.state = 96
            self.match(MiniLangParser.T__4)
            self.state = 97
            self.prog()
            self.state = 98
            self.match(MiniLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(MiniLangParser.ArgsContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_funccall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunccall" ):
                listener.enterFunccall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunccall" ):
                listener.exitFunccall(self)




    def funccall(self):

        localctx = MiniLangParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(MiniLangParser.ID)
            self.state = 101
            self.match(MiniLangParser.T__1)
            self.state = 102
            self.args()
            self.state = 103
            self.match(MiniLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = MiniLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 105
                self.match(MiniLangParser.ID)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 106
                    self.match(MiniLangParser.T__9)
                    self.state = 107
                    self.match(MiniLangParser.ID)
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = MiniLangParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14680068) != 0):
                self.state = 115
                self.expr()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 116
                    self.match(MiniLangParser.T__9)
                    self.state = 117
                    self.expr()
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





