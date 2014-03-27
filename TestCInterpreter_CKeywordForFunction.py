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
           }     """
        root=CParser.Parse(a)
        Runinterpreter(root)
        temp=scope.findVariable('data')
        self.assertEqual(temp[0][0],symbolTable['Data'])
        self.assertEqual(temp[1]['a'][0],symbolTable['int'])
        self.assertEqual(temp[1]['a'][1],2)

################################################################################
################################################################################
if __name__=='__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter_CKeyword)
        unittest.TextTestRunner(verbosity=2).run(suite)
