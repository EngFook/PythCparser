##"Files imported."                                                           ##
import unittest
import CParser
from CScope import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
                        This module is to test -> scope
                                                                             """
##"Test start."                                                               ##
class TestScope(unittest.TestCase):

    def test_create_scope(self):
        scope=Scope()
        self.assertEqual(scope.scopes[0],{})

    def test_add_scope(self):
        scope=Scope()
        scope.addScope()
        self.assertEqual(scope.scopes.__len__(),2)

    def test_delete_current_scope(self):
        scope=Scope()
        scope.addScope()
        self.assertEqual(scope.scopes.__len__(),2)
        scope.deleteCurrentScope()
        self.assertEqual(scope.scopes.__len__(),1)

    def test_add_variable_scope(self):
        scope=Scope()
        a="int b = 2 ;"
        root=CParser.parse(a)
        scope.declareVariable(root[0],int(root[0].second.interpreter()))
        temp=scope.findVariable('b')
        self.assertEqual(temp[1],2)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])

    def test_find_the_variable_in_diff_scope(self):
        scope=Scope()
        a="int a = 3 ;"
        root=CParser.parse(a)
        scope.declareVariable(root[0],int(root[0].second.interpreter()))
        scope.addScope()
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])

    def test_find_the__variable_from_diff_scope_with_variables(self):
        scope=Scope()
        a="int a = 3 ;"
        root=CParser.parse(a)
        scope.declareVariable(root[0],int(root[0].second.interpreter()))
        scope.addScope()
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])
        b="double b = 4 ;"
        root=CParser.parse(b)
        scope.declareVariable(root[0],int(root[0].second.interpreter()))
        scope.addScope()
        temp=scope.findVariable('b')
        self.assertEqual(temp[1],4)
        self.assertEqual(temp[0],symbolTable[root[0].first.id])

    def test_change_variable(self):
        scope=Scope()
        a="""int a ;
             a = 3 ;"""
        root=CParser.parse(a)
        scope.declareVariable(root[0])
        scope.changeValueOfVariable(root[1],int(root[1].second.interpreter()))
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],3)
        self.assertEqual(temp[0],symbolTable[root[0].id])

    def test_cannot_declare_twice(self):
        scope=Scope()
        a="""int a ;
             int a ;"""
        root=CParser.parse(a)
        scope.declareVariable(root[0])
        self.assertRaises(SyntaxError,scope.declareVariable,root[1])

    def test_can_declare_twice_in_diif_scope(self):
        scope=Scope()
        a="""int a ;
             int a ;"""
        root=CParser.parse(a)
        scope.declareVariable(root[0])
        scope.addScope()
        scope.declareVariable(root[1])

    def test_need_to_declare_before_assign(self):
        scope=Scope()
        a="""a = 3 ;"""
        root=CParser.parse(a)
        self.assertRaises(SyntaxError,scope.changeValueOfVariable,root[0])


################################################################################
################################################################################
if __name__=='__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestScope)
        unittest.TextTestRunner(verbosity=2).run(suite)