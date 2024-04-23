import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from ExprVisitor import ExprVisitor

class VisitorInterp(ExprVisitor):
    def __init__(self):
        self.variables={}
    def visitExpr(self, ctx: ExprParser.ExprContext):
        for child in ctx.getChildren():
            child