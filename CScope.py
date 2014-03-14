"""
    Have to modify . 3/13/2014
                                """
from CInterperter import *
class Scope():

    def createScope(self):
        self.scopes=[]
        self.scopes.append({})

    def addScope(self):
        self.scopes.append({})

    def deleteCurrentScope(self):
        del self.scopes[-1]

    def addVariable(self,root,value=0):
        temp=root
        while hasattr (temp,'first'):
            temp=temp.first
        if self.checkVariable(temp):
            raise SyntaxError ('"{0}" cannot defined twice. '.format(temp))
        self.scopes[-1][temp]=(symbolTable[root.first.id],value)

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
        temp=root
        while hasattr (temp,'first'):
            temp=temp.first
        temp1=self.findVariable(temp)
        self.scopes[self.index][temp]=(temp1[0],value)
        pass


