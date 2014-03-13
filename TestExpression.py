##"Files imported."                                                           ##
import unittest
import Cparser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
    This module is for test everything in Expression.
                                                            """
'''
    Set On/Off -> False = Off ; True = On
    To debug_all: set debug_all=True
                                            '''
debug_all=True
##"Test start."                                                               ##
class TestExperession(unittest.TestCase):

    def testAdvanceShouldReturnLiteral(self):
        tokenizer=Cparser.Tokenizer('3')
        token=tokenizer.advance()
        self.assertEqual(token.id,'(literal)')
        self.assertEqual(valueof(token),'3')

    def testAdvanceShouldReturnIdentifier(self):
        tokenizer=Cparser.Tokenizer('one')
        token=tokenizer.advance()
        self.assertEqual(token.id,'(identifier)')
        self.assertEqual(valueof(token),'one')

    def testAdvanceShouldReturnOperator(self):
        tokenizer=Cparser.Tokenizer('+')
        token=tokenizer.advance()
        self.assertEqual(token.arity,'binary')
        self.assertEqual(token.id,'+')

    def testAdvanceShouldReturnCorrectToken(self):
        tokenizer=Cparser.Tokenizer('one 3 +')
        token=tokenizer.advance()
        self.assertEqual(token.id,'(identifier)')
        self.assertEqual(valueof(token),'one')
        token=tokenizer.advance()
        self.assertEqual(token.id,'(literal)')
        self.assertEqual(valueof(token),'3')
        token=tokenizer.advance()
        self.assertEqual(token.arity,'binary')
        self.assertEqual(token.id,'+')

    def test2plus3(self):#2+3
        a='2 + 3 ;'
        root=Cparser.parse(a)
        two=root[0].first
        self.assertEqual(valueof(two),'2')
        self.assertEqual(two.id,'(literal)')
        three=root[0].second
        self.assertEqual(valueof(three),'3')
        self.assertEqual(three.id,'(literal)')
        self.assertEqual(root[0].id,'+')
        self.assertEqual(root[0].arity,'binary')

    def test2plus3multiply4(self):
        a='2 + 3 * 4 ;'
        """       +
                /   \
              2      *
                    /  \
                  3      4"""
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'+')
        self.assertEqual(root[0].arity,'binary')
        two=root[0].first
        self.assertEqual(valueof(two),'2')
        self.assertEqual(two.id,'(literal)')
        multiply=root[0].second
        self.assertEqual(multiply.id,'*')
        self.assertEqual(multiply.arity,'binary')
        three=multiply.first
        self.assertEqual(valueof(three),'3')
        self.assertEqual(three.id,'(literal)')
        four=multiply.second
        self.assertEqual(valueof(four),'4')
        self.assertEqual(four.id,'(literal)')

    def test2multiply3plus4(self):
        a='2 * 3 + 4 ;'
        """       +
                /   \
              *      4
            /  \
           2    3"""
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'+')
        self.assertEqual(root[0].arity,'binary')
        multiply=root[0].first
        self.assertEqual(multiply.id,'*')
        self.assertEqual(multiply.arity,'binary')
        two=multiply.first
        self.assertEqual(valueof(two),'2')
        self.assertEqual(two.id,'(literal)')
        three=multiply.second
        self.assertEqual(valueof(three),'3')
        self.assertEqual(three.id,'(literal)')
        four=root[0].second
        self.assertEqual(valueof(four),'4')
        self.assertEqual(four.id,'(literal)')

    def test2plus3multiply4plus5(self):
        a='2 + 3 * 4 + 5 ;'
        """       +
                /   \
              +      5
            /  \
           2    *
               /  \
              3    4"""
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'+')
        self.assertEqual(root[0].arity,'binary')
        plus2=root[0].first
        self.assertEqual(plus2.id,'+')
        self.assertEqual(plus2.arity,'binary')
        two=plus2.first
        self.assertEqual(valueof(two),'2')
        self.assertEqual(two.id,'(literal)')
        multiply=plus2.second
        self.assertEqual(multiply.id,'*')
        self.assertEqual(multiply.arity,'binary')
        three=multiply.first
        self.assertEqual(valueof(three),'3')
        self.assertEqual(three.id,'(literal)')
        four=multiply.second
        self.assertEqual(valueof(four),'4')
        self.assertEqual(four.id,'(literal)')
        five=root[0].second
        self.assertEqual(valueof(five),'5')
        self.assertEqual(five.id,'(literal)')

    def test2plus3plus4plus5(self):
          a='2 + 3 + 4 + 5 ;'
          """           +
                      /   \
                     +     5
                   /  \
                  +     4
                /  \
               2    3"""
          root=Cparser.parse(a)
          self.assertEqual(root[0].id,'+')
          self.assertEqual(root[0].arity,'binary')
          plus2=root[0].first
          self.assertEqual(plus2.id,'+')
          self.assertEqual(plus2.arity,'binary')
          plus3=plus2.first
          self.assertEqual(plus3.id,'+')
          self.assertEqual(plus3.arity,'binary')
          two=plus3.first
          self.assertEqual(valueof(two),'2')
          self.assertEqual(two.id,'(literal)')
          three=plus3.second
          self.assertEqual(valueof(three),'3')
          self.assertEqual(three.id,'(literal)')
          four=plus2.second
          self.assertEqual(valueof(four),'4')
          self.assertEqual(four.id,'(literal)')
          five=root[0].second
          self.assertEqual(valueof(five),'5')
          self.assertEqual(five.id,'(literal)')

    def test2plus3plus4plus5multiply6multiply7multiply8(self):
          a='2 + 3 + 4 + 5 * 6 * 7 * 8 ;'
          """          +
                   /       \
                  +         *
                /  \       /  \
               +    4     *    8
             /  \       /  \
            2    3     *    7
                      / \
                     5   6  """

          root=Cparser.parse(a)
          self.assertEqual(root[0].id,'+')
          self.assertEqual(root[0].arity,'binary')
          plus2=root[0].first
          self.assertEqual(plus2.id,'+')
          self.assertEqual(plus2.arity,'binary')
          plus3=plus2.first
          self.assertEqual(plus3.id,'+')
          self.assertEqual(plus3.arity,'binary')
          two=plus3.first
          self.assertEqual(valueof(two),'2')
          self.assertEqual(two.id,'(literal)')
          three=plus3.second
          self.assertEqual(valueof(three),'3')
          self.assertEqual(three.id,'(literal)')
          four=plus2.second
          self.assertEqual(valueof(four),'4')
          self.assertEqual(four.id,'(literal)')
          multiply=root[0].second
          self.assertEqual(multiply.id,'*')
          self.assertEqual(multiply.arity,'binary')
          multiply2=multiply.first
          self.assertEqual(multiply2.id,'*')
          self.assertEqual(multiply2.arity,'binary')
          multiply3=multiply2.first
          self.assertEqual(multiply3.id,'*')
          self.assertEqual(multiply3.arity,'binary')
          five=multiply3.first
          self.assertEqual(valueof(five),'5')
          self.assertEqual(five.id,'(literal)')
          six=multiply3.second
          self.assertEqual(valueof(six),'6')
          self.assertEqual(five.id,'(literal)')
          seven=multiply2.second
          self.assertEqual(valueof(seven),'7')
          self.assertEqual(five.id,'(literal)')
          eight=multiply.second
          self.assertEqual(valueof(eight),'8')
          self.assertEqual(five.id,'(literal)')


    def testnegativeone(self):
        a='- 1 ;'
        """     -
                |
                1"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'-')
        self.assertEqual(root[0].arity,'unary')
        one=root[0].first
        self.assertEqual(valueof(one),'1')
        self.assertEqual(one.id,'(literal)')

    def testnegativennoneegative(self):
        a='- - 1 ;'
        """     -
                |
                -
                |
                1"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'-')
        self.assertEqual(root[0].arity,'unary')
        negative=root[0].first
        self.assertEqual(negative.id,'-')
        self.assertEqual(negative.arity,'unary')
        one=negative.first
        self.assertEqual(valueof(one),'1')
        self.assertEqual(one.id,'(literal)')

    def testpower(self):
        a='1 ** 2 ** 3 ;'
        """       **
                /   \
               1    **
                   /  \
                  2    3"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'**')
        self.assertEqual(root[0].arity,'binary')
        one=root[0].first
        self.assertEqual(valueof(one),'1')
        self.assertEqual(one.id,'(literal)')
        power=root[0].second
        self.assertEqual(power.id,'**')
        self.assertEqual(power.arity,'binary')
        two=power.first
        self.assertEqual(valueof(two),'2')
        self.assertEqual(two.id,'(literal)')
        three=power.second
        self.assertEqual(valueof(three),'3')
        self.assertEqual(three.id,'(literal)')

    def testnegativeoneplus2(self):
        a='- 1 + 2 ;'
        """     +
              /   \
             -     2
             |
             1"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'+')
        self.assertEqual(root[0].arity,'binary')
        negative=root[0].first
        self.assertEqual(negative.id,'-')
        self.assertEqual(negative.arity,'unary')
        one=negative.first
        self.assertEqual(valueof(one),'1')
        self.assertEqual(one.id,'(literal)')
        two=root[0].second
        self.assertEqual(valueof(two),'2')
        self.assertEqual(one.id,'(literal)')

    def testnegativeoneplus2plusnegativethree(self):
        a='- 1 + 2  + - 3 ;'
        """         +
                  /   \
                +       -
              /   \     |
             -     2    3
             |
             1"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'+')
        self.assertEqual(root[0].arity,'binary')
        plus1=root[0].first
        self.assertEqual(plus1.id,'+')
        self.assertEqual(plus1.arity,'binary')
        negative1=plus1.first
        self.assertEqual(negative1.id,'-')
        self.assertEqual(negative1.arity,'unary')
        one=negative1.first
        self.assertEqual(valueof(one),'1')
        self.assertEqual(one.id,'(literal)')
        two=plus1.second
        self.assertEqual(valueof(two),'2')
        self.assertEqual(two.id,'(literal)')
        negative2=root[0].second
        self.assertEqual(negative2.id,'-')
        self.assertEqual(negative2.arity,'unary')
        three=negative2.first
        self.assertEqual(valueof(three),'3')
        self.assertEqual(three.id,'(literal)')


    def testnegativeIdentifier(self):
        a='- ptr ;'
        """  -
             |
             ptr"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'-')
        self.assertEqual(root[0].arity,'unary')
        ptr=root[0].first
        self.assertEqual(valueof(ptr),'ptr')
        self.assertEqual(ptr.id,'(identifier)')

    def testnegativenegatievIdentifier(self):
        a='-- ptr ;'
        """  --
             |
             ptr"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'--')
        self.assertEqual(root[0].arity,'unary')
        ptr=root[0].first
        self.assertEqual(valueof(ptr),'ptr')
        self.assertEqual(ptr.id,'(identifier)')

    def testpredecremetptrminusnegativeone(self):
        a='-- ptr + - 1 ;'
        """  +
            / \
           --   -
           |    |
           ptr  1"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'+')
        self.assertEqual(root[0].arity,'binary')
        predec=root[0].first
        self.assertEqual(predec.id,'--')
        self.assertEqual(predec.arity,'unary')
        ptr=predec.first
        self.assertEqual(valueof(ptr),'ptr')
        self.assertEqual(ptr.id,'(identifier)')
        negative1=root[0].second
        self.assertEqual(negative1.id,'-')
        self.assertEqual(negative1.arity,'unary')
        one=negative1.first
        self.assertEqual(valueof(one),'1')
        self.assertEqual(one.id,'(literal)')

    def testpostfixwithprefix(self):
        a='ptr -- - -- ptr ;'
        """     -
               / \
            --    --
             |     |
             ptr   ptr """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'-')
        self.assertEqual(root[0].arity,'binary')
        postfix=root[0].first
        self.assertEqual(postfix.id,'--')
        self.assertEqual(postfix.arity,'postunary')
        ptr=postfix.first
        #self.assertEqual(valueof(ptr),'ptr')
        self.assertEqual(ptr.id,'(identifier)')
        predec=root[0].second
        self.assertEqual(predec.id,'--')
        self.assertEqual(predec.arity,'unary')
        ptr1=predec.first
        self.assertEqual(valueof(ptr1),'ptr')
        self.assertEqual(ptr1.id,'(identifier)')



    def testxequalwplusyequalz(self):
        a='x = w + y = z ;'
        """     =
               / \
              x   =
                 /  \
                +   z
              /  \
             w   y """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'=')
        self.assertEqual(root[0].arity,'binary')
        x=root[0].first
        self.assertEqual(valueof(x),'x')
        self.assertEqual(x.id,'(identifier)')
        equal=root[0].second
        self.assertEqual(equal.id,'=')
        self.assertEqual(equal.arity,'binary')
        plus=equal.first
        self.assertEqual(plus.id,'+')
        self.assertEqual(plus.arity,'binary')
        w=plus.first
        self.assertEqual(valueof(w),'w')
        self.assertEqual(w.id,'(identifier)')
        y=plus.second
        self.assertEqual(valueof(y),'y')
        self.assertEqual(y.id,'(identifier)')
        z=equal.second
        self.assertEqual(valueof(z),'z')
        self.assertEqual(z.id,'(identifier)')

    def test_equal_and_etcwithequal(self):
        a='x = w += y ;'
        """     =
               / \
              x   +=
                 /  \
                w   y """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'=')
        self.assertEqual(root[0].arity,'binary')
        x=root[0].first
        self.assertEqual(valueof(x),'x')
        self.assertEqual(x.id,'(identifier)')
        equalplus=root[0].second
        self.assertEqual(equalplus.id,'+=')
        self.assertEqual(equalplus.arity,'binary')
        w=equalplus.first
        self.assertEqual(valueof(w),'w')
        self.assertEqual(w.id,'(identifier)')
        y=equalplus.second
        self.assertEqual(valueof(y),'y')
        self.assertEqual(y.id,'(identifier)')

    def testxdoty(self):
        a='x . y ;'
        """     .
               / \
              x   y """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'.')
        self.assertEqual(root[0].arity,'binary')
        x=root[0].first
        self.assertEqual(valueof(x),'x')
        self.assertEqual(x.id,'(identifier)')
        y=root[0].second
        self.assertEqual(valueof(y),'y')
        self.assertEqual(y.id,'(identifier)')

    def testbracketforerror(self):
        a='func ( a ) ( b ) ;'
        self.assertRaises(SyntaxError,Cparser.parse,a)


    def test_bracket(self):
        a='func [ a ] [ b ] ;'
        """    [
               /  \
              [    b
             / \
          func  a"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'[')
        self.assertEqual(root[0].arity,'postunary')
        b=root[0].second
        self.assertEqual(valueof(b),'b')
        self.assertEqual(b.id,'(identifier)')
        bracket=root[0].first
        self.assertEqual(bracket.id,'[')
        self.assertEqual(bracket.arity,'postunary')
        func=bracket.first
        self.assertEqual(valueof(func),'func')
        self.assertEqual(func.id,'(identifier)')
        a=bracket.second
        self.assertEqual(valueof(a),'a')
        self.assertEqual(func.id,'(identifier)')


    def test_Int_a(self):
        a='int a ;'
        """  int
             |
             a"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'int')
        a=root[0].first
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')

    def test_Int_a_b_c(self):
        a='int a , b , c ;'
        """  int
             |
             |-a
             |-b
             |-c"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'int')
        a=root[0].first[0]
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')
        a=root[0].first[1]
        self.assertEqual(valueof(a),'b')
        self.assertEqual(a.id,'(identifier)')
        a=root[0].first[2]
        self.assertEqual(valueof(a),'c')
        self.assertEqual(a.id,'(identifier)')


    def test_bracket_with_declaration(self):
        a='func ( int a ) ;'
        """   (
             / \
          func  int
                  |
                  a"""

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'(')
        self.assertEqual(root[0].arity,'function')
        integer=root[0].second
        self.assertEqual(integer.id,'int')
        a=integer.first
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')
        func=root[0].first
        self.assertEqual(valueof(func),'func')
        self.assertEqual(func.id,'(identifier)')

    def test_function_call_with_comma_and_int(self):
        a='int function ( a , b ) ;'
        """     (
               /  \
             int   |
               |   |-a
          function |-b """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'(')
        self.assertEqual(root[0].arity,'function')
        INT=root[0].first
        self.assertEqual(INT.id,'int')
        function=INT.first
        self.assertEqual(valueof(function),'function')
        self.assertEqual(function.id,'(identifier)')
        a=root[0].second[0]
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')
        b=root[0].second[1]
        self.assertEqual(valueof(b),'b')
        self.assertEqual(b.id,'(identifier)')

    def test_function_call_with_comma(self):
        a=' function ( a , b ) ;'
        """     (
               /  \
        function   |
                   |-a
                   |-b """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'(')
        self.assertEqual(root[0].arity,'function')
        function=root[0].first
        self.assertEqual(valueof(function),'function')
        self.assertEqual(function.id,'(identifier)')
        a=root[0].second[0]
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')
        b=root[0].second[1]
        self.assertEqual(valueof(b),'b')
        self.assertEqual(b.id,'(identifier)')

    def test_function_call_with_comma_with_declaration(self):
        a=' function ( int a , double b ) ;'
        """     (
               /  \
        function   |
                   |-int-a
                   |-double-b """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'(')
        self.assertEqual(root[0].arity,'function')
        function=root[0].first
        self.assertEqual(valueof(function),'function')
        self.assertEqual(function.id,'(identifier)')
        integer=root[0].second[0]
        self.assertEqual(integer.id,'int')
        a=integer.first
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')
        double=root[0].second[1]
        self.assertEqual(double.id,'double')
        b=double.first
        self.assertEqual(valueof(b),'b')
        self.assertEqual(b.id,'(identifier)')

    def test_integer_with_pointer_with_function(self):
        a='int * ( * ptr ) ;'

        """     int
                 |
                 *
                 |
                 (
                 |
                 *
                 |
                ptr     """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'int')
        address=root[0].first
        self.assertEqual(address.id,'*')
        self.assertEqual(address.arity,"unary")
        bracket=address.first
        self.assertEqual(bracket.id,'(')
        self.assertEqual(bracket.arity,"grouping")
        address2=bracket.first
        ptr=address2.first
        self.assertEqual(valueof(ptr),'ptr')
        self.assertEqual(ptr.id,'(identifier)')


    def test_function_call_with_command_declaration(self):
        a='int * ( * ptr ) ( int a , double b ) ;'

        """      (
                 |
                / \
              int  |
               |   |-int-a
               *   |-double-b
               |
               (
               |
               *
               |
               ptr     """

        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'(')
        INT=root[0].first
        self.assertEqual(INT.id,'int')
        address=INT.first
        self.assertEqual(address.id,'*')
        self.assertEqual(address.arity,"unary")
        bracket1=address.first
        self.assertEqual(bracket1.id,'(')
        self.assertEqual(bracket1.arity,"grouping")
        address1=bracket1.first
        self.assertEqual(address1.id,'*')
        self.assertEqual(address1.arity,"unary")
        ptr=address1.first
        self.assertEqual(valueof(ptr),'ptr')
        self.assertEqual(ptr.id,'(identifier)')
        int1=root[0].second[0]
        self.assertEqual(int1.id,'int')
        a=int1.first
        self.assertEqual(valueof(a),'a')
        self.assertEqual(a.id,'(identifier)')
        double1=root[0].second[1]
        self.assertEqual(double1.id,'double')
        b=double1.first
        self.assertEqual(valueof(b),'b')
        self.assertEqual(b.id,'(identifier)')

    def test_function_definition(self):
        a='''int func ( int x , int y )
            {
                return a + b ;
            } '''
        """
              (-----{----------return
            /   \                |
          int    |-int-x         +
            |    |-int-y        / \
        function               a   b"""
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'(')
        INT=root[0].first
        self.assertEqual(INT.id,'int')
        func=INT.first
        self.assertEqual(valueof(func),'func')
        listofvariable=root[0].second
        int0=listofvariable[0]
        self.assertEqual(int0.id,'int')
        x=int0.first
        self.assertEqual(valueof(x),'x')
        int1=listofvariable[1]
        self.assertEqual(int1.id,'int')
        y=int1.first
        self.assertEqual(valueof(y),'y')
        brace=root[0].third
        self.assertEqual(brace.id,'{')
        listofcontent=brace.first
        return0=listofcontent[0]
        self.assertEqual(return0.id,'return')
        plus=return0.first
        self.assertEqual(plus.id,'+')
        a=plus.first
        self.assertEqual(valueof(a),'a')
        b=plus.second
        self.assertEqual(valueof(b),'b')

    def test_int_a_equal_2(self):
        a=" int a = 2 ;"
        """   =
            /   \
          int    2
          |
          a"""
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'=')
        INT=root[0].first
        self.assertEqual(INT.id,'int')
        a=INT.first
        self.assertEqual(a.id,'(identifier)')
        self.assertEqual(valueof(a),'a')
        two=root[0].second
        self.assertEqual(two.id,'(literal)')
        self.assertEqual(valueof(two),'2')
################################################################################
################################################################################
if __name__=='__main__':
    if debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestExperession)
        unittest.TextTestRunner(verbosity=2).run(suite)