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
    def test_add_scope(self):
        global scope
        Scope.init_scope(self)
        self.assertEqual(scope[0],{})
        Scope.add_scope(self)
        self.assertEqual(scope[1],{})

    def test_delete_current_scope(self):
        global scope
        Scope.init_scope(self)
        Scope.add_scope(self)
        self.assertEqual(scope,[{},{}])
        self.assertEqual(scope[1],{})
        Scope.delete_current_scope(self)
        self.assertEqual(scope,[{}])

    def test_add_variable_scope(self):
        global scope
        Scope.init_scope(self)
        a="int b = 2 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a[0].first,a[0].first,a[0].second)
        temp=scope[-1][a[0].first.first.first]
        self.assertEqual(temp[1],2)
        self.assertEqual(temp[0],symbolTable[a[0].first.id])
        for b in scope[-1].keys():
            self.assertEqual(b,a[0].first.first.first)

    def test_find_variable_scope(self):
        global scope
        Scope.init_scope(self)
        a="int a = 3 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a[0].first,a[0].first,a[0].second)
        temp=Scope.find_variable(a[0].first,a[0].first)
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[a[0].first.id])

    def test_find_the_variable_in_diff_scope(self):
        global scope
        Scope.init_scope(self)
        a="int a = 3 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a[0].first,a[0].first,a[0].second)
        temp=Scope.find_variable(a[0].first,a[0].first)
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[a[0].first.id])
        Scope.add_scope(self)
        self.assertEqual(scope[-1],{})
        temp=Scope.find_variable(a[0].first,a[0].first)
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[a[0].first.id])

    def test_find_the__variable_from_diff_scope_with_variables(self):
        global scope
        Scope.init_scope(self)
        a="int a = 3 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a[0].first,a[0].first,a[0].second)
        temp=Scope.find_variable(a[0].first,a[0].first)
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[a[0].first.id])
        b="double b = 4 ;"
        b=root=Cparser.parse(b)
        Scope.add_variable(b[0].first,b[0].first,b[0].second)
        temp=Scope.find_variable(b[0].first,b[0].first)
        self.assertEqual(temp[1],4)
        self.assertEqual(temp[0],symbolTable[b[0].first.id])
        Scope.add_scope(self)
        self.assertEqual(scope[-1],{})
        temp=Scope.find_variable(a[0].first,a[0].first)
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[a[0].first.id])

    def test_add_the__variable_to_diff_scope(self):
        global scope
        Scope.init_scope(self)
        a="int a = 3 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a[0].first,a[0].first,a[0].second)
        temp=Scope.find_variable(a[0].first,a[0].first)
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[a[0].first.id])
        Scope.add_scope(self)
        b="double b = 4 ;"
        b=root=Cparser.parse(b)
        Scope.add_variable(b[0].first,b[0].first,b[0].second)
        temp=Scope.find_variable(b[0].first,b[0].first)
        self.assertEqual(temp[1],4)
        self.assertEqual(temp[0],symbolTable[b[0].first.id])
        temp=Scope.find_variable(a[0].first,a[0].first)
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[a[0].first.id])
################################################################################
################################################################################
if __name__=='__main__':
    if debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestScope)
        unittest.TextTestRunner(verbosity=2).run(suite)