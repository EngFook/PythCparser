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

    def declareVariable(self,root,value=0,Datatype=None):
        temp=self.GoToVariable(root)
        if self.checkVariable(temp):
            raise SyntaxError ('"{0}" cannot defined twice. '.format(temp))
        if Datatype == None:
            temp1=root
            while not hasattr(temp1,'std'):
                temp1=root.first
            self.scopes[-1][temp]=(symbolTable[temp1.id],value)
            return
        else:
            self.scopes[-1][temp]=(symbolTable[Datatype],value)

    def checkVariable(self,variable):
        self.index=self.scopes.__len__()
        while self.checkParentsScope():
            if self.checkCurrnetScope(variable) != None :
                return True
        else: False

    def findVariable(self,variable):
        self.index=self.scopes.__len__()
        while self.checkParentsScope():
            if self.checkCurrnetScope(variable) != None :
                return self.checkCurrnetScope(variable)
        raise SyntaxError ('"{0}" has not declare '.format(variable))

    def checkParentsScope(self):
        self.index=self.index-1
        if self.index != -1:
            return True
        else:
            False

    def checkCurrnetScope(self,variable):
        if variable in self.scopes[self.index].keys():
            return self.scopes[self.index][variable]
        else: return None

    def changeValueOfVariable(self,root,value=0):
        temp=self.GoToVariable(root)
        temp1=self.findVariable(temp)
        self.scopes[self.index][temp]=(temp1[0],value)
        pass

    def GoToVariable(self,root):
        temp=root
        while hasattr (temp,'first'):
            temp=temp.first
        return temp

    def changeValueOfVariableOfStruct(self,root,value=0):
        temp=self.GoToVariable(root)
        temp1=self.findVariable(temp)
        for temp2 in temp1[1]:
            if root.first.second.first == temp2:
                if temp1[1][temp2][0].id == 'int':
                    value =int(value)
                self.scopes[self.index][temp][1][temp2]=(temp1[1][temp2][0],value)
                return
        raise SyntaxError ('"{0}" has not declare '.format(root.first.second.first))
################################################################################
################################################################################
##"Create global scope."                                                      ##
global scope
scope=Scope()
##                                                                            ##