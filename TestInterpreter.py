import unittest

import Cparser
from Tokenizer import *
from CScope import *
def valueof(symObj):
    return symObj.first

#set On/Off -> False = Off ; True = On
#To verify test_result:
test_result=True
#To debug_all,set test_result = False:
debug_all=True

class ProductionClass():
    def method():
        return 3
################################################################################
##[Mixing style]################################################################
################################################################################
# Test -> Expression
################################################################################
class TestInterpreter(unittest.TestCase):
    def test_plus_interpreter(self):
        a=" 2 + 3 ;"
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,5)

    def test_plus_multiply_interpreter(self):
        a=" 2 + 3 * 4 ;"
        """       +
                /   \
              2      *
                    /  \
                  3      4"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,14)

    def test_postfix_negative_interpreter(self):
        a="- 1 ;"
        """ -
            |
            1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,-1)

    def test_plus_before_return_interpreter(self):
        a=" 2 ** 2 ** 3 ;"
        """       **
                /   \
              2      **
                    /  \
                  2      3"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,256)
        two=root.first
        value=two.interpreter()
        self.assertEqual(value,2)
        eight=root.second
        value=eight.interpreter()
        self.assertEqual(value,8)
        two=eight.first
        value=two.interpreter()
        self.assertEqual(value,2)
        three=eight.second
        value=three.interpreter()
        self.assertEqual(value,3)

    def test_braceket_interpreter(self):
        a=" ( 2 + 3 ) * 4 ;"
        """     *
              /    \
             (      4
             |
             +
           /   \
          2     3 """
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,20)
        bracket=root.first
        value=bracket.interpreter()
        self.assertEqual(value,5)
        four=root.second
        value=four.interpreter()
        self.assertEqual(value,4)
        plus=bracket.first
        value=plus.interpreter()
        self.assertEqual(value,5)
        two=plus.first
        value=two.interpreter()
        self.assertEqual(value,2)
        three=plus.second
        value=three.interpreter()
        self.assertEqual(value,3)

    def test_equalequal_condition_interpreter(self):
        a=" 1 == 1 ;"
        """ ==
           /  \
          1    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertTrue(value)

    def test_bigger_condition_interpreter(self):
        a=" 2 > 1 ;"
        """ >
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertTrue(value)

    def test_smaller_condition_interpreter(self):
        a=" 2 < 1 ;"
        """ <
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertFalse(value)

    def test_biggerequal_condition_interpret(self):
        a=" 2 >= 1 ;"
        """ >=
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertTrue(value)

    def test_smallerequal_condition_interpreter(self):
        a=" 2 < 1 ;"
        """ <=
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertFalse(value)

    def test_shiftleft_bit_interpreter(self):
        a=" 1 << 3 ;"
        """ <<
           /  \
          1    3"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,8)

    def test_shiftright_bit_interpreter(self):
        a=" 8 >> 3 ;"
        """ >>
           /  \
          8    3"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,1)

    def test_and_bit_interpreter(self):
        a=" 5 & 6 ;"
        """ &
           /  \
          5    6"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,4)

    def test_xor_bit_interpreter(self):
        a=" ~ 2 ;"
        """ ~
            |
            2"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,-3)

    def test_not_bit_interpreter(self):
        a=" ! 2 ;"
        """ !
            |
            2"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,0)

    def test_braces_interpreter(self):
        a="""{
                1 + 2 ;
                2 + 3 ;
             }"""
        """ {
            |------- +
            |       / \
            |      1   2
            |--------+
                    / \
                   2   3"""

        root=Cparser.parse(a)
        three=root.first[0].interpreter()
        five=root.first[1].interpreter()
        self.assertEqual(three,3)
        self.assertEqual(five,5)

    def test_int_a_double_b_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""
                int a = 2 ;
                double b = 3 ;
              """
        """
                     =
                    /  \
                int-a   2
                      =
                    /   \
               double-b  0.1"""
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],2)
        temp=Scope.find_variable(root[1].first,root[1].first)
        self.assertEqual(temp[0],'double')
        self.assertEqual(temp[1],3)

    def test_braces_with_assigened_indentfier_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""   int c = 2 ;
                1 + c ;
            """

        """
                     =
                    / \
                   c   2
                     +
                    / \
                   1   c"""
        root=Cparser.parsex(a)
        root[0].interpreter()
        three=root[1].interpreter()
        self.assertEqual(three,3)

    def test_minusminus_after_literal_indentfier_interpreter(self):
        a="10 -- ;"
        root=Cparser.parse(a)
        self.assertRaises(SyntaxError,root.interpreter)

    def test_minusminus_before_literal_indentfier_interpreter(self):
        a="-- 10 ;"
        root=Cparser.parse(a)
        self.assertRaises(SyntaxError,root.interpreter)

    def test_minusminus_after_indentifier_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""
                int a = 5 ;
                a -- ;
                -- a ;
             """

        """
                     =
                    /  \
                int-a   2
             --__a
             --__a"""
        root=Cparser.parsex(a)
        root[0].interpreter()
        five=root[1].interpreter()
        self.assertEqual(five,5)
        three=root[2].interpreter()
        self.assertEqual(three,3)

    def test_if_false_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""
                int a = 5 ;
                if ( 0 ) a = 4 ;
                1 + a ;

            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        six = root[2].interpreter()
        self.assertEqual(six,6)

    def test_if_true_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""
                int a = 5 ;
                if ( 1 ) a = 4 ;
                1 + a ;

            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        five = root[2].interpreter()
        self.assertEqual(five,5)


    def test_if_with_else_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""
                int a = 5 ;
                if ( 0 ) a = 4 ;
                else  a = 3 ;
            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],3)


    def test_if_with_else_if_true_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""
               int a = 5 ;
               if ( 0 ) a = 4 ;
               else if ( 1 ) a = 3 ;
            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],3)

    def test_if_with_else_if_false_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""
               int a = 5 ;
               if ( 0 ) a = 4 ;
               else
                    if ( 0 ) a = 3 ;
            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],5)

    def test_if_with_condition_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""
                int a = 5 ;
                if ( a == 1 ) a = 4 ;
            """
        root=Cparser.parse(a)
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],5)

    def test_equal_without_int_error_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="a = 1 ;"
        """     =
          /   \
         a     1 """
        root=Cparser.parse(a)
        self.assertRaises(SyntaxError,root.interpreter)

    def test_declate_twice_raise_error_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int a ;
             double a ;"""
        root=Cparser.parsex(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_double_a_with_one_point_zero_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int a = 1 ;
            a = a / 2 ;
            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],0)

    def test_equal_with_int_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="int a = 1 ;"
        """     =
              /   \
          int-a    1 """
        root=Cparser.parsex(a)
        root[0].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],1)

    def test_equal_with_int_zero_point_nine_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="int a = 0.9 ;"
        """     =
              /   \
          int-a    1 """
        root=Cparser.parsex(a)
        root[0].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],0)

    def test_equal_with_double_zero_point_nine_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="double a = 0.9 ;"
        """     =
              /   \
          double-a    1 """
        root=Cparser.parsex(a)
        root[0].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'double')
        self.assertEqual(temp[1],0.9)


    def test_int_a_with_negative_value_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="int a = -1 ;"
        """     =
              /   \
          int-a    1 """
        root=Cparser.parsex(a)
        root[0].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],-1)

    def test_int_a_without_value_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="int a ;"
        """int-a"""
        root=Cparser.parse(a)
        root.interpreter()
        temp=Scope.find_variable(root.first,root.first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],None)

    def test_int_a_with_value_plusplus_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int a = 1 ;
            a ++ ;"""
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],2)

    def test_while_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int x = - 1 ;
            while ( x < 1 ) x ++ ;
            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],1)

    def test_while_infinity_lopp_raise_syntax_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int x = 0 ;
             while ( 1 ) x ++ ;
            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_while_loop_with_many_statment_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int x = 0 ;
             while ( x < 4 )
             {
                     x ++ ;
                     x -- ;
                     x ++ ;
             }

            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],4)


    def test_do_while_loop_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int x = 0
                do {  x ++ ; }
             while ( x < 3 ) ;"""
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],3)

    def test_if_none_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""if ( 0 ) ;
            else ;"""
        root=Cparser.parsex(a)
        root[0].interpreter()

    def test_while_loop_None_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int x = 0 ;
             while ( x == 0 )  ;
            """
        root=Cparser.parsex(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_do_while_loop_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int x = 0
                do { }
             while ( x < 3 ) ;"""
        root=Cparser.parsex(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_for_loop_withouth_declaration_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""for ( x = 0 ; x == 5 ; x ++ ) ;"""
        root=Cparser.parsex(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_for_loop_with_declaration_inside_interpreter(self):
        global scope
        Scope.init_scope(self)
        a="""int x ;
             for ( x = 0 ; x < 5 ; x ++ ) ;"""
        root=Cparser.parsex(a)
        root[0].interpreter()
        root[1].interpreter()
        temp=Scope.find_variable(root[0].first,root[0].first)
        self.assertEqual(temp[0],'int')
        self.assertEqual(temp[1],5)




if __name__=='__main__':
    if test_result==True:
        unittest.main()
    elif debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter)
        unittest.TextTestRunner(verbosity=2).run(suite)