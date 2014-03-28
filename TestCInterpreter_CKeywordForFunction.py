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
               This module is to test -> Interpreter - Ckeyword for combined code
                                                                             """


##"Test start."                                                               ##
class TestInterpreter_CKeyword(unittest.TestCase):
    def setUp(self):
        scope.__init__()
        CParser.clearParseEnviroment()
        CParser.Initialization()

    def test_main_interpreter(self):
        a="""typedef struct {
                    int a ;
                    int b ;
                            } Data ;

           void function ( Data ) ;

           void function ( Data  data )
           {
                data . a = 2 ;
           }

           int main ( )
           {
                Data data ;
                function ( data ) ;
                return 0 ;
           }
             """
        root=CParser.Parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data')
        self.assertEqual(temp[0][0],symbolTable['Data'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['a'][1],2)

    def test_allow_redeclaration_interpreter(self):
        a="""
            int add ( int ) ;
            int add ( int ) ;
            int add ( int a )
            {
                return a ;
            }
        """
        root=CParser.Parse(a)
        Runinterpreter(root)

    def test_redeclaration_wrongly_raise_error_interpreter(self):
        a="""
            int add ( int ) ;
            int add ( double ) ;
            int add ( int a )
            {
                return a ;
            }
        """
        root=CParser.Parse(a)
        self.assertRaises(SyntaxError,Runinterpreter,root)

    def test_redeclaration_wrong_number_of_arguement_raise_error_interpreter(self):
        a="""
            int add ( int , double ) ;
            int add ( double ) ;
            int add ( int a )
            {
                return a ;
            }
        """
        root=CParser.Parse(a)
        self.assertRaises(SyntaxError,Runinterpreter,root)

    def test_two_same_function_raise_error_interpreter(self):
        a=("""
            int add ( int ) ;
            int add ( int ) ;
            int main ( )
            {
            }
            int add ( int a )
            {
                return a ;
            }
            int add ( int a )
            {
                return b ;
            }
            """)
        root=CParser.Parse(a)
        self.assertRaises(SyntaxError,Runinterpreter,root)


################################################################################
################################################################################
if __name__=='__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter_CKeyword)
        unittest.TextTestRunner(verbosity=2).run(suite)
