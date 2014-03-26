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
                     This module is to test -> Interpreter - CExpression
                                                                             """

##"Test start."                                                               ##
class TestInterpreter_CExpression(unittest.TestCase):
    def test_plus_interpreter(self):
        a=" 2 + 3 ;"
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,5.0)

    def test_plus_multiply_interpreter(self):
        a=" 2 + 3 * 4 ;"
        """       +
                /   \
              2      *
                    /  \
                  3      4"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,14)

    def test_postfix_negative_interpreter(self):
        a="- 1 ;"
        """ -
            |
            1"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,-1)

    def test_multiply_interpreter(self):
        a=" 2 ** 2 ** 3 ;"
        """       **
                /   \
              2      **
                    /  \
                  2      3"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,256)
        two=root[0].first
        value=two.interpreter()
        self.assertEqual(value,2)
        eight=root[0].second
        value=eight.interpreter()
        self.assertEqual(value,8)
        two=eight.first
        value=two.interpreter()
        self.assertEqual(value,2)
        three=eight.second
        value=three.interpreter()
        self.assertEqual(value,3)

    def test_braceket_interpreter(self):
        a=" ( 2 + 3 ) * 4 ;"
        """     *
              /    \
             (      4
             |
             +
           /   \
          2     3 """
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,20)
        bracket=root[0].first
        value=bracket.interpreter()
        self.assertEqual(value,5)
        four=root[0].second
        value=four.interpreter()
        self.assertEqual(value,4)
        plus=bracket.first
        value=plus.interpreter()
        self.assertEqual(value,5)
        two=plus.first
        value=two.interpreter()
        self.assertEqual(value,2)
        three=plus.second
        value=three.interpreter()
        self.assertEqual(value,3)

    def test_equalequal_condition_interpreter(self):
        a=" 1 == 1 ;"
        """ ==
           /  \
          1    1"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertTrue(value)

    def test_bigger_condition_interpreter(self):
        a=" 2 > 1 ;"
        """ >
           /  \
          2    1"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertTrue(value)

    def test_smaller_condition_interpreter(self):
        a=" 2 < 1 ;"
        """ <
           /  \
          2    1"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertFalse(value)

    def test_biggerequal_condition_interpret(self):
        a=" 2 >= 1 ;"
        """ >=
           /  \
          2    1"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertTrue(value)

    def test_smallerequal_condition_interpreter(self):
        a=" 2 < 1 ;"
        """ <=
           /  \
          2    1"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertFalse(value)

    def test_shiftleft_bit_interpreter(self):
        a=" 1 << 3 ;"
        """ <<
           /  \
          1    3"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,8)

    def test_shiftright_bit_interpreter(self):
        a=" 8 >> 3 ;"
        """ >>
           /  \
          8    3"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,1)

    def test_and_bit_interpreter(self):
        a=" 5 & 6 ;"
        """ &
           /  \
          5    6"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,4)

    def test_xor_bit_interpreter(self):
        a=" ~ 2 ;"
        """ ~
            |
            2"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,-3)

    def test_not_bit_interpreter(self):
        a=" ! 2 ;"
        """ !
            |
            2"""
        root=CParser.oneTimeParse(a)
        value=root[0].interpreter()
        self.assertEqual(value,0)

    def test_braces_interpreter(self):
        a="""{
                1 + 2 ;
                2 + 3 ;
             }"""
        """ {
            |------- +
            |       / \
            |      1   2
            |--------+
                    / \
                   2   3"""

        root=CParser.oneTimeParse(a)
        three=root[0].first[0].interpreter()
        five=root[0].first[1].interpreter()
        self.assertEqual(three,3)
        self.assertEqual(five,5)

    def test_array_interpreter(self):
        a="""int a [ ] ;"""
################################################################################
################################################################################
if __name__=='__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter_CExpression)
        unittest.TextTestRunner(verbosity=2).run(suite)
