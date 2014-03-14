##"Files imported."                                                           ##
import unittest
import Cparser
from CScope import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
    This module is for test scope.
                                                                """
'''
    Set On/Off -> False = Off ; True = On
    To debug_all: set debug_all=True
                                            '''
debug_all=True
##"Test start."                                                               ##
class TestScope(unittest.TestCase):

    def test_create_scope(self):
        scope=Scope()
        scope.createScope()
        self.assertEqual(scope.scopes[0],{})

    def test_add_scope(self):
        scope=Scope()
        scope.createScope()
        scope.addScope()
        self.assertEqual(scope.scopes.__len__(),2)

    def test_delete_current_scope(self):
        scope=Scope()
        scope.createScope()
        scope.addScope()
        self.assertEqual(scope.scopes.__len__(),2)
        scope.deleteCurrentScope()
        self.assertEqual(scope.scopes.__len__(),1)

    def test_add_variable_scope(self):
        scope=Scope()
        scope.createScope()
        a="int b = 2 ;"
        root=Cparser.parse(a)
        scope.addVariable(root[0],int(root[0].second.interpreter()))
        temp=scope.findVariable('b')
        self.assertEqual(temp[1],2)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])

    def test_find_the_variable_in_diff_scope(self):
        scope=Scope()
        scope.createScope()
        a="int a = 3 ;"
        root=Cparser.parse(a)
        scope.addVariable(root[0],int(root[0].second.interpreter()))
        scope.addScope()
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])

    def test_find_the__variable_from_diff_scope_with_variables(self):
        scope=Scope()
        scope.createScope()
        a="int a = 3 ;"
        root=Cparser.parse(a)
        scope.addVariable(root[0],int(root[0].second.interpreter()))
        scope.addScope()
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])
        b="double b = 4 ;"
        root=Cparser.parse(b)
        scope.addVariable(root[0],int(root[0].second.interpreter()))
        scope.addScope()
        temp=scope.findVariable('b')
        self.assertEqual(temp[1],4)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])

    def test_change_variable(self):
        scope=Scope()
        scope.createScope()
        a="""int a ;
             a = 3 ;"""
        root=Cparser.parse(a)
        scope.addVariable(root[0])
        scope.changeValueOfVariable(root[1],int(root[1].second.interpreter()))
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])

    def test_cannot_declare_twice(self):
        scope=Scope()
        scope.createScope()
        a="""int a ;
             int a ;"""
        root=Cparser.parse(a)
        scope.addVariable(root[0])
        self.assertRaises(SyntaxError,scope.addVariable,root[1])

    def test_need_to_declare_before_assign(self):
        scope=Scope()
        scope.createScope()
        a="""a = 3 ;"""
        root=Cparser.parse(a)
        self.assertRaises(SyntaxError,scope.changeValueOfVariable,root[0])


################################################################################
################################################################################
if __name__=='__main__':
    if debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestScope)
        unittest.TextTestRunner(verbosity=2).run(suite)