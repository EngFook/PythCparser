from Symbol import *
from Tokenizer import *
import CKeyword
import CExpression

global assignTable
assignTable={}

def CInterpreterGrammar():
    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() + self.second.interpreter()
        else:
            return  self.first.interpreter()

    sym=CExpression.infix('+',40)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() - self.second.interpreter()
        else:
            return - self.first.interpreter()

    sym=CExpression.infix('-',40)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() / self.second.interpreter()

    sym=CExpression.infix('/',60)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() * self.second.interpreter()
        else:
            return "this is the pointer of {0}".format(self.first.interpreter())
    sym=CExpression.infix('*',60)
    sym.interpreter=interpreter

    def interpreter(self):
        return int(self.first)

    sym=symbol('(literal)')
    sym.interpreter=interpreter


    def interpreter(self):
        global assignTable
        if self.first in assignTable:
            return assignTable[self.first].interpreter()
        else:
            raise SyntaxError('{0} have not assigned'.format(self.first))

    sym=symbol('(identifier)')
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter()

    sym=CExpression.infix('(',50)
    sym.interpreter=interpreter

    def interpreter(self):
        global assignTable
        if self.first.id == '(literal)':
            raise SyntaxError('{0} is not identifier'.format(self))
        temp=self.first.interpreter()
        temp1=createLiteral(self.first.interpreter()-1)
        assignTable[self.first.first].interpreter=temp1.interpreter
        if self.arity == 'postunary':
            return temp
        else:
            return temp1.interpreter()

    sym=CExpression.prefix('--',90)
    sym.interpreter=interpreter

    def interpreter(self):
        global assignTable
        if self.first.id == '(literal)':
            raise SyntaxError('{0} is not identifier'.format(self))
        temp=self.first.interpreter()
        temp1=createLiteral(self.first.interpreter()+1)
        assignTable[self.first.first].interpreter=temp1.interpreter
        if self.arity == 'postunary':
            return temp
        else:
            return temp1.interpreter()
    sym=CExpression.prefix('++',90)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() ** self.second.interpreter()

    sym=CExpression.infix('**',70)
    sym.interpreter=interpreter

    def interpreter(self):
        global assignTable
        self.first.interpreter=self.second.interpreter
        return self

    sym=CExpression.infix('=',10)
    sym.interpreter=interpreter

    def interpreter(self):
        return "The address of {0} point to {2}".format(self.first.interpreter(),self.first.interpreter())

    sym=CExpression.infix('.',80)
    sym.interpreter=interpreter
    sym=CExpression.infix('->',80)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() == self.second.interpreter() :
            return True
        else: False

    sym=CExpression.infix('==',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() < self.second.interpreter() :
            return True
        else: False

    sym=CExpression.infix('<',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() > self.second.interpreter() :
            return True
        else: False

    sym=CExpression.infix('>',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() < self.second.interpreter():
            return True
        if self.first.interpreter() == self.second.interpreter() :
            return True
        return False

    sym=CExpression.infix('>=',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() > self.second.interpreter() :
                return True
        if self.first.interpreter() == self.second.interpreter() :
                return True
        return False

    sym=CExpression.infix('>=',10)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() >> self.second.interpreter()

    sym=CExpression.infix('>>',15)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() << self.second.interpreter()

    sym=CExpression.infix('<<',15)
    sym.interpreter=interpreter


    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() & self.second.interpreter()
        else:
            return "this is the addresss of {0}".format(self.first.interpreter())
    sym=CExpression.infix('&',60)
    sym.interpreter=interpreter

    def interpreter(self):
        return not(self.first.interpreter())

    sym=CExpression.prefix('!',90)
    sym.interpreter=interpreter

    def interpreter(self):
        return ~(self.first.interpreter())

    sym=CExpression.prefix('~',90)
    sym.interpreter=interpreter

    def interpreter(self):
        return temp

    sym=CKeyword.keyword('{')
    sym.interpreter=interpreter

    def interpreter(self):
        temp=self.first.first.interpreter()
        return temp

    sym=CKeyword.keyword('int')
    sym.interpreter=interpreter
    sym=CKeyword.keyword('double')
    sym.interpreter=interpreter

    def interpreter(self):
        temp=self.first.interpreter()
        if self.first.interpreter() >= 1:
            self.second.interpreter()
        elif self.third != None :
            temp=self.third
            temp.first.interpreter()
        else :
            return

    sym=CKeyword.keyword('if')
    sym.interpreter=interpreter

    def interpreter(self):
        temp=self.first.interpreter()
        return

    sym=CKeyword.keyword('else')
    sym.interpreter=interpreter

CInterpreterGrammar()