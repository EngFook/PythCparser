"""
    Have to modify. 3/13/2014
                                """
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
        temp=scope.findVariable(self.first)
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
        scope.findVariable(self.first.first)
        scope.changeValueOfVariable(self,int(temp1.interpreter()))
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
        scope.findVariable(self.first.first)
        scope.changeValueOfVariable(self,int(temp1.interpreter()))
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
        return "The address of {0} point to {2}".format(self.first.interpreter(),self.first.interpreter())

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
        scope.addScope()
        for index in self.first:
            if index.id == 'case':
                break
            index.interpreter()
        scope.deleteCurrentScope()

    sym=CKeyword.keyword('{')
    sym.interpreter=interpreter


    def interpreter(self):
        if hasattr (self.first,'std'):
            self.first.assign(self)
            return "has assigned value to the object"
        elif self.first.id == '.':
            temp=self.first.interpreter()
        else:
            temp=scope.findVariable(self.first.first)
        temp[0].assign(self.first,self)
        return "has changed value to the object"

    sym=CExpression.infix('=',10)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.__class__() == []:
            length=self.first.__len__()
            temp=0
            temp1=self.first
            while temp < length:
                self.first=temp1[temp]
                scope.declareVariable(self)
                temp=temp+1
        else:
            scope.declareVariable(self)

    def assign(self,root):
        if hasattr(self,'std'):
            scope.declareVariable(root,int(root.second.interpreter()))
        else:
            scope.changeValueOfVariable(root,int(root.second.interpreter()))

    sym=CKeyword.keyword('int')
    sym.interpreter=interpreter
    sym.assign=assign

    def assign(self,root):
        if hasattr(self,'std'):
            scope.declareVariable(root,root.second.interpreter())
        else:
            scope.changeValueOfVariable(root,root.second.interpreter())

    sym=CKeyword.keyword('double')
    sym.interpreter=interpreter
    sym.assign=assign

    sym=CKeyword.keyword('floating')
    sym.interpreter=interpreter

    sym=CKeyword.keyword('char')
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first.interpreter() :
            if self.second != None:
                self.second.interpreter()
        if self.third != None :
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
            self.first.interpreter()

    sym=CKeyword.keyword('do')
    sym.interpreter=interpreter

    def interpreter(self):
        if self.first != None :
            scope.findVariable(self.first.first.first)
            self.first.interpreter()
        temp=0
        while self.second.interpreter():
            if self.third != None :
                self.third.interpreter()
            if self.four != None :
                self.four.interpreter()
            temp=temp+1
            if temp > 300 :
                raise SyntaxError('Infinity loop')

    sym=CKeyword.keyword('for')
    sym.interpreter=interpreter

    def interpreter(self):
        for case in self.second.address.keys():
            if self.first.interpreter() == int(case):
                index=self.second.address[case][0]
                while self.second.address[case][1].first[index+1].id != 'case':
                    if hasattr(self.second.address[case][1].first[index+1],'std'):
                        self.second.address[case][1].first[index+1].interpreter()
                    else:
                        self.second.address[case][1].first[index+1].interpreter()
                        if self.second.back[case] != None:
                            temp1=self.second.back[case][1]
                            while temp1 < self.second.first.__len__():
                                temp2=self.second.first
                                if temp2[temp1].id == 'default' or temp2[temp1].id == 'case':
                                    return
                                self.second.first[temp1].interpreter()
                                temp1 = temp1 + 1
                    index = index + 1
                    if self.second.address[case][1].first[index+1].id == 'default':
                        return
                return
        for default in self.second.first:
            if default.id =='default':
                default.interpreter(self.second.first)


    sym=CKeyword.keyword('switch')
    sym.interpreter=interpreter

    def interpreter(self,list):
        temp=list.index(self)+1
        while   temp < list.__len__():
            list[temp].interpreter()
            temp=temp+1
        return

    sym=CKeyword.keyword('default')
    sym.interpreter=interpreter

    def interpreter(self,list):
        temp=list.index(self)+1
        while   temp < list.__len__():
            list[temp].interpreter()
            temp=temp+1
        return

    sym=CKeyword.keyword('default')
    sym.interpreter=interpreter

    def interpreter(self):
        pass

    sym=CKeyword.keyword('#define')
    sym.interpreter=interpreter

    def assign(self,root):
        scope.changeValueOfVariableOfStruct(root,root.second.interpreter())


    def interpreter(self):
        List={}
        temp=0
        if self.id == 'struct':
            if self.third != None :
                temp2=0
                datatype=self.id +' '+self.first.first
                while temp2 < self.third.__len__():
                    while temp < self.second.first.__len__():
                        Class=self.second.first[temp].id
                        Variable=self.second.first[temp].first.first
                        temp=temp+1
                        List[Variable]=(symbolTable[Class],None)
                    scope.declareVariable(self.third[temp2],List,datatype)
                    temp2=temp2+1
        else:
            while temp < self.second.first.__len__():
                Class=self.second.first[temp].id
                Variable=self.second.first[temp].first.first
                temp=temp+1
                List[Variable]=(symbolTable[Class],None)
            scope.declareVariable(self,List)

    sym=CKeyword.keyword('struct')
    sym.interpreter=interpreter
    sym.assign=assign

    def interpreter(self):
        return scope.findVariable(self.first.first)

    sym=CExpression.infix('.',80)
    sym.interpreter=interpreter

CInterpreterGrammar()