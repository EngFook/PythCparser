##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
          This module is to test keyword -> for loop
                                                                             """
##"Test start here."                                                          ##
class TestKeyword_for_loop(unittest.TestCase):

    def test_for_loop_with_no_bracket_raiseSyntax(self):
        a='for  int x = 0 ; x = 5 ; x ++  ;'
        """
              for-------------------
                  |         |      |
                  =         |      ++
                 / \        =      |
               int  0      / \     x
                |         x   5
                x

               """
        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_for_loop_without_semicolumn_raiseSyntax(self):
        a='for ( int x = 0 ; x = 5 ; x ++ ) '
        """
              for-------------------
                  |         |      |
                  =         |      ++
                 / \        =      |
               int  0      / \     x
                |         x   5
                x

               """
        self.assertRaises(SyntaxError,CParser.parse,a)


    def test_for_loop_without_a_body(self):
        a='for ( x = 0 ; x = 5 ; x ++ ) ;'
        """
              for-------------------
                  |         |      |
                  =         |      ++
                 / \        =      |
                x   0      / \     x
                          x   5

               """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'for')
        equal=root[0].first
        self.assertEqual(equal.id,'=')
        x=equal.first
        self.assertEqual(valueof(x),'x')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        equal2=root[0].second
        self.assertEqual(equal2.id,'=')
        x2=equal2.first
        self.assertEqual(valueof(x2),'x')
        five=equal2.second
        self.assertEqual(valueof(five),'5')
        plusplus=root[0].third
        self.assertEqual(plusplus.id,'++')
        x3=plusplus.first
        self.assertEqual(valueof(x3),'x')

    def test_for_loop_with_a_body(self):
        a='for ( x = 0 ; x = 5 ; x ++ ) x + y = z ;'
        """
              for-----------------------------
                  |         |      |        |
                  =         |      ++       =
                 / \        =      |      /  \
                x   0      / \     x     +    z
                          x   5         / \
                                       x   y
               """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'for')
        equal=root[0].first
        self.assertEqual(equal.id,'=')
        x=equal.first
        self.assertEqual(valueof(x),'x')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        equal2=root[0].second
        self.assertEqual(equal2.id,'=')
        x2=equal2.first
        self.assertEqual(valueof(x2),'x')
        five=equal2.second
        self.assertEqual(valueof(five),'5')
        plusplus=root[0].third
        self.assertEqual(plusplus.id,'++')
        x3=plusplus.first
        self.assertEqual(valueof(x3),'x')
        equal3=root[0].four
        self.assertEqual(equal3.id,'=')
        plus=equal3.first
        self.assertEqual(plus.id,'+')
        x=plus.first
        self.assertEqual(valueof(x),'x')
        y=plus.second
        self.assertEqual(valueof(y),'y')
        z=equal3.second
        self.assertEqual(valueof(z),'z')

    def test_for_loop_with_a_statement_block(self):
        a='for ( x = 0 ; x = 5 ; x ++ )  { a = 1 ; b = 2 ; c = 3 ; } '
        """
              for-----------------------------
                  |         |      |        {
                  =         |      ++       |---=
                 / \        =      |        |  / \
                x   0      / \     x        | a   1
                          x   5             |---=
                                            | /   \
                                            |b     2
                                            |---=
                                            | /   \
                                            |c     3

                                  """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'for')
        equal=root[0].first
        self.assertEqual(equal.id,'=')
        x=equal.first
        self.assertEqual(valueof(x),'x')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        equal2=root[0].second
        self.assertEqual(equal2.id,'=')
        x2=equal2.first
        self.assertEqual(valueof(x2),'x')
        five=equal2.second
        self.assertEqual(valueof(five),'5')
        plusplus=root[0].third
        self.assertEqual(plusplus.id,'++')
        x3=plusplus.first
        self.assertEqual(valueof(x3),'x')
        brace=root[0].four
        self.assertEqual(brace.id,'{')
        equal=brace.first[0]
        self.assertEqual(equal.id,'=')
        a=equal.first
        self.assertEqual(valueof(a),'a')
        one=equal.second
        self.assertEqual(valueof(one),'1')
        equal1=brace.first[1]
        self.assertEqual(equal1.id,'=')
        b=equal1.first
        self.assertEqual(valueof(b),'b')
        two=equal1.second
        self.assertEqual(valueof(two),'2')
        equal2=brace.first[2]
        self.assertEqual(equal2.id,'=')
        c=equal2.first
        self.assertEqual(valueof(c),'c')
        three=equal2.second
        self.assertEqual(valueof(three),'3')
################################################################################
################################################################################
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_for_loop)
        unittest.TextTestRunner(verbosity=2).run(suite)