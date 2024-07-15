# Generated from MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#prog.
    def enterProg(self, ctx:MiniLangParser.ProgContext):
        pass

    # Exit a parse tree produced by MiniLangParser#prog.
    def exitProg(self, ctx:MiniLangParser.ProgContext):
        pass


    # Enter a parse tree produced by MiniLangParser#printExpr.
    def enterPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#printExpr.
    def exitPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assign.
    def enterAssign(self, ctx:MiniLangParser.AssignContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assign.
    def exitAssign(self, ctx:MiniLangParser.AssignContext):
        pass


    # Enter a parse tree produced by MiniLangParser#blank.
    def enterBlank(self, ctx:MiniLangParser.BlankContext):
        pass

    # Exit a parse tree produced by MiniLangParser#blank.
    def exitBlank(self, ctx:MiniLangParser.BlankContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comentario.
    def enterComentario(self, ctx:MiniLangParser.ComentarioContext):
        pass

    # Exit a parse tree produced by MiniLangParser#comentario.
    def exitComentario(self, ctx:MiniLangParser.ComentarioContext):
        pass


    # Enter a parse tree produced by MiniLangParser#estructura_if.
    def enterEstructura_if(self, ctx:MiniLangParser.Estructura_ifContext):
        pass

    # Exit a parse tree produced by MiniLangParser#estructura_if.
    def exitEstructura_if(self, ctx:MiniLangParser.Estructura_ifContext):
        pass


    # Enter a parse tree produced by MiniLangParser#estructura_while.
    def enterEstructura_while(self, ctx:MiniLangParser.Estructura_whileContext):
        pass

    # Exit a parse tree produced by MiniLangParser#estructura_while.
    def exitEstructura_while(self, ctx:MiniLangParser.Estructura_whileContext):
        pass


    # Enter a parse tree produced by MiniLangParser#declaracion_de_funcion.
    def enterDeclaracion_de_funcion(self, ctx:MiniLangParser.Declaracion_de_funcionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#declaracion_de_funcion.
    def exitDeclaracion_de_funcion(self, ctx:MiniLangParser.Declaracion_de_funcionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#llamada_a_funcion.
    def enterLlamada_a_funcion(self, ctx:MiniLangParser.Llamada_a_funcionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#llamada_a_funcion.
    def exitLlamada_a_funcion(self, ctx:MiniLangParser.Llamada_a_funcionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MulDiv_INTs.
    def enterMulDiv_INTs(self, ctx:MiniLangParser.MulDiv_INTsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MulDiv_INTs.
    def exitMulDiv_INTs(self, ctx:MiniLangParser.MulDiv_INTsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#AddSub_INTs.
    def enterAddSub_INTs(self, ctx:MiniLangParser.AddSub_INTsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#AddSub_INTs.
    def exitAddSub_INTs(self, ctx:MiniLangParser.AddSub_INTsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comparacion_INTs.
    def enterComparacion_INTs(self, ctx:MiniLangParser.Comparacion_INTsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#comparacion_INTs.
    def exitComparacion_INTs(self, ctx:MiniLangParser.Comparacion_INTsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MulDiv_STRINGs.
    def enterMulDiv_STRINGs(self, ctx:MiniLangParser.MulDiv_STRINGsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MulDiv_STRINGs.
    def exitMulDiv_STRINGs(self, ctx:MiniLangParser.MulDiv_STRINGsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#AddSub_STRINGs.
    def enterAddSub_STRINGs(self, ctx:MiniLangParser.AddSub_STRINGsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#AddSub_STRINGs.
    def exitAddSub_STRINGs(self, ctx:MiniLangParser.AddSub_STRINGsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comparacion_STRINGs.
    def enterComparacion_STRINGs(self, ctx:MiniLangParser.Comparacion_STRINGsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#comparacion_STRINGs.
    def exitComparacion_STRINGs(self, ctx:MiniLangParser.Comparacion_STRINGsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#int.
    def enterInt(self, ctx:MiniLangParser.IntContext):
        pass

    # Exit a parse tree produced by MiniLangParser#int.
    def exitInt(self, ctx:MiniLangParser.IntContext):
        pass


    # Enter a parse tree produced by MiniLangParser#string.
    def enterString(self, ctx:MiniLangParser.StringContext):
        pass

    # Exit a parse tree produced by MiniLangParser#string.
    def exitString(self, ctx:MiniLangParser.StringContext):
        pass


    # Enter a parse tree produced by MiniLangParser#id.
    def enterId(self, ctx:MiniLangParser.IdContext):
        pass

    # Exit a parse tree produced by MiniLangParser#id.
    def exitId(self, ctx:MiniLangParser.IdContext):
        pass


    # Enter a parse tree produced by MiniLangParser#parens.
    def enterParens(self, ctx:MiniLangParser.ParensContext):
        pass

    # Exit a parse tree produced by MiniLangParser#parens.
    def exitParens(self, ctx:MiniLangParser.ParensContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ifstat.
    def enterIfstat(self, ctx:MiniLangParser.IfstatContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ifstat.
    def exitIfstat(self, ctx:MiniLangParser.IfstatContext):
        pass


    # Enter a parse tree produced by MiniLangParser#whilestat.
    def enterWhilestat(self, ctx:MiniLangParser.WhilestatContext):
        pass

    # Exit a parse tree produced by MiniLangParser#whilestat.
    def exitWhilestat(self, ctx:MiniLangParser.WhilestatContext):
        pass


    # Enter a parse tree produced by MiniLangParser#funcdec.
    def enterFuncdec(self, ctx:MiniLangParser.FuncdecContext):
        pass

    # Exit a parse tree produced by MiniLangParser#funcdec.
    def exitFuncdec(self, ctx:MiniLangParser.FuncdecContext):
        pass


    # Enter a parse tree produced by MiniLangParser#funccall.
    def enterFunccall(self, ctx:MiniLangParser.FunccallContext):
        pass

    # Exit a parse tree produced by MiniLangParser#funccall.
    def exitFunccall(self, ctx:MiniLangParser.FunccallContext):
        pass


    # Enter a parse tree produced by MiniLangParser#params.
    def enterParams(self, ctx:MiniLangParser.ParamsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#params.
    def exitParams(self, ctx:MiniLangParser.ParamsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#args.
    def enterArgs(self, ctx:MiniLangParser.ArgsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#args.
    def exitArgs(self, ctx:MiniLangParser.ArgsContext):
        pass



del MiniLangParser