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
from CInterperter import *
##"Class created for scope with specific function."                           ##
class Scope():
    def __init__(self):
        self.scopes=[]
        self.scopes.append({})

    def addScope(self):
        self.scopes.append({})

    def deleteCurrentScope(self):
        del self.scopes[-1]

    def declareVariable(self,root,value=0,Datatype=None,index=None):
        List=[]
        temp=root.first
        if hasattr(temp,'id'):
            while temp.id == '[' or temp.id=='*':
                List.append(temp)
                temp=temp.first
        temp=self.GoToVariable(root,index)
        if Datatype==None :
            temp1=root
            while not hasattr(temp1,'std'):
                    temp1=root.first
            List.insert(0,symbolTable[temp1.id])
        else:
            List.insert(0,symbolTable[Datatype])
        if self.checkCurrnetScope(temp) != None :
            raise SyntaxError ('"{0}" cannot defined twice. '.format(temp))
        self.scopes[-1][temp]=(List,value)
        return

    def checkVariable(self,variable):
        self.index=self.scopes.__len__()
        while self.checkParentsScope():
            if self.checkCurrnetScope(variable) != None :
                return True
        else: False

    def findVariable(self,variable):
        self.index=self.scopes.__len__()
        while self.checkParentsScope():
            if self.checkScope(variable) != None :
                return self.checkScope(variable)
        raise SyntaxError ('"{0}" has not declare '.format(variable))

    def checkParentsScope(self):
        self.index=self.index-1
        if self.index != -1:
            return True
        else:
            False

    def checkScope(self,variable):
        if variable in self.scopes[self.index].keys():
            return self.scopes[self.index][variable]
        else: return None

    def checkCurrnetScope(self,variable):
        if variable in self.scopes[-1].keys():
            return self.scopes[-1][variable]
        else: return None

    def changeValueOfVariable(self,root,value=0):
        temp=self.GoToVariable(root)
        temp1=self.findVariable(temp)
        self.scopes[self.index][temp]=(temp1[0],value)
        pass

    def GoToVariable(self,root,index=0):
        temp=root
        while hasattr (temp,'first'):
            temp=temp.first
            if temp.__class__()==[]:
                temp=temp[index]
        return temp

    def findValueOfVariableOfStruct(self,root,mainvariable,current=None):
        current = root
        temp=[]
        while current.id == '.':
            temp.append(current.second.first)
            current=current.first
        store=scope.scopes[self.index][mainvariable]
        while temp != [] :
            temp1 = temp.pop()
            if temp1 not in store[1] :
                raise SyntaxError ('wrong format')
            store=store[1][temp1]
        return store[1]

    global assign
    assign=False

    def changeValueOfVariableOfStruct(self,variable,biggest,contentofvariable,value=0):

        global assign
        assign=False
        for key in biggest[1]:
            if biggest[1][key][1].__class__() == {}:
                if key == contentofvariable:
                    raise SyntaxError ('wrong format')
                temp=biggest[1][key]
                self.changeValueOfVariableOfStruct(variable,temp,contentofvariable,value)
                if assign == True :
                    return
            if contentofvariable == key:
                if biggest[1][key][0].id == 'int':
                    value =int(value)
                biggest[1][contentofvariable]=(biggest[1][key][0],value)
                assign=True
                return
        if assign or biggest !=  self.scopes[self.index][variable]:
            return
        else:
            raise SyntaxError ('"{0}" has not declare '.format(root.first.second.first))

################################################################################
################################################################################
##"Create global scope."                                                      ##
global scope
scope=Scope()
##                                                                            ##