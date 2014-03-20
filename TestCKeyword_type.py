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

    def test_Int_a(self):
        a='int a ;'
        """  int
             |
             a"""

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'int')
        a=root[0].first
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')

    def test_Int_a_b_c(self):
        a='int a , b , c ;'
        """  int
             |
             |-a
             |-b
             |-c"""

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'int')
        a=root[0].first[0]
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')
        a=root[0].first[1]
        self.assertEqual(valueof(a),'b')
        self.assertEqual(a.id,'(identifier)')
        a=root[0].first[2]
        self.assertEqual(valueof(a),'c')
        self.assertEqual(a.id,'(identifier)')

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
                         /     \
                    [a,b,c,d]   {
                                |
                                [-------int
                                  |      |
                                  |      a
                                  |
                                  |-----int
                                         |
                                         b

                                                            """
        root=CParser.parse(a)
        equal=root[1]
        self.assertEqual(equal.id,'=')
        structType=equal.first
        self.assertEqual(structType.id,'struct Type')
        arrayfirst=equal.first.first
        a=arrayfirst[0]
        self.assertEqual(valueof(a),'a')
        b=arrayfirst[1]
        self.assertEqual(valueof(b),'b')
        c=arrayfirst[2]
        self.assertEqual(valueof(c),'c')
        d=arrayfirst[3]
        self.assertEqual(valueof(d),'d')
        brace=equal.first.second
        self.assertEqual(brace.id,'{')
        INTA=brace.first[0]
        self.assertEqual(INTA.id,'int')
        a=INTA.first
        self.assertEqual(valueof(a),'a')
        INTB=brace.first[1]
        self.assertEqual(INTB.id,'int')
        b=INTB.first
        self.assertEqual(valueof(b),'b')
        arraysecond=root[1].second
        one=arraysecond[0]
        self.assertEqual(valueof(one),'1')
        two=arraysecond[1]
        self.assertEqual(valueof(two),'2')
        NONE=arraysecond[2]
        self.assertIsNone(NONE)
        three=arraysecond[3]
        self.assertEqual(valueof(three),'3')

    def test_type_with_declaration_of_variable_more_than_once_struct_type_2nd(self):
        a=''' struct Type2 {
                int a ;
                int b ;
                            } ;
              struct Type2 a , b , c , d ;  '''
        """
                                    (root[0])
                      struct Type2
                         /     \
                    [a,b,c,d]   {
                                |
                                [-------int
                                  |      |
                                  |      a
                                  |
                                  |-----int
                                         |
                                         b

                                                            """
        root=CParser.parse(a)
        structType=root[1]
        self.assertEqual(structType.id,'struct Type2')
        arrayfirst=structType.first
        a=arrayfirst[0]
        self.assertEqual(valueof(a),'a')
        b=arrayfirst[1]
        self.assertEqual(valueof(b),'b')
        c=arrayfirst[2]
        self.assertEqual(valueof(c),'c')
        d=arrayfirst[3]
        self.assertEqual(valueof(d),'d')
        brace=structType.second
        self.assertEqual(brace.id,'{')
        INTA=brace.first[0]
        self.assertEqual(INTA.id,'int')
        a=INTA.first
        self.assertEqual(valueof(a),'a')
        INTB=brace.first[1]
        self.assertEqual(INTB.id,'int')
        b=INTB.first
        self.assertEqual(valueof(b),'b')

    def test_type_with_declaration_of_variable_more_than_once_enum_type(self):
        a='''enum DAY_A
                        {
                            saturday ,
                            sunday
                                        } workday ;
                    enum DAY_A a , b ;'''
        """
                                    (root[1])
                        enum DAY_A
                         /     \
                    [a , b]     {
                                |
                                [-------saturday
                                  |
                                  |
                                  |
                                  |-----sunday

                                                            """
        root=CParser.parse(a)
        enumType=root[1]
        self.assertEqual(enumType.id,'enum DAY_A')
        arrayfirst=enumType.first
        a=arrayfirst[0]
        self.assertEqual(valueof(a),'a')
        b=arrayfirst[1]
        self.assertEqual(valueof(b),'b')
        brace=enumType.second
        self.assertEqual(brace.id,'{')
        saturday=brace.first[0]
        self.assertEqual(valueof(saturday),'saturday')
        sunday=brace.first[1]
        self.assertEqual(valueof(sunday),'sunday')

    def test_type_with_declaration_of_variable_more_than_once_enum_type_2nd(self):
        a='''enum DAY_B
                        {
                            saturday ,
                            sunday
                                        } workday ;
                    enum DAY_B a = 1 , b = 2 ;'''
        """
                                    (root[1])
                                  =
                               /     \
                        enum DAY_B     [1,2]
                         /     \
                    [a,b]   {
                                |
                                [-------saturday
                                  |
                                  |
                                  |
                                  |-----sunday


                                                            """
        root=CParser.parse(a)
        equal=root[1]
        self.assertEqual(equal.id,'=')
        enumType=equal.first
        self.assertEqual(enumType.id,'enum DAY_B')
        arrayfirst=enumType.first
        a=arrayfirst[0]
        self.assertEqual(valueof(a),'a')
        b=arrayfirst[1]
        self.assertEqual(valueof(b),'b')
        brace=equal.first.second
        saturday=brace.first[0]
        self.assertEqual(valueof(saturday),'saturday')
        sunday=brace.first[1]
        self.assertEqual(valueof(sunday),'sunday')
        arraysecond=root[1].second
        one=arraysecond[0]
        self.assertEqual(valueof(one),'1')
        two=arraysecond[1]
        self.assertEqual(valueof(two),'2')

################################################################################
################################################################################
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_type)
        unittest.TextTestRunner(verbosity=2).run(suite)