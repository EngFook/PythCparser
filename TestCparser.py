##"Files imported."                                                           ##
import unittest
import CParser
##"Test all here."                                                            ##
"""                         Add Test Module Here:                            """
from TestCScope import *
from TestTokenizer import *
from TestCExpression import *
from TestCKeyword_enum import *
from TestCKeyword_type import *
from TestCKeyword_define import *
from TestCKeyword_struct import *
from TestCKeyword_typedef import *
from TestCKeyword_if_else import *
from TestCKeyword_do_while import *
from TestCKeyword_for_loop import *
from TestCKeyword_switch_case import *
from TestCInterpreter_CKeyword import *
from TestCInterpreter_CExpression import *
from TestCInterpreter_CKeywordForFunction import *
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
                                Test start here

                                                                             """
def valueof(symObj):
    return symObj.first

if __name__=='__main__':
        unittest.main()