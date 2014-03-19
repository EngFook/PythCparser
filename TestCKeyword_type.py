##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
                  This module is to test keyword -> type
                                                                             """
##"Test start here."                                                          ##
class TestKeyword_type(unittest.TestCase):

    def test_type_with_declaration_of_variable_more_than_once_int(self):
        a=''' int a = 1 , b = 2 , c , d = 3 ; '''
        """
                            =
                          /   \
                        int     [1,2,None,3]
                         |
                    [a,b,c,d]
                                                """
        root=CParser.parse(a)
        equal=root[0]
        self.assertEqual(equal.id,'=')
        INT=equal.first
        self.assertEqual(INT.id,'int')
        arrayfirst=equal.first
        a=arrayfirst.first[0]
        self.assertEqual(valueof(a),'a')
        b=arrayfirst.first[1]
        self.assertEqual(valueof(b),'b')
        c=arrayfirst.first[2]
        self.assertEqual(valueof(c),'c')
        d=arrayfirst.first[3]
        self.assertEqual(valueof(d),'d')
        arraysecond=root[0].second
        one=arraysecond[0]
        self.assertEqual(valueof(one),'1')
        two=arraysecond[1]
        self.assertEqual(valueof(two),'2')
        NONE=arraysecond[2]
        self.assertIsNone(NONE)
        three=arraysecond[3]
        self.assertEqual(valueof(three),'3')

    def test_type_with_declaration_of_variable_more_than_once_double(self):
        a=''' double a = 1 , b = 2 , c , d = 3 ; '''
        """
                            =
                          /   \
                      double   [1,2,None,3]
                         |
                    [a,b,c,d]
                                                """
        root=CParser.parse(a)
        equal=root[0]
        self.assertEqual(equal.id,'=')
        DOUBLE=equal.first
        self.assertEqual(DOUBLE.id,'double')
        arrayfirst=equal.first
        a=arrayfirst.first[0]
        self.assertEqual(valueof(a),'a')
        b=arrayfirst.first[1]
        self.assertEqual(valueof(b),'b')
        c=arrayfirst.first[2]
        self.assertEqual(valueof(c),'c')
        d=arrayfirst.first[3]
        self.assertEqual(valueof(d),'d')
        arraysecond=root[0].second
        one=arraysecond[0]
        self.assertEqual(valueof(one),'1')
        two=arraysecond[1]
        self.assertEqual(valueof(two),'2')
        NONE=arraysecond[2]
        self.assertIsNone(NONE)
        three=arraysecond[3]
        self.assertEqual(valueof(three),'3')

    def test_type_with_declaration_of_variable_more_than_once_struct_type(self):
        a=''' struct Type {
                int a ;
                int b ;
                            } ;
              struct Type a = 1 , b = 2 , c , d = 3  ;  '''
        """
                                    (root[1])
                                  =
                               /     \
                      struct Type   [1,2,None,3]
                         |
                    [a,b,c,d]
                                                """
        root=CParser.parse(a)
        equal=root[1]
        self.assertEqual(equal.id,'=')
        structType=equal.first
        self.assertEqual(structType.id,'struct Type')
        arrayfirst=equal.first
        a=arrayfirst.first[0]
        self.assertEqual(valueof(a),'a')
        b=arrayfirst.first[1]
        self.assertEqual(valueof(b),'b')
        c=arrayfirst.first[2]
        self.assertEqual(valueof(c),'c')
        d=arrayfirst.first[3]
        self.assertEqual(valueof(d),'d')
        arraysecond=root[1].second
        one=arraysecond[0]
        self.assertEqual(valueof(one),'1')
        two=arraysecond[1]
        self.assertEqual(valueof(two),'2')
        NONE=arraysecond[2]
        self.assertIsNone(NONE)
        three=arraysecond[3]
        self.assertEqual(valueof(three),'3')
################################################################################
################################################################################
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_type)
        unittest.TextTestRunner(verbosity=2).run(suite)