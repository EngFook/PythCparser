import unittest
import Cparser
from TestTokenizer import *
from TestKeyword import *
from TestExpression import *
from Tokenizer import *
def valueof(symObj):
    return symObj.first

#set On/Off -> False = Off ; True = On
#To verify test_result:
test_result=True
################################################################################
################################################################################
################################################################################
# Test -> Tokenizer,Keyword,Expression by importing files.
################################################################################

if __name__=='__main__':
    if test_result==True:
        unittest.main()

