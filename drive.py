import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from VisitoyInterp import VisitorInterp
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    print(parser)
    tree = parser.compileParseTreePattern()
    print(tree)

if __name__ == '__main__':
    main(sys.argv)