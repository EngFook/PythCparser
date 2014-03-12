from Symbol import *
from Tokenizer import *
from CScope import *
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
        temp=Scope.find_variable(self.first,self.first)
        if temp[0] == 'int':
            temp1=self.first.interpreter()/self.second.interpreter()
            return temp1
        else:
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
        return float(self.first)

    sym=symbol('(literal)')
    sym.interpreter=interpreter


    def interpreter(self):
        temp=Scope.find_variable(self,self)
        if temp[1] != None:
            return int(temp[1])
        else: return None

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
        temp2=Scope.find_variable(self.first,self.first)
        Scope.add_variable(self.first,temp2,temp1)
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
        temp2=Scope.find_variable(self.first,self.first)
        Scope.add_variable(self.first,temp2,temp1)
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
        if hasattr (self.first,'std'):
            Scope.add_variable(self.first,self.first,self.second)
            return "has assigned value to the object"
        else:
            temp=Scope.find_variable(self.first,self.first)
            Scope.add_variable(self.first,temp,self.second)
            return "has assigned value to the object"

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
        if self.first.interpreter().is_integer() and self.second.interpreter().is_integer():
            return int(self.first.interpreter()) >> int(self.second.interpreter())
        else:
            raise SyntaxError('value entered is not identifier')

    sym=CExpression.infix('>>',15)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter().is_integer() and self.second.interpreter().is_integer():
            return int(self.first.interpreter()) << int(self.second.interpreter())
        else:
            raise SyntaxError('value entered is not identifier')

    sym=CExpression.infix('<<',15)
    sym.interpreter=interpreter


    def interpreter(self):
        if self.arity == 'binary':
            if self.first.interpreter().is_integer() and self.second.interpreter().is_integer():
                return int(self.first.interpreter()) & int(self.second.interpreter())
            else:
                raise SyntaxError('value entered is not identifier')
        else:
            return "this is the addresss of {0}".format(self.first.interpreter())
    sym=CExpression.infix('&',60)
    sym.interpreter=interpreter

    def interpreter(self):
        return not(self.first.interpreter())

    sym=CExpression.prefix('!',90)
    sym.interpreter=interpreter

    def interpreter(self):
        return ~int(self.first.interpreter())

    sym=CExpression.prefix('~',90)
    sym.interpreter=interpreter

    def interpreter(self):
        temp=[]
        a=0
        Scope.add_scope(self)
        for index in self.first:
            temp.append(index.interpreter())
        Scope.delete_current_scope(self)
        temp1=self.first.__len__()
        while a < temp1:
            self.first[a].interpreter()
            a=a+1
        return temp

    sym=CKeyword.keyword('{')
    sym.interpreter=interpreter

    def interpreter(self):
        temp=Scope.check_variable(self.first,self.first)
        if temp == None :
            Scope.add_variable(self,self.first,None)
        elif temp[0] == self.id:
            Scope.add_variable(self,self.first,None)
        else:
            raise SyntaxError('Cannot declare twice')

    sym=CKeyword.keyword('int')
    sym.interpreter=interpreter

    sym=CKeyword.keyword('double')
    sym.interpreter=interpreter

    sym=CKeyword.keyword('floating')
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() :
            if self.second != None:
                self.second.interpreter()
        elif self.third != None :
            temp=self.third
            if temp.first != None:
                temp.first.interpreter()
        else :
            return

    sym=CKeyword.keyword('if')
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first != None :
            temp=self.first.interpreter()
        return

    sym=CKeyword.keyword('else')
    sym.interpreter=interpreter

    def interpreter(self):
        temp=0
        while self.first.interpreter():
            temp=temp+1
            if temp > 300 :
                raise SyntaxError('Infinity loop')
            if self.second != None:
                self.second.interpreter()

    sym=CKeyword.keyword('while')
    sym.interpreter=interpreter

    def interpreter(self):
        temp=0
        self.first.interpreter()
        while self.second.first.interpreter():
            temp=temp+1
            if temp > 300 :
                raise SyntaxError('Infinity loop')
            if self.first != None:
                self.first.interpreter()

    sym=CKeyword.keyword('do')
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first != None :
            Scope.find_variable(self.first.first,self.first.first)
            self.first.interpreter()
        while self.second.interpreter():
            if self.third != None :
                self.third.interpreter()

    sym=CKeyword.keyword('for')
    sym.interpreter=interpreter

CInterpreterGrammar()