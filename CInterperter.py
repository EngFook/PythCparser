from Symbol import *
from Tokenizer import *
from CExpression import *
from CKeyword import *

def CInterpreterGrammar():
    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() + self.second.interpreter()
        else:
            return  self.first.interpreter()

    sym=infix('+',40)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() - self.second.interpreter()
        else:
            return - self.first.interpreter()

    sym=infix('-',40)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() / self.second.interpreter()

    sym=infix('/',60)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() * self.second.interpreter()
        else:
            return "this is the pointer of {0}".format(self.first.interpreter())
    sym=infix('*',60)
    sym.interpreter=interpreter

    def interpreter(self):
        return int(self.first)

    sym=symbol('(literal)')
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first

    sym=symbol('(identifier)')
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter()

    sym=infix('(',100)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.arity == 'postunary':
            return self.first.interpreter()
        else:
            return self.first.interpreter()-1

    sym=prefix('--',90)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.arity == 'postunary':
            return self.first.interpreter()
        else:
            return self.first.interpreter()+1

    sym=prefix('++',90)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() ** self.second.interpreter()

    sym=infix('**',70)
    sym.interpreter=interpreter

    def interpreter(self):
        self.first.interpreter=self.second.interpreter
        return self

    sym=infix('=',10)
    sym.interpreter=interpreter

    def interpreter(self):
        return "The address of {0} point to {2}".format(self.first.interpreter(),self.first.interpreter())

    sym=infix('.',80)
    sym.interpreter=interpreter
    sym=infix('->',80)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() == self.second.interpreter() :
            return True
        else: False

    sym=infix('==',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() < self.second.interpreter() :
            return True
        else: False

    sym=infix('<',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() > self.second.interpreter() :
            return True
        else: False

    sym=infix('>',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() < self.second.interpreter():
            return True
        if self.first.interpreter() == self.second.interpreter() :
            return True
        return False

    sym=infix('>=',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() > self.second.interpreter() :
                return True
        if self.first.interpreter() == self.second.interpreter() :
                return True
        return False

    sym=infix('>=',10)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() >> self.second.interpreter()

    sym=infix('>>',15)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() << self.second.interpreter()

    sym=infix('<<',15)
    sym.interpreter=interpreter


    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() & self.second.interpreter()
        else:
            return "this is the addresss of {0}".format(self.first.interpreter())
    sym=infix('&',60)
    sym.interpreter=interpreter

    def interpreter(self):
        return not(self.first.interpreter())

    sym=prefix('!',90)
    sym.interpreter=interpreter

    def interpreter(self):
        return ~(self.first.interpreter())

    sym=prefix('~',90)
    sym.interpreter=interpreter

CInterpreterGrammar()