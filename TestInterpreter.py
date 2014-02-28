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
    def test_plus_interpreter(self):
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


    def test_plus_multiply_interpreter(self):
        a=" 2 + 3 * 4 ;"
        """       +
                /   \
              2      *
                    /  \
                  3      4"""
        root=Cparser.parse(a)
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

    def test_postfix_negative_interpreter(self):
        a="- 1 ;"
        """ -
            |
            1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,-1)
        one=root.first
        value=one.interpreter()
        self.assertEqual(value,1)

    def test_postfix_negative_and_divide_interpreter(self):
        a="- 1 / 4 ;"
        """    '/'
              /  \
             -    4
             |
             1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,-0.25)
        negative=root.first
        value=negative.interpreter()
        self.assertEqual(value,-1)
        one=negative.first
        value=one.interpreter()
        self.assertEqual(value,1)
        four=root.second
        value=four.interpreter()
        self.assertEqual(value,4)

    def test_pointer_interpreter(self):
        a="* ptr ;"
        """     *
                |
                ptr"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,"this is the pointer of {0}".format("ptr"))
        ptr=root.first
        value=ptr.interpreter()
        self.assertEqual(value,"ptr")

    def test_plus_before_return_interpreter(self):
        a="10 -- - -- 10 ;"
        """     +
               /  \
             --   --
             |     |
             10    10"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,1)
        postfix10=root.first
        value=postfix10.interpreter()
        self.assertEqual(value,10)
        prefix10=root.second
        value=prefix10.interpreter()
        self.assertEqual(value,9)

    def test_plus_before_return_interpreter(self):
        a=" 2 ** 2 ** 3 ;"
        """       **
                /   \
              2      **
                    /  \
                  2      3"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,256)
        two=root.first
        value=two.interpreter()
        self.assertEqual(value,2)
        eight=root.second
        value=eight.interpreter()
        self.assertEqual(value,8)
        two=eight.first
        value=two.interpreter()
        self.assertEqual(value,2)
        three=eight.second
        value=three.interpreter()
        self.assertEqual(value,3)

    def test_equal_interpreter(self):
        a=" a = 1 ;"
        """     =
              /   \
             a     1 """
        root=Cparser.parse(a)
        value=root.interpreter()
        a=value.first.interpreter()
        self.assertEqual(a,1)

    def test_pointer_interpreter(self):
        a="ptr -> temp = 10 ;"
        """
                =
              /   \
            ->      10
          /   \
        ptr   temp"""
        root=Cparser.parse(a)
        value=root.interpreter()
        pointer=value.first.interpreter()
        self.assertEqual(pointer,10)

    def test_braceket_interpreter(self):
        a=" ( 2 + 3 ) * 4 ;"
        """     *
              /    \
             (      4
             |
             +
           /   \
          2     3 """
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,20)
        bracket=root.first
        value=bracket.interpreter()
        self.assertEqual(value,5)
        four=root.second
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
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertTrue(value)

    def test_bigger_condition_interpreter(self):
        a=" 2 > 1 ;"
        """ >
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertTrue(value)

    def test_smaller_condition_interpreter(self):
        a=" 2 < 1 ;"
        """ <
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertFalse(value)

    def test_biggerequal_condition_interpret(self):
        a=" 2 >= 1 ;"
        """ >=
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertTrue(value)

    def test_smallerequal_condition_interpreter(self):
        a=" 2 < 1 ;"
        """ <=
           /  \
          2    1"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertFalse(value)

    def test_shiftleft_bit_interpreter(self):
        a=" 1 << 3 ;"
        """ <<
           /  \
          1    3"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,8)

    def test_shiftright_bit_interpreter(self):
        a=" 8 >> 3 ;"
        """ >>
           /  \
          8    3"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,1)

    def test_and_bit_interpreter(self):
        a=" 5 & 6 ;"
        """ &
           /  \
          5    6"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,4)

    def test_xor_bit_interpreter(self):
        a=" ~ 2 ;"
        """ ~
            |
            2"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,-3)

    def test_not_bit_interpreter(self):
        a=" ! 2 ;"
        """ !
            |
            2"""
        root=Cparser.parse(a)
        value=root.interpreter()
        self.assertEqual(value,0)




if __name__=='__main__':
    if test_result==True:
        unittest.main()
    elif debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter)
        unittest.TextTestRunner(verbosity=2).run(suite)