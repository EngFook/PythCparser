import unittest
import Cparser
from CScope import *
def valueof(symObj):
    return symObj.first

test_result=True
debug_all=True

class TestScope(unittest.TestCase):
    def test_add_scope(self):
        global scope
        self.assertEqual(scope[0],{})
        Scope.add_scope(self)
        self.assertEqual(scope[1],{})
        Scope.delete_current_scope(self)

    def test_delete_current_scope(self):
        global scope
        Scope.add_scope(self)
        self.assertEqual(scope,[{},{}])
        self.assertEqual(scope[1],{})
        Scope.delete_current_scope(self)
        self.assertEqual(scope,[{}])

    def test_add_variable_scope(self):
        global scope
        i=0
        a="int b = 2 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a.first,a.first,a.second)
        temp=scope[-1][a.first.first]
        self.assertEqual(temp[1],'2')
        self.assertEqual(temp[0],a.first)
        for b in scope[-1].keys():
            self.assertEqual(b,a.first.first)
        scope[-1].clear()

    def test_find_variable_scope(self):
        global scope
        a="int a = 3 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a.first,a.first,a.second)
        temp=Scope.find_variable(a.first,a.first)
        self.assertEqual(temp[1],'3')
        self.assertEqual(temp[0],a.first)
        scope[-1].clear()

    def test_find_the_variable_in_diff_scope(self):
        global scoe
        a="int a = 3 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a.first,a.first,a.second)
        temp=Scope.find_variable(a.first,a.first)
        self.assertEqual(temp[1],'3')
        self.assertEqual(temp[0],a.first)
        Scope.add_scope(self)
        self.assertEqual(scope[-1],{})
        temp=Scope.find_variable(a.first,a.first)
        self.assertEqual(temp[1],'3')
        self.assertEqual(temp[0],a.first)
        Scope.delete_current_scope(self)
        scope[-1].clear()

    def test_find_the__variable_from_diff_scope_with_variables(self):
        global scoe
        a="int a = 3 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a.first,a.first,a.second)
        temp=Scope.find_variable(a.first,a.first)
        self.assertEqual(temp[1],'3')
        self.assertEqual(temp[0],a.first)
        b="double b = 4 ;"
        b=root=Cparser.parse(b)
        Scope.add_variable(b.first,b.first,b.second)
        temp=Scope.find_variable(b.first,b.first)
        self.assertEqual(temp[1],'4')
        self.assertEqual(temp[0],b.first)
        Scope.add_scope(self)
        self.assertEqual(scope[-1],{})
        temp=Scope.find_variable(a.first,a.first)
        self.assertEqual(temp[1],'3')
        self.assertEqual(temp[0],a.first)
        Scope.delete_current_scope(self)
        scope[-1].clear()

    def test_add_the__variable_to_diff_scope(self):
        global scoe
        a="int a = 3 ;"
        a=root=Cparser.parse(a)
        Scope.add_variable(a.first,a.first,a.second)
        temp=Scope.find_variable(a.first,a.first)
        self.assertEqual(temp[1],'3')
        self.assertEqual(temp[0],a.first)
        Scope.add_scope(self)
        b="double b = 4 ;"
        b=root=Cparser.parse(b)
        Scope.add_variable(b.first,b.first,b.second)
        temp=Scope.find_variable(b.first,b.first)
        self.assertEqual(temp[1],'4')
        self.assertEqual(temp[0],b.first)
        temp=Scope.find_variable(a.first,a.first)
        self.assertEqual(temp[1],'3')
        self.assertEqual(temp[0],a.first)
        Scope.delete_current_scope(self)
        scope[-1].clear()

if __name__=='__main__':
    if test_result==True:
        unittest.main()
    elif debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter)
        unittest.TextTestRunner(verbosity=2).run(suite)