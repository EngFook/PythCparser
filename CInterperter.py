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
##"Interpreter the array root[i],i=1,2,3,...                                  ##
def Runinterpreter(self):
    index=0
    List=[]
    while index < self.__len__():
        if self[index].arity == 'function':
            if self[index].third != None:
                temp=0
                while temp < List.__len__():
                    if self[index].first.first.first == List[temp]:
                        raise SyntaxError('There are two same function.')
                    temp=temp+1
                List.append(self[index].first.first.first)
            self[index].interpreter(self)
        else:
            self[index].interpreter()
        index = index + 1
##

def FunctionForPrintf(self,content):
    temp = 0 ;
    value=[]
    ForPrint=''
    if hasattr(content,'type'):
        if content.type=='string':
            ForPrint=ForPrint+'"'+content.first+'"'
    else:
        length=content.__len__()
        while temp < length :
            if hasattr (content[temp],'type'):
                if value != []:
                    PrintMany(ForPrint,value)
                    value=[]
                    ForPrint=''
                    ForPrint=ForPrint+'"'+content.first+'"'
                if content[temp].type=='string':
                    ForPrint=ForPrint+'"'+content[temp].first+'"'
                else:
                    if content[temp].id == "[":
                        arrayList=scope.findVariable(content[temp].first.first)[1]
                        temp1=arrayList[int(content[temp].second.interpreter())]
                        if temp1==None:
                            temp1=0
                        value.append(temp1)
                    else:
                        if hasattr ( content[temp],'type'):
                            value.append(scope.findVariable(content[temp].first)[1])
                        else:
                            value.append(int(content[temp].interpreter()))
            else:
##                if content.isidentifier():
##                    ForPrint=ForPrint+'"'+content.first+'"
                if content[temp].id == "[":
                    arrayList=scope.findVariable(content[temp].first.first)[1]
                    temp1=arrayList[int(content[temp].second.interpreter())]
                    if temp1==None:
                        temp1=0
                    value.append(temp1)
                else:
                    if hasattr ( content[temp],'type'):
                        value.append(scope.findVariable(content[temp].first)[1])
                    else:
                        value.append(content[temp].interpreter())

            temp=temp+1
    PrintMany(ForPrint,value)
    ForPrint=' '
    value=[]

def PrintMany(ForPrint,value):
    if value == []:
        print('##'+ForPrint)
    elif value.__len__() == 1:
        print('##'+ForPrint % value[0])
    elif value.__len__()==2:
        print('##'+ ForPrint % (value[0],value[1]))
    elif value.__len__()==3:
        print('##'+ ForPrint % (value[0],value[1],value[2]))

def FunctionForScanf(self,content):
    temp = 0 ;
    value=[]
    ForPrint=''
    length=content.__len__()
    while temp < length :
        if content[temp].id=='(identifier)' or content[temp].id== '&':
            if hasattr(content[temp].first,'startswith'):
                    if content[temp].first.startswith('%d'):
                        pass
                    elif content[temp].first.startswith('%s'):
                        pass
                    else:
                        if content[temp].id == '&':
                            content[temp]=content[temp].first
                        elif temp1.startswith('%s'):
                            content=input("{0}: ".format(content[temp]))
                            FunctionForPrintf(self,content)
                        else:
                            raise SyntaxError ('Expected "&" reference to the address of {0}.'.format(content[temp]))
            else:
                if content[temp].id == '&':
                    content[temp]=content[temp].first
                else:
                    raise SyntaxError ('Expected "&" reference to the address of {0}.'.format(content[temp]))
        if content[temp].id == '[':
            temp1=content[temp].first.first
        else:
            temp1=content[temp].first
        if temp1.startswith('%d'):
            pass
        elif temp1.startswith('%s'):
            pass
        else:
            if content[temp].id == '[':
                key_in=input("{0} [ {1} ]: ".format(content[temp].first,content[temp].second.interpreter()))
                key_in=float(key_in)
                scope.changeValueOfVariable(content[temp],key_in)
            else:
                key_in=input("{0}: ".format(content[temp]))
                if  hasattr(key_in,'startswith'):
                    if key_in.isidentifier():
                        raise SyntaxError ('Expected an integer value.')
                key_in=float(key_in)
                scope.changeValueOfVariable(content[temp],key_in)
        temp=temp+1
                                                         ##
