##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
from CScope import *
from CInterperter import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
               This module is to test -> Interpreter - Ckeyword
                                                                             """


##"Test start."                                                               ##
class TestInterpreter_CKeyword(unittest.TestCase):
    def setUp(self):
        scope.__init__()
        CParser.clearParseEnviroment()

    def test_int_a_double_b_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],2)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0][0],symbolTable['double'])
        self.assertEqual(temp[1],3)

    def test_with_assigened_indentfier_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        root[0].interpreter()
        three=root[1].interpreter()
        self.assertEqual(three,3)

    def test_minusminus_after_literal_indentfier_interpreter(self):
        a="10 -- ;"
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_minusminus_before_literal_indentfier_interpreter(self):
        a="-- 10 ;"
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_minusminus_after_indentifier_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        root[0].interpreter()
        five=root[1].interpreter()
        self.assertEqual(five,5)
        three=root[2].interpreter()
        self.assertEqual(three,3)

    def test_equal_without_int_error_interpreter(self):
        a="a = 1 ;"
        """ =
          /   \
         a     1 """
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_int_a_without_value_interpreter(self):
        a="int a ;"
        """int-a"""
        root=CParser.oneTimeParse(a)
        root[0].interpreter()
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],0)

    def test_declate_twice_raise_error_interpreter(self):
        a="""int a ;
             double a ;"""
        root=CParser.oneTimeParse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_equal_with_int_interpreter(self):
        a="int a = 1 ;"
        """     =
              /   \
          int-a    1 """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],1)

    def test_int_a_with_a_divide_by_two_interpreter(self):
        a="""int a = 1 ;
            a = a / 2 ;
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],0)

    def test_equal_with_int_zero_point_nine_interpreter(self):
        a="int a = 0.9 ;"
        """     =
              /   \
          int-a    1 """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],0)

    def test_equal_with_double_zero_point_nine_interpreter(self):
        a="double a = 0.9 ;"
        """     =
              /   \
          double-a    1 """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['double'])
        self.assertEqual(temp[1],0.9)


    def test_int_a_with_negative_value_interpreter(self):
        a="int a = -1 ;"
        """     =
              /   \
          int-a    1 """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],-1)

    def test_int_a_b_c_interpreter(self):
        a="int a , b , c ;"
        """int-a"""
        root=CParser.oneTimeParse(a)
        root[0].interpreter()
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],0.)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],0.)
        temp=scope.findVariable('c')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],0.)

    def test_int_a_with_value_plusplus_interpreter(self):
        a="""int a = 1 ;
            a ++ ;"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1] , 2 )

    def test_if_false_interpreter(self):
        a="""
                int a = 5 ;
                if ( 0 ) a = 4 ;
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )


    def test_if_true_interpreter(self):
        a="""
                int a = 5 ;
                if ( 1 ) a = 4 ;
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_if_with_else_interpreter(self):
        a="""
                int a = 5 ;
                if ( 0 ) a = 4 ;
                else  a = 3 ;
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 3 )


    def test_if_with_else_if_true_interpreter(self):
        a="""
               int a = 5 ;
               if ( 0 ) a = 4 ;
               else if ( 1 ) a = 3 ;
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 3 )

    def test_if_with_else_if_false_interpreter(self):
        a="""
               int a = 5 ;
               if ( 0 ) a = 4 ;
               else
                    if ( 0 ) a = 3 ;
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_if_with_condition_interpreter(self):
        a="""
                int a = 5 ;
                if ( a == 1 ) a = 4 ;
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_if_with_condition_many_statement_interpreter(self):
        a="""
                int a = 1 ;
                if ( a == 1 )
                {
                    a = 4 ;
                    a ++ ;
                }
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_while_interpreter(self):
        a="""int x = - 1 ;
            while ( x < 1 ) x ++ ;
            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 1 )

    def test_while_infinity_lopp_raise_syntax_interpreter(self):
        a="""int x = 0 ;
             while ( 1 ) x ++ ;
            """
        root=CParser.oneTimeParse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_while_loop_with_many_statment_interpreter(self):
        a="""int x = 0 ;
             while ( x < 4 )
             {
                     x ++ ;
                     x -- ;
                     x ++ ;
             }

            """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_while_loop_with_many_statment_diff_variable_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )
        temp=scope.findVariable('b')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5)
        temp=scope.findVariable('c')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 6)

    def test_do_while_loop_interpreter(self):
        a="""int x = 0 ;
                do {  x ++ ; }
             while ( x < 3 ) ;  """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 3)

    def test_do_while_loop_with_many_statement_interpreter(self):
        a="""int x , b ;
                x = 0 ;
                b = 1 ;
                do {  x ++ ;
                      b ++ ; }
             while ( x < 3 ) ;"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 3)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 4)

    def test_while_loop_None_interpreter(self):
        a="""int x = 0 ;
             while ( x == 0 )  ;
            """
        root=CParser.oneTimeParse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_do_while_loop_interpreter_2nd(self):
        a="""int x = 0 ;
                do { }
             while ( x < 3 ) ;"""
        root=CParser.oneTimeParse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_for_loop_withouth_declaration_interpreter(self):
        a="""for ( x = 0 ; x == 5 ; x ++ ) ;"""
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_for_loop_with_declaration_interpreter(self):
        a="""int x ;
             for ( x = 0 ; x < 5 ; x ++ ) ;"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5)


    def test_for_loop_with_working_interpreter(self):
        a="""int x , b ;
             b = 0 ;
             for ( x = 0 ; x < 5 ; x ++ )
             {
                b ++ ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5)

    def test_for_loop_with_multiple_working_interpreter(self):
        a="""int x , b ;
             double a ;
             for ( x = 0 ; x < 5 ; x ++ )
             {
                b ++ ;
                a = b - 1 ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['double'])
        self.assertEqual(temp[1], 4)

    def test_switch_case_chose_default_interpreter(self):
        a=""" int choice , a ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                default    : a = 3 ; }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 3 )

    def test_switch_case_chose_default_interpreter(self):
        a=""" int choice , a ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                default    : a = 3 ; a ++ ; }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_switch_case_chose_case1_interpreter(self):
        a=""" int choice , a ;
            choice = 1 ;
            switch ( choice )
            {
                case 1 : a = 1 ;
                case 2 : a = 2 ;
                default    : a = 3 ; }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 1 )

    def test_switch_case_chose_case1_multiple_statement_interpreter(self):
        a=""" int choice , a ;
            choice = 1 ;
            switch ( choice )
            {
                case 1 : a = 1 ; a ++ ;
                case 2 : a = 2 ;
                default    : a = 3 ; }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 2 )


    def test_switch_case_chose_case2_interpreter(self):
        a=""" int choice , a ;
            choice = 2 ;
            switch ( choice )
            {
                case 1 : a = 1 ; a ++ ;
                case 2 : a = 3 ; a ++ ;
                default    : a = 5 ; a ++ ; }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_switch_case_with_if_loop_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 3 )

    def test_switch_case_with_if_loop_true_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 2 )

    def test_switch_case_with_if_loop_chose_case_in_if_loop_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 4 )

    def test_switch_case_with_if_loop_run_statement_outside_if_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_switch_case_with_if_loop_chose_default_interpreter(self):
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
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 6 )

    def test_define_only_one_statement_interpreter(self):
        a="""#define Str  2 + 3 +
            int a = 0 ;
           { a = Str 4 }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 9 )

    def test_define_two_statement_interpreter(self):
        a="""#define Str for ( x = 0 ; x
            int x , y , z ;
            { Str < 5 ; x ++ ) z = x + 1 ; }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )
        temp=scope.findVariable('z')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1], 6 )

    def test_struct_interpreter(self):
        a="""
            struct test {
                int a ;
                int b ; } ;
                struct test x ; """

        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['struct test'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_with_two_statement_interpreter(self):
        a="""
            struct test {
                int a ;
                int b ; } ;
                struct test x ;
                struct test y ; """

        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['struct test'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])
        temp=scope.findVariable('y')
        self.assertEqual(temp[0][0],symbolTable['struct test'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_point_interpreter(self):
        a="""
            struct test {
                int a ;
                int b ; } ;
                struct test x ;
                x . a = 3 ;
                x . b = 4 ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[1]['a'][1],3)
        temp=scope.findVariable('x')
        self.assertEqual(temp[1]['b'][1],4)

    def test_struct_with_declaration_interpreter(self):
        a=""" struct Datatype {
                int a ;
                int b ;
                            } data1 ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data1')
        self.assertEqual(temp[0][0],symbolTable['struct Datatype'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_with_multiple_declaration_interpreter(self):
        a=""" struct Datatype {
                int a ;
                int b ;
                            } data1 , data2 ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data1')
        self.assertEqual(temp[0][0],symbolTable['struct Datatype'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])
        temp=scope.findVariable('data2')
        self.assertEqual(temp[0][0],symbolTable['struct Datatype'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_typedef_interpreter(self):
        a= """typedef struct {
                        int a ;
                        int b ;
                                } Data ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['Data'].id,'Data')
        self.assertEqual(symbolTable['Data'].second.first[0].first.first,'a')
        self.assertEqual(symbolTable['Data'].second.first[1].first.first,'b')

    def test_typedef_datatype_interpreter(self):
        a="""typedef struct Datatype1 {
                    int a ;
                    int b ;
                            } Datatype ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['Datatype'].id,'Datatype')
        self.assertEqual(symbolTable['Datatype'].second.first[0].first.first,'a')
        self.assertEqual(symbolTable['Datatype'].second.first[1].first.first,'b')
        self.assertEqual(symbolTable['struct Datatype1'].id,'struct Datatype1')
        self.assertEqual(symbolTable['struct Datatype1'].second.first[0].first.first,'a')
        self.assertEqual(symbolTable['struct Datatype1'].second.first[1].first.first,'b')

    def test_typedef_interpreter(self):
        a="""typedef struct {
                    int a ;
                    int b ;
                            } Data2 ;
                    Data2 x ; """
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['Data2'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
##        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_typedef_struct_with_two_declaration_interpreter(self):
        a="""typedef struct {
                    int a ;
                    int b ;
                            } Data3 ;
                    Data3 x ;
                    typedef Data3 y ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['Data3'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])
        temp=scope.findVariable('y')
        self.assertEqual(temp[0][0],symbolTable['Data3'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_enum_with_workdays_interpreter(self):
        a=""" enum DAY {
                            saturday ,
                            sunday
                                        } workday ; """
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('workday')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],None)

    def test_enum_with_two_variable_interpreter(self):
        a=""" enum DAY {
                            saturday ,
                            sunday
                                        } workday , weekend ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('workday')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],None)
        temp=scope.findVariable('weekend')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],None)

    def test_enum_with_no_variable_interpreter(self):
        a=""" enum DAY {
                            saturday ,
                            sunday
                                        } ; """
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')

    def test_enum_with_variable_declare_interpreter(self):
        a=""" enum DAY
                        {
                            saturday ,
                            sunday = 0  ,
                            friday
                                        } workday ;

                enum DAY x ; """
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],0)

    def test_enum_with_variable_assign_with_integer_directly_interpreter(self):
        a=""" enum DAY
                        {
                            saturday ,
                            sunday = 0  ,
                            friday
                                        } workday ;

                enum DAY x = 1 ; """
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],1)

    def test_enum_with_variable_assign_with_integer_interpreter(self):
        a=""" enum DAY
                        {
                            saturday ,
                            sunday = 0  ,
                            friday
                                        } workday ;

                enum DAY x ;
                x = 1 ; """
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],1)

    def test_enum_with_variable_assign_with_integer_interpreter(self):
        a=""" enum DAY
                        {
                            saturday ,
                            sunday ,
                            friday
                                        } workday ;

                enum DAY x = saturday ; """
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],0)

    def test_enum_with_two_variable_assign_with_integer_interpreter(self):
        a=""" enum DAY
                        {
                            saturday ,
                            sunday = 0  ,
                            friday
                                        } workday ;

                enum DAY x = sunday ;
                enum DAY y = friday ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],0)
        temp=scope.findVariable('y')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],1)
        CParser.clearParseEnviroment()

    def test_struct_inside_a_struct_interpreter(self):
        a="""        typedef struct {
                    float x ;
                    float y ;
                    } coordinate ;

                   typedef struct Data {
                   int a ;
                   int  b ;
                   double c ;
                   coordinate d ;
                   } Data ;

                   int main ( ) {
                   Data data ;
                                      } """

        root=CParser.Parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data')
        self.assertEqual(temp[0][0],symbolTable['Data'])
        self.assertEqual(temp[1]['d'][0],symbolTable['coordinate'])
        self.assertEqual(temp[1]['d'][1]['x'][0],symbolTable['float'])
        self.assertEqual(temp[1]['d'][1]['y'][0],symbolTable['float'])

    def test_struct_inside_a_struct_interpreter(self):
        a="""        typedef struct {
                    float x ;
                    float y ;
                    } coordinate ;

                   typedef struct Data {
                   int a ;
                   int  b ;
                   double c ;
                   coordinate d ;
                   } Data ;
                   int main ( ) {
                   Data data ;
                   data . d . x = 3 ;
                   data . c = 4 ;
                                      } """

        root=CParser.Parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data')
        self.assertEqual(temp[0][0],symbolTable['Data'])
        self.assertEqual(temp[1]['d'][0],symbolTable['coordinate'])
        self.assertEqual(temp[1]['d'][1]['x'][0],symbolTable['float'])
        self.assertEqual(temp[1]['d'][1]['x'][1],3)
        self.assertEqual(temp[1]['c'][0],symbolTable['double'])
        self.assertEqual(temp[1]['c'][1],4)

    def test_struct_assign_struct_to_variable_interpreter(self):
        a="""        typedef struct {
                    float x ;
                    float y ;
                    } coordinate ;

                   typedef struct Data {
                   int a ;
                   int  b ;
                   double c ;
                   coordinate d ;
                   } Data ;

                   int main ( ) {
                   Data data ;
                   int z ;
                   data . c = 3 ;
                   z = data . c ;
                                      } """

        root=CParser.Parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data')
        self.assertEqual(temp[0][0],symbolTable['Data'])
        self.assertEqual(temp[1]['c'][0],symbolTable['double'])
        self.assertEqual(temp[1]['c'][1],3)
        temp=scope.findVariable('z')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],3)

    def test_struct_assign_struct_to_variable_struct_in_sturct_interpreter(self):
        a="""        typedef struct {
                    float x ;
                    float y ;
                    } coordinate ;

                   typedef struct Data {
                   int a ;
                   int  b ;
                   double c ;
                   coordinate d ;
                   } Data ;

                   int main ( ) {
                   Data data ;
                   int z ;
                   data . d . x = 3 ;
                   z = data . d . x ;
                                      } """

        root=CParser.Parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('z')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],3)

    def test_enum_with_x_and_y_interpreter(self):
        a=''' enum DAY {
                            saturday ,
                            sunday
                                        } ;
             enum DAY x , y  ;'''
        root=CParser.Parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],0)
        temp=scope.findVariable('y')
        self.assertEqual(temp[0][0],symbolTable['enum DAY'])
        self.assertEqual(temp[1],0)


    def test_main_function_interpreter(self):
        a=""" int main ( )
                {
                    int a ;
                    a = 3 ;
                }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],3)

    def test_add_function_declaration_interpreter(self):
        a="""int add ( int , int ) ;
            int add ( int a , int b ) { }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('add')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],root[1])

    def test_add_function_declaration_raise_error_interpreter(self):
        a="""int add ( int , int ) ;
            int add ( int a , int b , int c ) { }"""
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,root[0].interpreter,root)

    def test_add_function_declaration_raise_error_interpreter(self):
        a="""int add ( int , int ) ;
            int add ( int a , int b , int c ) { }"""
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,root[0].interpreter,root)

    def test_add_function_declaration_raise_error2_interpreter(self):
        a="""int add ( int , int ) ;
            double add ( int a , int b ) { }"""
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,root[0].interpreter,root)

    def test_add_function_declaration_raise_error3_interpreter(self):
        a="""int add ( int , int ) ;
             int add ( int a , double b ) { }"""
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,root[0].interpreter,root)

    def test_call_function_interpreter(self):
        a="""int add ( int , int ) ;
             int main ( )
             {
                int a ;
                a = add ( 2 , 3 ) ;
                return 0 ;
             }

             int add ( int a , int b )
             {
                return a + b ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],5)

    def test_call_function_twice_interpreter(self):
        a="""int add ( int , int ) ;
             int main ( )
             {
                int a ;
                a = add ( 2 , 3 ) + add ( 3 , 4 ) ;
                return 0 ;
             }

             int add ( int a , int b )
             {
                return a + b ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],12)


    def test_int_a_b_c_equal_2_3_interpreter(self):
        a="""int a = 1 , b , c = 4 ; """
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],1)
        temp=scope.findVariable('b')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],0)
        temp=scope.findVariable('c')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],4)

    def test_int_limit_interpreter(self):
        a="""int main ( )
             {
                short int a , b ;
                unsigned short int c , d ;
                unsigned int e , f ;
                int g , h ;
                long int i , j ;
                a = 70000 ;
                b = - 70000 ;
                c = 70000 ;
                d = - 70000 ;
                e = 5000000000 ;
                f = - 5000000000 ;
                g = 5000000000 ;
                h = - 5000000000 ;
                i = 5000000000 ;
                j = - 5000000000 ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],32767)
        temp=scope.findVariable('b')
        self.assertEqual(temp[1],-32768)
        temp=scope.findVariable('c')
        self.assertEqual(temp[1],65535)
        temp=scope.findVariable('d')
        self.assertEqual(temp[1],0)
        temp=scope.findVariable('e')
        self.assertEqual(temp[1],4294967295)
        temp=scope.findVariable('f')
        self.assertEqual(temp[1],0)
        temp=scope.findVariable('g')
        self.assertEqual(temp[1],2147483647)
        temp=scope.findVariable('h')
        self.assertEqual(temp[1],-2147483648)
        temp=scope.findVariable('i')
        self.assertEqual(temp[1],2147483647)
        temp=scope.findVariable('j')
        self.assertEqual(temp[1],-2147483648)

    def test_char_limit_interpreter(self):
        a="""int main ( )
             {
                signed char a , b ;
                unsigned char c , d ;
                a = 300 ;
                b = - 300 ;
                c = 300 ;
                d = - 300 ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],127)
        temp=scope.findVariable('b')
        self.assertEqual(temp[1],-128)
        temp=scope.findVariable('c')
        self.assertEqual(temp[1],255)
        temp=scope.findVariable('d')
        self.assertEqual(temp[1],0)

    def test_int_limit_assign_after_declare_interpreter(self):
        a="""int main ( )
             {
                short int a = 70000 , b = - 70000 ;
                unsigned short int c = 70000 , d = - 70000 ;
                unsigned int e = 5000000000 , f = - 5000000000 ;
                int g = 5000000000 , h = - 5000000000 ;
                long int i = 5000000000 , j = - 5000000000 ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],32767)
        temp=scope.findVariable('b')
        self.assertEqual(temp[1],-32768)
        temp=scope.findVariable('c')
        self.assertEqual(temp[1],65535)
        temp=scope.findVariable('d')
        self.assertEqual(temp[1],0)
        temp=scope.findVariable('e')
        self.assertEqual(temp[1],4294967295)
        temp=scope.findVariable('f')
        self.assertEqual(temp[1],0)
        temp=scope.findVariable('g')
        self.assertEqual(temp[1],2147483647)
        temp=scope.findVariable('h')
        self.assertEqual(temp[1],-2147483648)
        temp=scope.findVariable('i')
        self.assertEqual(temp[1],2147483647)
        temp=scope.findVariable('j')
        self.assertEqual(temp[1],-2147483648)

    def test_char_limit_assign_after_declare_interpreter(self):
        a="""int main ( )
             {
                signed char a = 300 , b = - 300 ;
                unsigned char c = 300 , d = - 300 ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[1],127)
        temp=scope.findVariable('b')
        self.assertEqual(temp[1],-128)
        temp=scope.findVariable('c')
        self.assertEqual(temp[1],255)
        temp=scope.findVariable('d')
        self.assertEqual(temp[1],0)

    def test_declare_function_have_variable_interpreter(self):
        a="""int add ( int c , int d ) ;
             int main ( )
             {
                int a ;
                a = add ( 2 , 3 ) + add ( 3 , 4 ) ;
                return 0 ;
             }

             int add ( int a , int b )
             {
                return a + b ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0][0],symbolTable['int'])
        self.assertEqual(temp[1],12)

    def test_return_for_void_interpreter(self):
        a="""void donothing ( int c , int d ) ;
             int main ( )
             {
                donothing ( 3 , 4 ) ;
                return 0 ;
             }

             void donothing ( int a , int b )
             {
                return 0 ;
             }"""
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,Runinterpreter,root)

    def test_retrun_for_int_interpreter(self):
        a="""int donothing ( int c , int d ) ;
             int main ( )
             {
                donothing ( 3 , 4 ) ;
                return 0 ;
             }

             int donothing ( int a , int b )
             {
               a = b  ;
             }"""
        root=CParser.oneTimeParse(a)
        self.assertRaises(SyntaxError,Runinterpreter,root)

    def test_main_interpreter(self):
        a="""int donothing ( int c , int d ) ;
             int main ( )
             {
                donothing ( 3 , 4 ) ;
             }

             int donothing ( int a , int b )
             {
               return a  ;
             }"""
        root=CParser.oneTimeParse(a)
        Runinterpreter(root)

################################################################################
################################################################################
if __name__=='__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter_CKeyword)
        unittest.TextTestRunner(verbosity=2).run(suite)
