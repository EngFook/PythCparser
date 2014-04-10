##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
          This module is to test keyword -> if else
                                                                             """
##"Test start here."                                                          ##
class TestKeyword_if_else(unittest.TestCase):

    def test_statement_if_with_a_condition_only(self):
        a='if ( x ) ;'
        """  if
              |
              (
              |
              x

        """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        x=bracket.first
        self.assertEqual(valueof(x),'x')

    def test_statement_if_with_a_body_only_raiseSyntax_(self):
        a='if x ;'
        """  if
              |
              |
              x

        """
        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_statement_else_with_body_only_raiseSyntax(self):
        a='else x ;'
        """  else
              |
              x

                """
        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_statement_if_with_else_raiseSyntax(self):
        a='if ( y ) ; else ( x ) ;'
        """ if
              |______
              |     |
              (    else
              |     |
              y     (
                    |
                    x
                """
        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_statement_if_with_a_condition_and_body(self):
        a='if ( x ) y = 1 ;'
        """  if
              |______
              |     |
              (     =
              |    / \
              x   y   1

        """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        x=bracket.first
        self.assertEqual(valueof(x),'x')
        equal=root[0].second
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(x),'x')
        one=equal.second
        self.assertEqual(valueof(one),'1')

    def test_statement_if_with_condition_only_and_else(self):
        a='if ( y > 4 ) ; else z = 2 ;'
        """      if
               /    \
               (     else
               |        \
               >         =
            /  \        /  \
          y      4     z    2"""

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        else1=root[0].third
        self.assertEqual(else1.id,'else')
        equal=else1.first
        self.assertEqual(equal.id,'=')
        z=equal.first
        self.assertEqual(valueof(z),'z')
        three=equal.second
        self.assertEqual(valueof(three),'2')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        bigger=bracket.first
        self.assertEqual(bigger.id,'>')
        y=bigger.first
        self.assertEqual(valueof(y),'y')
        four=bigger.second
        self.assertEqual(valueof(four),'4')

    def test_statement_if_with_the_condition_body_and_else(self):
        a='if ( y > 4 ) x = 3 ; else z = 2 ;'
        """      if
               /   \       \
               (    \     else
               |     \        \
               >       =       =
            /  \     /  \     /  \
          y      4  x    3   z    2"""

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        else1=root[0].third
        self.assertEqual(else1.id,'else')
        equal=else1.first
        self.assertEqual(equal.id,'=')
        z=equal.first
        self.assertEqual(valueof(z),'z')
        three=equal.second
        self.assertEqual(valueof(three),'2')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        bigger=bracket.first
        self.assertEqual(bigger.id,'>')
        y=bigger.first
        self.assertEqual(valueof(y),'y')
        four=bigger.second
        self.assertEqual(valueof(four),'4')
        equalsign=root[0].second
        self.assertEqual(equalsign.id,'=')
        x=equalsign.first
        self.assertEqual(valueof(x),'x')
        three=equalsign.second
        self.assertEqual(valueof(three),'3')

    def test_statement_if_with_condition_and_statement_block(self):
        a='if ( x == 1 ) { a = 1 ; b = 2 ; c = 3 ; }'
        """         if
                  /     \
                 (       {
                 |       |---=
                ==       |  / \
               /   \     | a   1
              x     1    |---=
                         | /   \
                         |b     2
                         |---=
                           /   \
                          c     3"""
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        one=equalequal.second
        self.assertEqual(valueof(one),'1')
        brace=root[0].second
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

    def test_statement_if_with_condition_and_statement_block_and_else(self):
        a='if ( x == 1 ) { a = 1 ; b = 2 ; c = 3 ; } else z = 2 ;'
        """         if_____________
                  /     \          \
                 (       {         else
                 |       |---=       |
                ==       |  / \      =
               /   \     | a   1    / \
              x     1    |---=     z   2
                         | /   \
                         |b     2
                         |---=
                           /   \
                          c     3"""

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        one=equalequal.second
        self.assertEqual(valueof(one),'1')
        brace=root[0].second
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
        else1=root[0].third
        self.assertEqual(else1.id,'else')
        equal=else1.first
        self.assertEqual(equal.id,'=')
        z=equal.first
        self.assertEqual(valueof(z),'z')
        three=equal.second
        self.assertEqual(valueof(three),'2')

    def test_statement_if_with_the_condition_body_and_else_with_statement_block(self):
        a=' if ( x == 2 ) y = x ; else { a = 1 ; b = 2 ; c = 3 ; }'
        """         _____if_______
                   /     |       |
                  /      |      else
                 /       |       |
                 (       =       {
                 |      /  \     |---=
                ==     y    x    |  / \
               /   \             | a   1
              x     2            |---=
                                 | /   \
                                 |b     2
                                 |---=
                                   /   \
                                  c     3"""
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        equal=root[0].second
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        x=equal.second
        self.assertEqual(valueof(x),'x')
        else1=root[0].third
        self.assertEqual(else1.id,'else')
        brace=else1.first
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

    def test_statement_if_with_condition_with_statement_block_and_else_with_statement_block(self):
        a='if ( x == 1 ) { a = 1 ; b = 2 ; c = 3 ; } else { a = 1 ; b = 2 ; c = 3 ; } '
        """         if_____________
                  /     \          \
                 (       {         else
                 |       |---=       |
                ==       |  / \      {
               /   \     | a   1     |---=
              x     1    |---=       |  / \
                         | /   \     | a   1
                         |b     2    |---=
                         |---=       | /   \
                           /   \     |b     2
                          c     3    |---=
                                       /   \
                                      c     3

                                            """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        one=equalequal.second
        self.assertEqual(valueof(one),'1')
        brace=root[0].second
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
        else1=root[0].third
        self.assertEqual(else1.id,'else')
        brace=else1.first
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

    def test_statement_if_with_the_condition_body_and_else_if_with_statement_block(self):
        a=' if ( x == 2 ) y = x ; else if ( x == 1 ) { a = 1 ; b = 2 ; c = 3 ; }'
        """         _____if_______
                   /     |       |
                  /      |      else---------
                 /       |               ___if______
                 (       =              |           |
                 |      / \             (           {
                 |     y   x            |           |---=
                ==                      ==          |  / \
               /   \                   /  \         | a   1
              x     2                 x     1       |---=
                                                    | /   \
                                                    |b     2
                                                    |---=
                                                      /   \
                                                     c     3"""
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        equal=root[0].second
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        x=equal.second
        self.assertEqual(valueof(x),'x')
        else1=root[0].third
        self.assertEqual(else1.id,'else')
        ifstatement=else1.first
        self.assertEqual(ifstatement.id,'if')
        bracket=ifstatement.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        one=equalequal.second
        self.assertEqual(valueof(one),'1')
        brace=ifstatement.second
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

    def test_statement_if_with_the_condition_body_and_else_if_with_statement_block_and_else(self):
        a=' if ( x == 2 ) y = x ; else if ( x == 1 ) { a = 1 ; b = 2 ; c = 3 ; } else y ;'
        """         _____if_______
                   /     |       |
                  /      |      else---------
                 /       |               ___if_____________________
                 (       =              |           |              |
                 |      / \             (           {             else
                 |     y   x            |           |---=          |
                ==                      ==          |  / \         y
               /   \                   /  \         | a   1
              x     2                 x     1       |---=
                                                    | /   \
                                                    |b     2
                                                    |---=
                                                      /   \
                                                     c     3"""
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        equal=root[0].second
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        x=equal.second
        self.assertEqual(valueof(x),'x')
        else1=root[0].third
        self.assertEqual(else1.id,'else')
        ifstatement=else1.first
        self.assertEqual(ifstatement.id,'if')
        bracket=ifstatement.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        one=equalequal.second
        self.assertEqual(valueof(one),'1')
        brace=ifstatement.second
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
        else2=ifstatement.third
        self.assertEqual(else2.id,'else')
        y=else2.first
        self.assertEqual(valueof(y),'y')

    def test_statement_if_with_the_condition_body_and_with_statement_block_contain_if(self):
        a=' if ( x == 2 ) { if ( x == 3 ) ; y = 4 ; }'
        """         _____if
                   /      |
                  /       {
                 /        |
                 (        |------if
                 |        |       |
                ==        |       (
               /   \      |       |
              x     2     |       ==
                          |      /  \
                          |     x    3
                          |
                          |-------=
                                /   \
                               y     4"""

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=root[0].second
        self.assertEqual(brace.id,'{')
        ifstatement=brace.first[0]
        self.assertEqual(ifstatement.id,'if')
        bracket=ifstatement.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        three=equalequal.second
        self.assertEqual(valueof(three),'3')
        equal=brace.first[1]
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        four=equal.second
        self.assertEqual(valueof(four),'4')

    def test_statement_if_with_the_condition_body_and_with_nested_statement_block_contain_if(self):
        a=' if ( x == 2 ) { if ( x == 3 ) { if ( x == 4 ) ; y = 5 ; } }'
        """         _____if
                   /      |
                  /       {
                 /        |
                 (        |------if____________
                 |                |           {
                 |                |           |
                ==                (           |--------if
               /   \              |           |         |
              x     2             ==          |         (
                                 /  \         |         |
                                x    3        |         ==
                                              |        /  \
                                              |       x    4
                                              |
                                              |-------=
                                                    /   \
                                                   y     5

                                                    """

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=root[0].second
        self.assertEqual(brace.id,'{')
        ifstatement=brace.first[0]
        self.assertEqual(ifstatement.id,'if')
        bracket=ifstatement.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        three=equalequal.second
        self.assertEqual(valueof(three),'3')
        brace1=ifstatement.second
        self.assertEqual(brace.id,'{')
        ifstatement1=brace1.first[0]
        self.assertEqual(ifstatement1.id,'if')
        bracket=ifstatement1.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        four=equalequal.second
        self.assertEqual(valueof(four),'4')
        equal=brace1.first[1]
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        five=equal.second
        self.assertEqual(valueof(five),'5')

    def test_statement_if_with_the_condition_body_and_with_nested_statement_block_contain_if_and_else_if(self):
        a=' if ( x == 2 ) { if ( x == 3 ) ; else if ( x == 4 ) ; y = 5 ;  }'
        """         _____if
                   /      |
                  /       {
                 /        |
                 (        |------if____________
                 |                |           |
                 |                |          else
                ==                (           |----------
               /   \              |           |         |
              x     2             |           |         if
                                  |           |         |
                                  ==          |         (
                                 /  \         |         |
                                x    3        |         ==
                                              |        /  \
                                              |       x    4
                                              |
                                              |-------=
                                                    /   \
                                                   y     5

                                                    """

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=root[0].second
        self.assertEqual(brace.id,'{')
        ifstatement=brace.first[0]
        self.assertEqual(ifstatement.id,'if')
        bracket=ifstatement.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        three=equalequal.second
        self.assertEqual(valueof(three),'3')
        else1=ifstatement.third
        self.assertEqual(else1.id,'else')
        ifstatement1=else1.first
        self.assertEqual(ifstatement1.id,'if')
        bracket=ifstatement1.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        four=equalequal.second
        self.assertEqual(valueof(four),'4')
        equal=brace.first[1]
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        five=equal.second
        self.assertEqual(valueof(five),'5')

    def test_statement_if_with_the_condition_body_and_with_nested_statement_block_contain_if_and_else(self):
        a=' if ( x == 2 ) { if ( x == 3 ) else  y = 5 ; }'
        """         _____if
                   /      |
                  /       {
                 /        |
                 (        |------if____________
                 |                |          else
                 |                |           |
                ==                (           |
               /   \              |           |
              x     2             |           |
                                  |           |
                                  ==          |
                                 /  \         |
                                x    3        |
                                              |
                                              |
                                              |
                                              |-------=
                                                    /   \
                                                   y     5

                                                    """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'if')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=root[0].second
        self.assertEqual(brace.id,'{')
        ifstatement=brace.first[0]
        self.assertEqual(ifstatement.id,'if')
        bracket=ifstatement.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        three=equalequal.second
        self.assertEqual(valueof(three),'3')
        else1=ifstatement.second
        self.assertEqual(else1.id,'else')
        equal=else1.first
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        five=equal.second
        self.assertEqual(valueof(five),'5')
################################################################################
################################################################################
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_if_else)
        unittest.TextTestRunner(verbosity=2).run(suite)