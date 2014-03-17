"""
    Have to modify . 3/13/2014

                                """
import unittest
import Cparser
from Tokenizer import *
from CScope import *
from CInterperter import *
def valueof(symObj):
    return symObj.first

#set On/Off -> False = Off ; True = On
#To verify test_result:
test_result=True
#To debug_all,set test_result = False:
debug_all=True

def Runinterpreter(self):
    index=0
    while index < self.__len__():
        self[index].interpreter()
        index = index + 1
################################################################################
##[Mixing style]################################################################
################################################################################
# Test -> Expression
################################################################################
class TestInterpreter(unittest.TestCase):
    def test_plus_interpreter(self):
        a=" 2 + 3 ;"
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertEqual(value,5.0)

    def test_plus_multiply_interpreter(self):
        a=" 2 + 3 * 4 ;"
        """       +
                /   \
              2      *
                    /  \
                  3      4"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertEqual(value,14)

    def test_postfix_negative_interpreter(self):
        a="- 1 ;"
        """ -
            |
            1"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertEqual(value,-1)

    def test_multiply_interpreter(self):
        a=" 2 ** 2 ** 3 ;"
        """       **
                /   \
              2      **
                    /  \
                  2      3"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertEqual(value,256)
        two=root[0].first
        value=two.interpreter()
        self.assertEqual(value,2)
        eight=root[0].second
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
        value=root[0].interpreter()
        self.assertEqual(value,20)
        bracket=root[0].first
        value=bracket.interpreter()
        self.assertEqual(value,5)
        four=root[0].second
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
        value=root[0].interpreter()
        self.assertTrue(value)

    def test_bigger_condition_interpreter(self):
        a=" 2 > 1 ;"
        """ >
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertTrue(value)

    def test_smaller_condition_interpreter(self):
        a=" 2 < 1 ;"
        """ <
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertFalse(value)

    def test_biggerequal_condition_interpret(self):
        a=" 2 >= 1 ;"
        """ >=
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertTrue(value)

    def test_smallerequal_condition_interpreter(self):
        a=" 2 < 1 ;"
        """ <=
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertFalse(value)

    def test_shiftleft_bit_interpreter(self):
        a=" 1 << 3 ;"
        """ <<
           /  \
          1    3"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertEqual(value,8)

    def test_shiftright_bit_interpreter(self):
        a=" 8 >> 3 ;"
        """ >>
           /  \
          8    3"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertEqual(value,1)

    def test_and_bit_interpreter(self):
        a=" 5 & 6 ;"
        """ &
           /  \
          5    6"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertEqual(value,4)

    def test_xor_bit_interpreter(self):
        a=" ~ 2 ;"
        """ ~
            |
            2"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
        self.assertEqual(value,-3)

    def test_not_bit_interpreter(self):
        a=" ! 2 ;"
        """ !
            |
            2"""
        root=Cparser.parse(a)
        value=root[0].interpreter()
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
        three=root[0].first[0].interpreter()
        five=root[0].first[1].interpreter()
        self.assertEqual(three,3)
        self.assertEqual(five,5)

    def test_int_a_double_b_interpreter(self):
        scope.__init__()
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
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],2)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0],symbolTable['double'])
        self.assertEqual(temp[1],3)

    def test_with_assigened_indentfier_interpreter(self):
        scope.__init__()
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
        root=Cparser.parse(a)
        root[0].interpreter()
        three=root[1].interpreter()
        self.assertEqual(three,3)

    def test_minusminus_after_literal_indentfier_interpreter(self):
        a="10 -- ;"
        root=Cparser.parse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_minusminus_before_literal_indentfier_interpreter(self):
        a="-- 10 ;"
        root=Cparser.parse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_minusminus_after_indentifier_interpreter(self):
        scope.__init__()
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
        root=Cparser.parse(a)
        root[0].interpreter()
        five=root[1].interpreter()
        self.assertEqual(five,5)
        three=root[2].interpreter()
        self.assertEqual(three,3)

    def test_equal_without_int_error_interpreter(self):
        scope.__init__()
        a="a = 1 ;"
        """ =
          /   \
         a     1 """
        root=Cparser.parse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_int_a_without_value_interpreter(self):
        scope.__init__()
        a="int a ;"
        """int-a"""
        root=Cparser.parse(a)
        root[0].interpreter()
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],0)

    def test_declate_twice_raise_error_interpreter(self):
        scope.__init__()
        a="""int a ;
             double a ;"""
        root=Cparser.parse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_equal_with_int_interpreter(self):
        scope.__init__()
        a="int a = 1 ;"
        """     =
              /   \
          int-a    1 """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],1)

    def test_int_a_with_a_divide_by_two_interpreter(self):
        scope.__init__()
        a="""int a = 1 ;
            a = a / 2 ;
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],0)

    def test_equal_with_int_zero_point_nine_interpreter(self):
        scope.__init__()
        a="int a = 0.9 ;"
        """     =
              /   \
          int-a    1 """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],0)

    def test_equal_with_double_zero_point_nine_interpreter(self):
        scope.__init__()
        a="double a = 0.9 ;"
        """     =
              /   \
          double-a    1 """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['double'])
        self.assertEqual(temp[1],0.9)


    def test_int_a_with_negative_value_interpreter(self):
        scope.__init__()
        a="int a = -1 ;"
        """     =
              /   \
          int-a    1 """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],-1)

    def test_int_a_b_c_interpreter(self):
        scope.__init__()
        a="int a , b , c ;"
        """int-a"""
        root=Cparser.parse(a)
        root[0].interpreter()
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],0.)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],0.)
        temp=scope.findVariable('c')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],0.)

    def test_int_a_with_value_plusplus_interpreter(self):
        scope.__init__()
        a="""int a = 1 ;
            a ++ ;"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1] , 2 )

    def test_if_false_interpreter(self):
        scope.__init__()
        a="""
                int a = 5 ;
                if ( 0 ) a = 4 ;
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )


    def test_if_true_interpreter(self):
        scope.__init__()
        a="""
                int a = 5 ;
                if ( 1 ) a = 4 ;
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_if_with_else_interpreter(self):
        scope.__init__()
        a="""
                int a = 5 ;
                if ( 0 ) a = 4 ;
                else  a = 3 ;
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 3 )


    def test_if_with_else_if_true_interpreter(self):
        scope.__init__()
        a="""
               int a = 5 ;
               if ( 0 ) a = 4 ;
               else if ( 1 ) a = 3 ;
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 3 )

    def test_if_with_else_if_false_interpreter(self):
        scope.__init__()
        a="""
               int a = 5 ;
               if ( 0 ) a = 4 ;
               else
                    if ( 0 ) a = 3 ;
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_if_with_condition_interpreter(self):
        scope.__init__()
        a="""
                int a = 5 ;
                if ( a == 1 ) a = 4 ;
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_if_with_condition_many_statement_interpreter(self):
        scope.__init__()
        a="""
                int a = 1 ;
                if ( a == 1 )
                {
                    a = 4 ;
                    a ++ ;
                }
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_while_interpreter(self):
        scope.__init__()
        a="""int x = - 1 ;
            while ( x < 1 ) x ++ ;
            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 1 )

    def test_while_infinity_lopp_raise_syntax_interpreter(self):
        scope.__init__()
        a="""int x = 0 ;
             while ( 1 ) x ++ ;
            """
        root=Cparser.parse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_while_loop_with_many_statment_interpreter(self):
        scope.__init__()
        a="""int x = 0 ;
             while ( x < 4 )
             {
                     x ++ ;
                     x -- ;
                     x ++ ;
             }

            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_while_loop_with_many_statment_diff_variable_interpreter(self):
        scope.__init__()
        a="""int x = 0 ;
             int b = 1 ;
             int c = 2 ;
             while ( x < 4 )
             {
                     x ++ ;
                     b ++ ;
                     c ++ ;
             }

            """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )
        temp=scope.findVariable('b')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5)
        temp=scope.findVariable('c')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 6)


    def test_do_while_loop_interpreter(self):
        scope.__init__()
        a="""int x = 0
                do {  x ++ ; }
             while ( x < 3 ) ;"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 3)

    def test_do_while_loop_with_many_statement_interpreter(self):
        scope.__init__()
        a="""int x , b ;
                x = 0 ;
                b = 1 ;
                do {  x ++ ;
                      b ++ ; }
             while ( x < 3 ) ;"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 3)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 4)

    def test_while_loop_None_interpreter(self):
        scope.__init__()
        a="""int x = 0 ;
             while ( x == 0 )  ;
            """
        root=Cparser.parse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_do_while_loop_interpreter(self):
        scope.__init__()
        a="""int x = 0
                do { }
             while ( x < 3 ) ;"""
        root=Cparser.parse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_for_loop_withouth_declaration_interpreter(self):
        scope.__init__()
        a="""for ( x = 0 ; x == 5 ; x ++ ) ;"""
        root=Cparser.parse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_for_loop_with_declaration_interpreter(self):
        scope.__init__()
        a="""int x ;
             for ( x = 0 ; x < 5 ; x ++ ) ;"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5)


    def test_for_loop_with_working_interpreter(self):
        scope.__init__()
        a="""int x , b ;
             b = 0 ;
             for ( x = 0 ; x < 5 ; x ++ )
             {
                b ++ ;
             }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5)

    def test_for_loop_with_multiple_working_interpreter(self):
        scope.__init__()
        a="""int x , b ;
             double a ;
             for ( x = 0 ; x < 5 ; x ++ )
             {
                b ++ ;
                a = b - 1 ;
             }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['double'])
        self.assertEqual(temp[1], 4)

    def test_switch_case_chose_default_interpreter(self):
        scope.__init__()
        a=""" int choice , a ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                default    : a = 3 ; }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 3 )

    def test_switch_case_chose_default_interpreter(self):
        scope.__init__()
        a=""" int choice , a ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                default    : a = 3 ; a ++ ; }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_switch_case_chose_case1_interpreter(self):
        scope.__init__()
        a=""" int choice , a ;
            choice = 1 ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                default    : a = 3 ; }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 1 )

    def test_switch_case_chose_case1_multiple_statement_interpreter(self):
        scope.__init__()
        a=""" int choice , a ;
            choice = 1 ;
            switch ( choice )
            {
                case 1 : a = 1 ; a ++ ;
                case 2 : a = 2 ;
                default    : a = 3 ; }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 2 )


    def test_switch_case_chose_case2_interpreter(self):
        scope.__init__()
        a=""" int choice , a ;
            choice = 2 ;
            switch ( choice )
            {
                case 1 : a = 1 ; a ++ ;
                case 2 : a = 3 ; a ++ ;
                default    : a = 5 ; a ++ ; }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_switch_case_with_if_loop_interpreter(self):
        scope.__init__()
        a="""int choice , a , x ;
            choice = 2 ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                    if ( x == 0 )
                    {
                        a ++ ;
                        case 3 : a = 4 ;
                    }
                default : z = 5 ;
            } """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 3 )

    def test_switch_case_with_if_loop_true_interpreter(self):
        scope.__init__()
        a="""int choice , a , x ;
            choice = 2 ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                    if ( x == 1 )
                    {
                        a ++ ;
                        case 3 : a = 4 ;
                    }
                default : z = 5 ;
            } """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 2 )

    def test_switch_case_with_if_loop_chose_case_in_if_loop_interpreter(self):
        scope.__init__()
        a="""int choice , a , x ;
            choice = 3 ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                    if ( x == 1 )
                    {
                        a ++ ;
                        case 3 : a = 4 ;
                    }
                default : z = 5 ;
            } """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_switch_case_with_if_loop_run_statement_outside_if_interpreter(self):
        scope.__init__()
        a="""int choice , a , x ;
            choice = 3 ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                    if ( x == 1 )
                    {
                        a ++ ;
                        case 3 : a = 4 ;
                    }
                    a = 5 ;
                default : a = 6 ;
            } """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_switch_case_with_if_loop_chose_default_interpreter(self):
        scope.__init__()
        a="""int choice , a , x ;
            choice = 5 ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                    if ( x == 1 )
                    {
                        a ++ ;
                        case 3 : a = 4 ;
                    }
                    a = 5 ;
                default : a = 6 ;
            } """
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 6 )

    def test_define_only_one_statement_interpreter(self):
        scope.__init__()
        a="""#define Str  2 + 3 +
            int a = 0 ;
           { a = Str 4 }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 9 )

    def test_define_two_statement_interpreter(self):
        scope.__init__()
        a="""#define Str for ( x = 0 ; x
            int x , y , z ;
            { Str < 5 ; x ++ ) z = x + 1 ; }"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )
        temp=scope.findVariable('z')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 6 )

    def test_struct_interpreter(self):
        scope.__init__()
        a="""
            struct test {
                int a ;
                int b ; } ;
                struct test x ; """

        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['struct test'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_with_two_statement_interpreter(self):
        scope.__init__()
        a="""
            struct test2 {
                int a ;
                int b ; } ;
                struct test2 x ;
                struct test2 y ; """

        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['struct test2'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])
        temp=scope.findVariable('y')
        self.assertEqual(temp[0],symbolTable['struct test2'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_point_interpreter(self):
        scope.__init__()
        a="""
            struct test3 {
                int a ;
                int b ; } ;
                struct test3 x ;
                x . a = 3 ;
                x . b = 4 ;"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[1]['a'][1],3)
        temp=scope.findVariable('x')
        self.assertEqual(temp[1]['b'][1],4)

    def test_struct_point_interpreter(self):
        scope.__init__()
        a="""
            struct test4 {
                int a ;
                int b ; } ;
                struct test4 x ;
                x . c = 2 ;"""
        root=Cparser.parse(a)
        root[0].interpreter()
        root[1].interpreter()
        self.assertRaises(SyntaxError,root[2].interpreter)

    def test_struct_with_declaration_interpreter(self):
        scope.__init__()
        a=""" struct Datatype {
                int a ;
                int b ;
                            } data1 ;"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data1')
        self.assertEqual(temp[0],symbolTable['struct Datatype'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_with_multiple_declaration_interpreter(self):
        scope.__init__()

        a=""" struct Datatype2 {
                int a ;
                int b ;
                            } data1 , data2 ;"""
        root=Cparser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data1')
        self.assertEqual(temp[0],symbolTable['struct Datatype2'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])
        temp=scope.findVariable('data2')
        self.assertEqual(temp[0],symbolTable['struct Datatype2'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])




if __name__=='__main__':
    if test_result==True:
        unittest.main()
    elif debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter)
        unittest.TextTestRunner(verbosity=2).run(suite)