from Symbol import *
from Tokenizer import *
from CExpression import *
from CKeyword import *

def CInterpreterGrammar():
    def interpreter(self):
        return self.first.interpreter() + self.second.interpreter()

    sym=infix('+',40)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() - self.second.interpreter()

    sym=infix('-',40)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() / self.second.interpreter()

    sym=infix('/',60)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() * self.second.interpreter()

    sym=infix('*',60)
    sym.interpreter=interpreter


    def interpreter(self):
        return int(self.first)

    sym=symbol('(literal)')
    sym.interpreter=interpreter

CInterpreterGrammar()