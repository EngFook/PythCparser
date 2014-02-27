import unittest
import Cparser
from Tokenizer import *
def valueof(symObj):
    return symObj.first

#set On/Off -> False = Off ; True = On
#To verify test_result:
test_result=True
#To debug_all,set test_result = False:
debug_all=True
################################################################################
##[Mixing style]################################################################
################################################################################
# Test -> Expression
################################################################################
class TestInterpreter(unittest.TestCase):
    def testIndentifierInter(self):
        a=" 2 + 3 ;"
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,5)
        two=root.first
        value=two.interpreter()
        self.assertEqual(value,2)
        three=root.second
        value=three.interpreter()
        self.assertEqual(value,3)


    def testIndentifierInter(self):
        a=" 2 + 3 * 4 ;"
        """       +
                /   \
              2      *
                    /  \
                  3      4"""
        root=Cparser.parse(a)
        print(root)
        value=root.interpreter()
        self.assertEqual(value,14)
        two=root.first.interpreter()
        self.assertEqual(two,2)
        twelve=root.second.interpreter()
        self.assertEqual(twelve,12)
        three=root.second.first
        value=three.interpreter()
        self.assertEqual(value,3)
        four=root.second.second
        value=four.interpreter()
        self.assertEqual(value,4)

if __name__=='__main__':
    if test_result==True:
        unittest.main()
    elif debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter)
        unittest.TextTestRunner(verbosity=2).run(suite)