def CInterpreterGrammar():

    def interpreter(self):
        return self

    sym=CKeyword.keyword('break')
    sym.interpreter=interpreter

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
        return self.first.interpreter() % self.second.interpreter()

    sym=CExpression.infix('%',60)
    sym.interpreter=interpreter

    def interpreter(self):
        return self.first.interpreter() and self.second.interpreter()

    sym=CExpression.infix('&&',5)
    sym.interpreter=interpreter

    def interpreter(self):
        if self.arity == 'binary':
            return self.first.interpreter() * self.second.interpreter()
        else:
            return "this is the pointer of {0}".format(self.first.interpreter())
    sym=CExpression.infix('*',60)
    sym.interpreter=interpreter

    def interpreter(self):
        temp=scope.findVariable(self.first.first)
        if self.second != None:
            if temp[1][int(self.second.interpreter())] == None:
                return 0
            return temp[1][int(self.second.interpreter())]
        else:
            return temp[1]

    sym=CExpression.infix('[',50)
    sym.interpreter=interpreter

    def interpreter(self):
        return float(self.first)

    sym=symbol('(literal)')
    sym.interpreter=interpreter

    def interpreter(self):
        temp=scope.findVariable(self.first)
        if temp[1] != None:
            if temp[1].__class__()=={}:
                return temp[1]
            else:
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
        if self.first.interpreter() != self.second.interpreter() :
            return True
        else: False

    sym=CExpression.infix('!=',10)
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

    sym=CExpression.infix('<=',10)
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
            return self.first.interpreter()
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

    def interpreter(self,main=None,ReturnDataType=None):
        temp=[]
        hasreturn=False
        a=0
        if main != 'main':
            scope.addScope()
        for index in self.first:
            if index.id == 'case':
                break
            if index.id == 'return':
                hasreturn=True
                temp=index.interpreter(ReturnDataType)
            elif index.id == 'break':
                return index
            else:
                temp=index.interpreter()
            if hasattr (temp,'id'):
                if temp.id == 'break':
                    return temp
        if main == 'function':
            scope.deleteCurrentScope()
            if ReturnDataType != 'void' and not hasreturn:
                raise SyntaxError('Should return somthing')
            else:
                return temp
        if main != 'main':
            scope.deleteCurrentScope()
            if main == 'function':
                if ReturnDataType != 'void' and not hasreturn:
                    raise SyntaxError('Should return something')
                else:
                    return temp
        return temp

    sym=CKeyword.keyword('{')
    sym.interpreter=interpreter


    def interpreter(self):
        if hasattr (self.first,'std'):
            self.first.assign(self)
            return "has assigned value to the object"
        elif self.first.id == '.':
            temp=self.first.interpreter()
        elif self.first.id == '[':
            index=int(self.first.second.interpreter())
            temp=scope.findVariable(self.first.first.first)
            if temp[1].__len__() <=index:
                raise SyntaxError('array size not correct')
        else:
            temp=scope.findVariable(self.first.first)
        temp[0][0].assign(self.first,self)
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
            if self.first.id == '[':
                if self.first.second == None :
                    raise SyntaxError('Array size missing')
            scope.declareVariable(self)

    def assign(self,root):
        temp=0
        if hasattr(self,'std'):
            if self.first.__class__() == []:
                while temp<self.first.__len__():
                    if root.second[temp]!=None:
                        temp1=root.second[temp].interpreter()
                        if temp1 > (0xffffffff-1)/2:
                            temp1=(0xffffffff-1)/2
                        elif temp1 < -1*(0xffffffff+1)/2:
                            temp1=-1*(0xffffffff+1)/2
                        scope.declareVariable(root,int(temp1),None,temp)
                    else:
                        scope.declareVariable(root,0,None,temp)
                    temp=temp+1
            else:
                temp1=root.second.interpreter()
                if temp1 > (0xffffffff-1)/2:
                    temp1=(0xffffffff-1)/2
                elif temp1 < -1*(0xffffffff+1)/2:
                    temp1=-1*(0xffffffff+1)/2
                scope.declareVariable(root,int(temp1))
        else:
            if root.second.id == '.':
                mainvariable=scope.GoToVariable(root.second)
                temp = scope.findValueOfVariableOfStruct(root.second,mainvariable)
                if temp > (0xffffffff-1)/2:
                    temp=(0xffffffff-1)/2
                elif temp < -1*(0xffffffff+1)/2:
                    temp=-1*(0xffffffff+1)/2
                scope.changeValueOfVariable(root,int(temp))
            else:
                temp=root.second.interpreter()
                if temp > (0xffffffff-1)/2:
                    temp=(0xffffffff-1)/2
                elif temp < -1*(0xffffffff+1)/2:
                    temp=-1*(0xffffffff+1)/2
                scope.changeValueOfVariable(root,int(temp))

    sym=CKeyword.keyword('int')
    sym.interpreter=interpreter
    sym.assign=assign

    def assign(self,root):
        temp=0
        if hasattr(self,'std'):
            if self.first.__class__() == []:
                while temp<self.first.__len__():
                    if root.second[temp]!=None:
                        scope.declareVariable(root,root.second[temp].interpreter(),None,temp)
                    else:
                        scope.declareVariable(root,0,None,temp)
                    temp=temp+1
            else:
                scope.declareVariable(root,root.second.interpreter())
        else:
            if root.second.id == '.':
                mainvariable=scope.GoToVariable(root.second)
                temp = scope.findValueOfVariableOfStruct(root.second,mainvariable)
                scope.changeValueOfVariable(root,temp)
            else:
                scope.changeValueOfVariable(root,root.second.interpreter())

    sym=CKeyword.keyword('double')
    sym.interpreter=interpreter
    sym.assign=assign

    sym=CKeyword.keyword('float')
    sym.interpreter=interpreter
    sym.assign=assign

    sym=CKeyword.keyword('char')
    sym.interpreter=interpreter
    sym.assign=assign

    def interpreter(self):
        if self.first.interpreter() :
            if self.second != None:
                return self.second.interpreter()
        if self.third != None :
            temp=self.third
            if temp.first != None:
                return temp.first.interpreter()
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
                temp1=self.second.interpreter()
                if hasattr (temp1,'id'):
                    if temp1.id == 'break':
                        break

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
            if self.four != None :
                self.four.interpreter()
            if self.third != None :
                self.third.interpreter()
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

    def interpreter(self):
        pass

    sym=CKeyword.keyword('#define')
    sym.interpreter=interpreter

    def assign(self,root):
        variable=scope.GoToVariable(root)
        biggest=scope.findVariable(variable)
        contentofvariable=root.first.second.first
        scope.changeValueOfVariableOfStruct(variable,biggest,contentofvariable,root.second.interpreter())

    def findthecontent(self,Class):
        List={}
        index=0
        temp=symbolTable[Class].second.first
        while index < temp.__len__ () :
            Variable=temp[index].first.first
            if symbolTable[temp[index].id].second != None:
                temp2=self.findthecontent(temp[index].id)
                List[Variable]=(symbolTable[temp[index].id],temp2)
            else:
                List[Variable]=(symbolTable[temp[index].id],None)
            index =index + 1
        return List


    def interpreter(self,root=None):
        List={}
        temp=0
        if root != None :
            self.third =root.second
        if self.id == 'struct':
            if self.third != None :
                temp2=0
                while temp2 < self.third.__len__():
                    if self.first == None :
                        if root.id == 'typedef':
                            datatype=self.third[temp2].first
                        else:
                            datatype="NamELesS"+' '+self.third[temp2].first
                    else:
                        datatype=self.id +' '+self.first.first
                    while temp < self.second.first.__len__():
                        Class=self.second.first[temp].id
                        Variable=self.second.first[temp].first.first
                        temp=temp+1
                        List[Variable]=(symbolTable[Class],None)
                    scope.declareVariable(self.third[temp2],List,datatype)
                    temp2=temp2+1
        else:
            temp3=0
            store=[]
            while temp < self.second.first.__len__():
                Class=self.second.first[temp].id
                Variable=self.second.first[temp].first.first
                temp=temp+1
                Checkstruct=symbolTable[Class].second
                if Checkstruct != None:
                    value=self.findthecontent(Class)
                    List[Variable]=(symbolTable[Class],value)
                else:
                    List[Variable]=(symbolTable[Class],None)
            scope.declareVariable(self,List)

    sym=CKeyword.keyword('struct')
    sym.interpreter=interpreter
    sym.assign=assign
    sym.findthecontent=findthecontent

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
        temp=Scope.GoToVariable(None,self)
        return scope.findVariable(temp)

    sym=CExpression.infix('.',80)
    sym.interpreter=interpreter


    def interpreter(self):
        self.first.interpreter(self)

    sym=CKeyword.keyword('typedef')
    sym.interpreter=interpreter

    def interpreter(self,root=None):
        if self.arity != 'function':
            return self.first.interpreter()
        else:
            functionname=scope.GoToVariable(self)
            if not hasattr(self.first,'std'):
                function=scope.findVariable(functionname)
                if functionname == "scanf":
                    FunctionForScanf(function,self.second)
                    return
                if functionname == "printf":
                    FunctionForPrintf(function,self.second)
                    return
                scope.addScope()
                temp=0
                if function[1].second.__class__() == []:
                    while temp < function[1].second.__len__():
                        scope.declareVariable(function[1].second[temp],self.second[temp].interpreter())
                        temp=temp+1
                else:
                    scope.declareVariable(function[1].second,self.second.interpreter())
                temp=function[1].third.interpreter('function',function[1].first.id)
                scope.deleteCurrentScope()
                return temp
            if scope.checkVariable(functionname):
                temp=scope.findVariable(functionname)[1]
                if self.third == None :
                    if temp.first.id != self.first.id :
                        raise SyntaxError("Wrong Retrun Datatype of Redeclaration")
                    elif temp.second.__class__() != []:
                        if temp.second != None:
                            if temp.second.id != self.second.id:
                                raise SyntaxError("Argument of Redeclaration not same.")
                    elif temp.second.__class__() == []:
                        if self.second.__class__() != []:
                            raise SyntaxError("Number argument of Redeclaration not same.")
                        if temp.second.__len__()!= self.second.__len__():
                            raise SyntaxError("Number argument of Redeclaration not same.")
                        temp1=0
                        while temp1<temp.second.__len__():
                            if temp.second[temp1].id != self.second[temp1].id:
                                raise SyntaxError("Wrong datatype of argument of Redeclaration")
                            temp1=temp1+1
                return
            if functionname != 'main':
                temp=root.__len__()-1
                while temp != -1:
                    functiondeclare=scope.GoToVariable(root[temp])
                    if functiondeclare == functionname:
                        token=root[temp]
                        break
                    temp=temp-1
                if token.second.__class__() == []:
                    if token.second.__len__() != self.second.__len__() :
                        raise SyntaxError('Not same number of argument as defined in function prototype')
                else:
                    if self.second.__class__() == []:
                        raise SyntaxError('Not same number of argument as defined in function prototype')
                if token.first.id != self.first.id :
                    raise SyntaxError('The return data type not same')
                temp=0
                if self.second.__class__() == []:
                    while temp < self.second.__len__():
                        if self.second[temp].id != token.second[temp].id:
                            raise SyntaxError('The datatype of the argument not same')
                        temp=temp+1
                else:
                    if self.second != None : # For those who do not pass in any argument
                     if self.second.id != token.second.id:
                        raise SyntaxError('The datatype of the argument not same')
                scope.declareVariable(self,token)
            else:
                self.third.interpreter('main')

    sym=CExpression.infix('(',50)
    sym.interpreter=interpreter

    def interpreter(self,ReturnDataType):
        if ReturnDataType=='void':
            raise SyntaxError('Void functin do not return anything.')
        else:
            return self.first.interpreter()

    sym=CKeyword.keyword('return')
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
        temp=0
        if hasattr(self,'std'):
            if self.first.__class__() == []:
                while temp<self.first.__len__():
                    if root.second[temp]!=None:
                        temp1=root.second[temp].interpreter()
                        if temp1 > (self.value-1)/2:
                            temp1=(self.value-1)/2
                        elif temp1 < -1*(self.value+1)/2:
                            temp1=-1*(self.value+1)/2
                        scope.declareVariable(root,int(temp1),None,temp)
                    else:
                        scope.declareVariable(root,0,None,temp)
                    temp=temp+1
            else:
                temp1=root.second.interpreter()
                if temp1 > (self.value-1)/2:
                    temp1=(self.value-1)/2
                elif temp1 < -1*(self.value+1)/2:
                    temp1=-1*(self.value+1)/2
                scope.declareVariable(root,int(temp1))
        else:
            if root.second.id == '.':
                mainvariable=scope.GoToVariable(root.second)
                temp = scope.findValueOfVariableOfStruct(root.second,mainvariable)
                temp1=scope.findVariable(self.first)
                if temp > (temp1[0][0].value-1)/2:
                    temp=(temp1[0][0].value-1)/2
                elif temp < -1*(temp1[0][0].value+1)/2:
                    temp=-1*(temp1[0][0].value+1)/2
                scope.changeValueOfVariable(root,int(temp))
            else:
                temp=root.second.interpreter()
                temp1=scope.findVariable(self.first)
                if temp > (temp1[0][0].value-1)/2:
                    temp=(temp1[0][0].value-1)/2
                elif temp < -1*(temp1[0][0].value+1)/2:
                    temp=-1*(temp1[0][0].value+1)/2
                scope.changeValueOfVariable(root,int(temp))

    sym=CKeyword.keyword('short')
    sym.interpreter=interpreter
    sym.assign=assign

    sym=CKeyword.keyword('signed')
    sym.interpreter=interpreter
    sym.assign=assign

    def assign(self,root):
        temp=0
        if hasattr(self,'std'):
            if self.first.__class__() == []:
                while temp<self.first.__len__():
                    if root.second[temp]!=None:
                        temp1=root.second[temp].interpreter()
                        if temp1 > (self.value):
                            temp1=(self.value)
                        elif temp1 < 0:
                            temp1=0
                        scope.declareVariable(root,int(temp1),None,temp)
                    else:
                        scope.declareVariable(root,0,None,temp)
                    temp=temp+1
            else:
                temp1=root.second.interpreter()
                if temp1 > (self.value):
                    temp1=(self.value)
                elif temp1 < 0:
                    temp1=0
                scope.declareVariable(root,int(temp1))
        else:
            if root.second.id == '.':
                mainvariable=scope.GoToVariable(root.second)
                temp = scope.findValueOfVariableOfStruct(root.second,mainvariable)
                temp1=scope.findVariable(self.first)
                if temp > (temp1[0][0].value):
                    temp=(temp1[0][0].value)
                elif temp <  0:
                    temp=0
                scope.changeValueOfVariable(root,int(temp))
            else:
                temp=root.second.interpreter()
                temp1=scope.findVariable(self.first)
                if temp > (temp1[0][0].value):
                    temp=(temp1[0][0].value)
                elif temp < 0:
                    temp=0
                scope.changeValueOfVariable(root,int(temp))

    sym=CKeyword.keyword('unsigned')
    sym.interpreter=interpreter
    sym.assign=assign

    def assign(self,root):
        temp=0
        if hasattr(self,'std'):
            if self.first.__class__() == []:
                while temp<self.first.__len__():
                    if root.second[temp]!=None:
                        temp1=root.second[temp].interpreter()
                        if self.value != None:
                            if temp1 > (self.value-1)/2:
                                temp1=(self.value-1)/2
                            elif temp1 < -1*(self.value+1)/2:
                                temp1=-1*(self.value+1)/2
                            temp1=int(temp1)
                        scope.declareVariable(root,temp1,None,temp)
                    else:
                        scope.declareVariable(root,0,None,temp)
                    temp=temp+1
            else:
                temp1=root.second.interpreter()
                if self.value != None:
                    if temp1 > (self.value-1)/2:
                        temp1=(self.value-1)/2
                    elif temp1 < -1*(self.value+1)/2:
                        temp1=-1*(self.value+1)/2
                    temp1=int(temp1)
                scope.declareVariable(root,temp1)
        else:
            if root.second.id == '.':
                mainvariable=scope.GoToVariable(root.second)
                temp = scope.findValueOfVariableOfStruct(root.second,mainvariable)
                if self.value != None:
                    if temp > (self.value-1)/2:
                        temp=(self.value-1)/2
                    elif temp < -1*(self.value+1)/2:
                        temp=-1*(self.value+1)/2
                    temp=int(temp)
                scope.changeValueOfVariable(root,temp)
            else:
                temp=root.second.interpreter()
                temp1=scope.findVariable(self.first)
                if temp1[0][0].value != None:
                    if temp > (temp1[0][0].value-1)/2:
                        temp=(temp1[0][0].value-1)/2
                    elif temp < -1*(temp1[0][0].value+1)/2:
                        temp=-1*(temp1[0][0].value+1)/2
                    temp=int(temp)
                scope.changeValueOfVariable(root,temp)

    sym=CKeyword.keyword('long')
    sym.interpreter=interpreter
    sym.assign=assign



################################################################################
################################################################################
##"Call C InterpreterGrammar()."                                              ##
CInterpreterGrammar()
##                                                                            ##