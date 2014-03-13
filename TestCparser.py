##"Files imported."                                                           ##
import unittest
import Cparser
##"Test scope."                                                               ##
"""        Test All Scope:        """
from TestTokenizer import *
from TestKeyword import *
from TestExpression import *
from TestInterpreter import *
from TestScope import *
from TestCKeywordDefine import *
from TestCKeywordStruct import *
""""""""""""""""""""""""""""""""""""""
def valueof(symObj):
    return symObj.first
##"Test start here."                                                          ##
##"set On/Off -> False = Off ; True = On."                                    ##
test_result=True
if __name__=='__main__':
    if test_result==True:
        unittest.main()
##                                                                            ##
