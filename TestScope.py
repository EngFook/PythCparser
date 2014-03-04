import unittest
import Cparser
from Tokenizer import *
def valueof(symObj):
    return symObj.first

test_result=True
debug_all=True

class TestScope(unittest.TestCase):
    def test_nth(self):
        pass

if __name__=='__main__':
    if test_result==True:
        unittest.main()
    elif debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter)
        unittest.TextTestRunner(verbosity=2).run(suite)