##"Files imported."                                                           ##
import unittest
import Cparser
##"Test all here."                                                            ##
"""          Add Test Module Here:       """
from TestScope import *
from TestKeyword import *
from TestTokenizer import *
from TestExpression import *
#from TestInterpreter import *
from TestCKeywordDefine import *
from TestCKeywordStructEnumTypedef import *
""""""""""""""""""""""""""""""""""""""""""""
"""
    Test start here.
    set On/Off -> False = Off ; True = On.

                                          """
test_result=True
def valueof(symObj):
    return symObj.first

if __name__=='__main__':
    if test_result==True:
        unittest.main()