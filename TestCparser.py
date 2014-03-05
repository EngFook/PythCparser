import unittest
import Cparser
from TestTokenizer import *
from TestKeyword import *
from TestExpression import *
from TestInterpreter import *
from TestScope import *
from Tokenizer import *
from TestCKeywordDefine import *
def valueof(symObj):
    return symObj.first

test_result=True

if __name__=='__main__':
    if test_result==True:
        unittest.main()

