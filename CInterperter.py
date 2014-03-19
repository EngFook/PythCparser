#-------------------------------------------------------------------------------
# Name:        PythCparser
# Purpose:     To parse and interpret C language by using Python.
#
# Author:      Goh Eng Fook
#              Lim Bing Ran
#
# Created:     07/03/2013
# Copyright:   (c) 2013-2014, Goh Eng Fook & Lim Bing Ran
# Licence:     GPLv3
#-------------------------------------------------------------------------------
##"Files imported."                                                           ##
from Tokenizer import *
from CScope import *
import CKeyword
import CExpression
##"Global assignTable."                                                       ##
global assignTable
assignTable={}
##                                                                            ##
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

    def interpreter(self,main=None):
        temp=[]
        a=0
        if main != 'main':
            scope.addScope()
        for index in self.first:
            if index.id == 'case':
                break
            temp=index.interpreter()
            if main == 'function':
                scope.deleteCurrentScope()
                return temp
        if main != 'main':
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

    def assign(self,root):
        AssignYet=False
        number=0
        List=symbolTable[root.first.id].second.first
        if hasattr(self,'std'):
            for temp in List:
                if temp.id == '=':
                    number=int(temp.second.interpreter())
                    temp=temp.first
                    number=number+1
                else:
                    number=number+1
                if temp.first == root.second.first:
                    scope.declareVariable(root,number-1)
                    AssignYet=True
            if not AssignYet:
                scope.declareVariable(root,int(root.second.interpreter()))
        else:
            scope.changeValueOfVariable(root,int(root.second.interpreter()))


    def interpreter(self):
        temp=0
        if self.id == 'enum':
            if self.third != None:
                datatype=self.id +' '+self.first.first
                while temp <self.third.__len__():
                    scope.declareVariable(self.third[temp],None,datatype)
                    temp = temp + 1
        else:
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


    sym=CKeyword.keyword('enum')
    sym.interpreter=interpreter
    sym.assign=assign

    def interpreter(self):
        return scope.findVariable(self.first.first)

    sym=CExpression.infix('.',80)
    sym.interpreter=interpreter


    def interpreter(self):
        self.first.interpreter()

    sym=CKeyword.keyword('typedef')
    sym.interpreter=interpreter

    def interpreter(self,root=None):
        if self.arity != 'function':
            return self.first.interpreter()
        else:
            functionname=scope.GoToVariable(self)
            if not hasattr(self.first,'std'):
                function=scope.findVariable(functionname)
                scope.addScope()
                temp=0
                while temp < function[1].second.__len__():
                    scope.declareVariable(function[1].second[temp],self.second[temp].interpreter())
                    temp=temp+1
                temp=function[1].third.interpreter('function')
                scope.deleteCurrentScope()
                return temp
            if scope.checkVariable(functionname):
                return
            if functionname != 'main':
                temp=root.__len__()-1
                while temp != -1:
                    functiondeclare=scope.GoToVariable(root[temp])
                    if functiondeclare == functionname:
                        token=root[temp]
                        break
                    temp=temp-1
                if token == self or token.second.__len__() != self.second.__len__() or token.first.id != self.first.id :
                    raise SyntaxError('Function has not declared correctly.')
                temp=0
                while temp < self.second.__len__():
                    if self.second[temp].id != token.second[temp].id:
                        raise SyntaxError('Function has not declared correctly.')
                    temp=temp+1
                scope.declareVariable(self,token)
            else:
                self.third.interpreter('main')

    sym=CExpression.infix('(',50)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter()

    sym=CKeyword.keyword('return')
    sym.interpreter=interpreter
################################################################################
################################################################################
##"Call C InterpreterGrammar()."                                              ##
CInterpreterGrammar()
##                                                                            ##