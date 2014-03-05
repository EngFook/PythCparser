import unittest
import Cparser
from CScope import *
def valueof(symObj):
    return symObj.first

class Scope:
    global scope
    scope=[{}]
    def add_scope(self):
        global scope
        a={}
        scope.append(a)
        return

    def delete_current_scope(self):
        global scope
        del scope[-1]

    def find_variable(self,variable):
        index=scope.__len__()
        while index > 0:
            if variable.first in scope[index-1].keys():
                return scope[index-1][variable.first]
            index=index-1
        raise SyntaxError ('Could not find the value of {0}'.format(variable.first))

    def add_variable(self,variable,value):
        global scope
        scope[-1][variable.first]=(self,value.first)
        pass


