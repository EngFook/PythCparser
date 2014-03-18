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
               This module is to test -> Interpreter - operator
                                                                             """
##"Interpreter the array root[i],i=1,2,3,...                                  ##
def Runinterpreter(self):
    index=0
    while index < self.__len__():
        self[index].interpreter()
        index = index + 1
##"Test start."                                                               ##
class TestInterpreter_operator(unittest.TestCase):

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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
        root[0].interpreter()
        three=root[1].interpreter()
        self.assertEqual(three,3)

    def test_minusminus_after_literal_indentfier_interpreter(self):
        a="10 -- ;"
        root=CParser.parse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_minusminus_before_literal_indentfier_interpreter(self):
        a="-- 10 ;"
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_int_a_without_value_interpreter(self):
        scope.__init__()
        a="int a ;"
        """int-a"""
        root=CParser.parse(a)
        root[0].interpreter()
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],0)

    def test_declate_twice_raise_error_interpreter(self):
        scope.__init__()
        a="""int a ;
             double a ;"""
        root=CParser.parse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_equal_with_int_interpreter(self):
        scope.__init__()
        a="int a = 1 ;"
        """     =
              /   \
          int-a    1 """
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],1)

    def test_int_a_with_a_divide_by_two_interpreter(self):
        scope.__init__()
        a="""int a = 1 ;
            a = a / 2 ;
            """
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1],-1)

    def test_int_a_b_c_interpreter(self):
        scope.__init__()
        a="int a , b , c ;"
        """int-a"""
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 5 )

    def test_while_interpreter(self):
        scope.__init__()
        a="""int x = - 1 ;
            while ( x < 1 ) x ++ ;
            """
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 1 )

    def test_while_infinity_lopp_raise_syntax_interpreter(self):
        scope.__init__()
        a="""int x = 0 ;
             while ( 1 ) x ++ ;
            """
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_do_while_loop_interpreter(self):
        scope.__init__()
        a="""int x = 0
                do { }
             while ( x < 3 ) ;"""
        root=CParser.parse(a)
        root[0].interpreter()
        self.assertRaises(SyntaxError,root[1].interpreter)

    def test_for_loop_withouth_declaration_interpreter(self):
        scope.__init__()
        a="""for ( x = 0 ; x == 5 ; x ++ ) ;"""
        root=CParser.parse(a)
        self.assertRaises(SyntaxError,root[0].interpreter)

    def test_for_loop_with_declaration_interpreter(self):
        scope.__init__()
        a="""int x ;
             for ( x = 0 ; x < 5 ; x ++ ) ;"""
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 6 )

    def test_define_only_one_statement_interpreter(self):
        scope.__init__()
        a="""#define Str  2 + 3 +
            int a = 0 ;
           { a = Str 4 }"""
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('a')
        self.assertEqual(temp[0],symbolTable['int'])
        self.assertEqual(temp[1], 9 )

    def test_define_two_statement_interpreter(self):
        scope.__init__()
        a="""#define Str for ( x = 0 ; x
            int x , y , z ;
            { Str < 5 ; x ++ ) z = x + 1 ; }"""
        root=CParser.parse(a)
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

        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['struct test'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_with_two_statement_interpreter(self):
        scope.__init__()
        a="""
            struct test {
                int a ;
                int b ; } ;
                struct test x ;
                struct test y ; """

        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['struct test'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])
        temp=scope.findVariable('y')
        self.assertEqual(temp[0],symbolTable['struct test'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_point_interpreter(self):
        scope.__init__()
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

    def test_struct_point_with_undeclared_variable_interpreter(self):
        scope.__init__()
        a="""
            struct test {
                int a ;
                int b ; } ;
                struct test x ;
                x . c = 2 ;"""
        root=CParser.parse(a)
        root[0].interpreter()
        root[1].interpreter()
        self.assertRaises(SyntaxError,root[2].interpreter)

    def test_struct_with_declaration_interpreter(self):
        scope.__init__()
        a=""" struct Datatype {
                int a ;
                int b ;
                            } data1 ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data1')
        self.assertEqual(temp[0],symbolTable['struct Datatype'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_struct_with_multiple_declaration_interpreter(self):
        scope.__init__()
        a=""" struct Datatype {
                int a ;
                int b ;
                            } data1 , data2 ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data1')
        self.assertEqual(temp[0],symbolTable['struct Datatype'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])
        temp=scope.findVariable('data2')
        self.assertEqual(temp[0],symbolTable['struct Datatype'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_typedef_interpreter(self):
        scope.__init__()
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
        scope.__init__()
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
        scope.__init__()
        a="""typedef struct {
                    int a ;
                    int b ;
                            } Data2 ;
                    Data2 x ; """
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['Data2'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_typedef_struct_with_two_declaration_interpreter(self):
        scope.__init__()
        a="""typedef struct {
                    int a ;
                    int b ;
                            } Data3 ;
                    Data3 x ;
                    typedef Data3 y ;"""
        root=CParser.parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('x')
        self.assertEqual(temp[0],symbolTable['Data3'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])
        temp=scope.findVariable('y')
        self.assertEqual(temp[0],symbolTable['Data3'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['b'][0],symbolTable['int'])

    def test_enum_with_workdays_interpreter(self):
        scope.__init__()
        a=''' enum DAY {
                            saturday ,
                            sunday
                                        } workday ; '''
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('workday')
        self.assertEqual(temp[0],symbolTable['enum DAY'])
        self.assertEqual(valueof(temp[1][0]),'saturday')
        self.assertEqual(valueof(temp[1][1]),'sunday')

    def test_enum_with_two_variable_interpreter(self):
        scope.__init__()
        a=''' enum DAY {
                            saturday ,
                            sunday
                                        } workday , weekend ; '''
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
        temp=scope.findVariable('workday')
        self.assertEqual(temp[0],symbolTable['enum DAY'])
        self.assertEqual(valueof(temp[1][0]),'saturday')
        self.assertEqual(valueof(temp[1][1]),'sunday')
        temp=scope.findVariable('weekend')
        self.assertEqual(temp[0],symbolTable['enum DAY'])
        self.assertEqual(valueof(temp[1][0]),'saturday')
        self.assertEqual(valueof(temp[1][1]),'sunday')

    def test_enum_with_no_variable_interpreter(self):
        scope.__init__()
        a=''' enum DAY {
                            saturday ,
                            sunday
                                        } ; '''
        root=CParser.parse(a)
        Runinterpreter(root)
        self.assertEqual(symbolTable['enum DAY'].id,'enum DAY')
################################################################################
################################################################################
if __name__=='__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter_operator)
        unittest.TextTestRunner(verbosity=2).run(suite)