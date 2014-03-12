from CInterperter import *
class Scope:
    global scope
    scope=[{}]
    def init_scope(self):
        global scope
        scope.clear()
        a={}
        scope.append(a)
        pass

    def add_scope(self):
        global scope
        a={}
        scope.append(a)
        pass

    def delete_current_scope(self):
        global scope
        del scope[-1]
        pass

    def find_variable(self,variable):
        index=scope.__len__()
        if hasattr(self,'std'):
            variable=self.first
        while index > 0:
            if variable.first in scope[index-1].keys():
                return scope[index-1][variable.first]
            index=index-1
        raise SyntaxError ('"{0}" has not declare '.format(variable.first))

    def check_variable(self,variable):
        index=scope.__len__()
        if hasattr(self,'std'):
            variable=self.first
        while index > 0:
            if variable.first in scope[index-1].keys():
                return scope[index-1][variable.first]
            index=index-1
        return None

    def add_variable(self,variable,value):
        global scope
        if hasattr(self,'std'):
            if value == None :
                scope[-1][variable.first]=(self.id,None)
            else:
                if hasattr(value,'led'):
                    temp=value.interpreter()
                if self.id == 'int':
                    temp=int(temp)
                    scope[-1][self.first.first]=(self.id,temp)
                else:
                    scope[-1][self.first.first]=(self.id,temp)
        else:
            temp=value.interpreter()
            if variable[0] == 'int':
                temp=int(temp)
            scope[-1][self.first]=(variable[0],temp)
        pass
