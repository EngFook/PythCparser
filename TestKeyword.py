import unittest
import cparser
from Tokenizer import *
def valueof(symObj):
    return symObj.first

#set debug On/Off -> False = Off ; True = On
#If debug_All is Off, specific debug parts can be set manually.
debug_All=True
debug_scope=False
debug_if_else=False
debug_do_while=False
debug_forloop=True
debug_switchcase=False
debug_braces=False
################################################################################
################################################################################
################################################################################
# Test -> if and else
################################################################################
class TestKeyword_scope(unittest.TestCase):
    def testdefinestament(self):
        a='#define x 10'
        """ #define
               |
               x
               |
               10"""
        root=cparser.parse(a)
        self.assertEqual(root.id,'#define')
        x=root.first
        self.assertEqual(valueof(x),'x')
        self.assertEqual(x.id,'constantidentifier')
        ten=x.constantidentifier
        self.assertEqual(valueof(ten),'10')


################################################################################
################################################################################
################################################################################
# Test -> if and else
################################################################################
class TestKeyword_if_else(unittest.TestCase):

    def test_statement_if_with_a_condition_only(self):
        a='if ( x ) ;'
        """  if
              |
              (
              |
              x

        """
        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
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
        self.assertRaises(SyntaxError,cparser.parse,a)

    def test_statement_else_with_body_only_raiseSyntax(self):
        a='else x ;'
        """  else
              |
              x

                """
        self.assertRaises(SyntaxError,cparser.parse,a)

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
        self.assertRaises(SyntaxError,cparser.parse,a)

    def test_statement_if_with_a_condition_and_body(self):
        a='if ( x ) y = 1 ;'
        """  if
              |______
              |     |
              (     =
              |    / \
              x   y   1

        """
        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        x=bracket.first
        self.assertEqual(valueof(x),'x')
        equal=root.second
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

        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        else1=root.third
        self.assertEqual(else1.id,'else')
        equal=else1.first
        self.assertEqual(equal.id,'=')
        z=equal.first
        self.assertEqual(valueof(z),'z')
        three=equal.second
        self.assertEqual(valueof(three),'2')
        bracket=root.first
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

        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        else1=root.third
        self.assertEqual(else1.id,'else')
        equal=else1.first
        self.assertEqual(equal.id,'=')
        z=equal.first
        self.assertEqual(valueof(z),'z')
        three=equal.second
        self.assertEqual(valueof(three),'2')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        bigger=bracket.first
        self.assertEqual(bigger.id,'>')
        y=bigger.first
        self.assertEqual(valueof(y),'y')
        four=bigger.second
        self.assertEqual(valueof(four),'4')
        equalsign=root.second
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
        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        one=equalequal.second
        self.assertEqual(valueof(one),'1')
        brace=root.second
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

        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        one=equalequal.second
        self.assertEqual(valueof(one),'1')
        brace=root.second
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
        else1=root.third
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
        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        equal=root.second
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        x=equal.second
        self.assertEqual(valueof(x),'x')
        else1=root.third
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
        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        one=equalequal.second
        self.assertEqual(valueof(one),'1')
        brace=root.second
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
        else1=root.third
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
        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        equal=root.second
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        x=equal.second
        self.assertEqual(valueof(x),'x')
        else1=root.third
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
        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        equal=root.second
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        x=equal.second
        self.assertEqual(valueof(x),'x')
        else1=root.third
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

        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=root.second
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

        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=root.second
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

        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=root.second
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

        root=cparser.parse(a)
        self.assertEqual(root.id,'if')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=root.second
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
################################################################################
# Test -> do while
################################################################################
class TestKeyword_do_while(unittest.TestCase):

    def test_while_statement_with_body_raiseSyntax(self):
        a='while x'
        """while
             |
             x
                """
        self.assertRaises(SyntaxError,cparser.parse,a)

    def test_while_statement_with_condition_only(self):
        a='while ( x < 1 ) ;'
        """ while
             |
             (
             |
             <
            / \
           x   1"""
        root=cparser.parse(a)
        self.assertEqual(root.id,'while')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        smaller=bracket.first
        self.assertEqual(smaller.id,'<')
        x=smaller.first
        self.assertEqual(valueof(x),'x')
        one=smaller.second
        self.assertEqual(valueof(one),'1')

    def test_while_statement_with_condition_and_body(self):
        a='while ( x < 1 ) x ++ ;'
        """ while
            /  \
           (    ++
           |     |
           <     x
          / \
         x   1"""
        root=cparser.parse(a)
        self.assertEqual(root.id,'while')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        smaller=bracket.first
        self.assertEqual(smaller.id,'<')
        x=smaller.first
        self.assertEqual(valueof(x),'x')
        one=smaller.second
        self.assertEqual(valueof(one),'1')
        plusplus=root.second
        self.assertEqual(plusplus.id,'++')
        x=plusplus.first
        self.assertEqual(valueof(x),'x')

    def test_while_statement_with_condition_and_statement_block(self):
        a='while ( x < 1 ) { a = 1 ; b = 2 ; c = 3 ; } '
        """ while
            /  \
           (    {
           |     |
           <     |---=
          / \    |  / \
         x   1   | a   1
                 |---=
                 | /   \
                 |b     2
                 |---=
                   /   \
                  c     3"""

        root=cparser.parse(a)
        self.assertEqual(root.id,'while')
        bracket=root.first
        self.assertEqual(bracket.id,'(')
        smaller=bracket.first
        self.assertEqual(smaller.id,'<')
        x=smaller.first
        self.assertEqual(valueof(x),'x')
        one=smaller.second
        self.assertEqual(valueof(one),'1')
        brace=root.second
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

    def test_do_with_body_statement_follow_by_while(self):
        a='do {  x ++ ; } while ( x < 1 ) ;'
        """  do
            /  \
           {   while
           |     |
           ++    (
           |     |
           x     <
                / \
               X   1"""
        root=cparser.parse(a)
        self.assertEqual(root.id,'do')
        bracket=root.first
        self.assertEqual(bracket.id,'{')
        plusplus=bracket.first[0]
        self.assertEqual(plusplus.id,'++')
        x=plusplus.first
        self.assertEqual(valueof(x),'x')
        while1=root.second
        self.assertEqual(while1.id,'while')
        bracket1=while1.first
        self.assertEqual(bracket1.id,'(')
        smaller=bracket1.first
        self.assertEqual(smaller.id,'<')
        x=smaller.first
        self.assertEqual(valueof(x),'x')
        one=smaller.second
        self.assertEqual(valueof(one),'1')
################################################################################
################################################################################
################################################################################
# Test -> for loop
################################################################################
class TestKeyword_forloop(unittest.TestCase):

##    boudary condition: such as for () , must startwith bracket
##    -> condition
##    -> body
##    -> counter
##    Raise Syntax Error
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
        self.assertRaises(SyntaxError,cparser.parse,a)

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
        self.assertRaises(SyntaxError,cparser.parse,a)


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
        root=cparser.parse(a)
        self.assertEqual(root.id,'for')
        equal=root.first
        self.assertEqual(equal.id,'=')
        x=equal.first
        self.assertEqual(valueof(x),'x')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        equal2=root.second
        self.assertEqual(equal2.id,'=')
        x2=equal2.first
        self.assertEqual(valueof(x2),'x')
        five=equal2.second
        self.assertEqual(valueof(five),'5')
        plusplus=root.third
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
        root=cparser.parse(a)
        self.assertEqual(root.id,'for')
        equal=root.first
        self.assertEqual(equal.id,'=')
        x=equal.first
        self.assertEqual(valueof(x),'x')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        equal2=root.second
        self.assertEqual(equal2.id,'=')
        x2=equal2.first
        self.assertEqual(valueof(x2),'x')
        five=equal2.second
        self.assertEqual(valueof(five),'5')
        plusplus=root.third
        self.assertEqual(plusplus.id,'++')
        x3=plusplus.first
        self.assertEqual(valueof(x3),'x')
        equal3=root.four
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
        root=cparser.parse(a)
        self.assertEqual(root.id,'for')
        equal=root.first
        self.assertEqual(equal.id,'=')
        x=equal.first
        self.assertEqual(valueof(x),'x')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        equal2=root.second
        self.assertEqual(equal2.id,'=')
        x2=equal2.first
        self.assertEqual(valueof(x2),'x')
        five=equal2.second
        self.assertEqual(valueof(five),'5')
        plusplus=root.third
        self.assertEqual(plusplus.id,'++')
        x3=plusplus.first
        self.assertEqual(valueof(x3),'x')
        brace=root.four
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
################################################################################
# Test-> switch case
################################################################################
class TestKeyword_switchcase(unittest.TestCase):

##
##    still have to add some more.
##
##

    def test_switch_case_with_one_body_in_each_case(self):
        a='''switch ( choice )
            {
                case ' A ' : x = 1 ;
                case ' B ' : y = 2 ;
                default    : z = 3 ; } '''
        """     swtich
                /     \
               (       {
               |        |-case A
               |        |
               |        |---- =
              choice    |    / \
                        |   x   1
                        |--case B
                        |
                        |------=
                        |     / \
                        |   y    2
                        |- default
                        |------------=
                                    / \
                                   z    3"""
        root=cparser.parse(a)
        self.assertEqual(root.id,'switch')
        self.assertEqual(root.arity,'binary')
        choice=root.first
        self.assertEqual(valueof(choice),'choice')
        self.assertEqual(choice.id,'(identifier)')
        bracket=root.second
        self.assertEqual(bracket.id,'{')
        listofchoice=bracket.first
        casea=listofchoice[0]
        self.assertEqual(casea.id,'case')
        a=casea.first
        self.assertEqual(valueof(a),'A')
        self.assertEqual(a.id,'(identifier)')
        equal=listofchoice[1]
        x=equal.first
        self.assertEqual(valueof(x),'x')
        self.assertEqual(x.id,'(identifier)')
        one=equal.second
        self.assertEqual(valueof(one),'1')
        self.assertEqual(one.id,'(literal)')
        caseb=listofchoice[2]
        self.assertEqual(casea.id,'case')
        b=caseb.first
        self.assertEqual(valueof(b),'B')
        self.assertEqual(b.id,'(identifier)')
        equal2=listofchoice[3]
        y=equal2.first
        self.assertEqual(valueof(y),'y')
        self.assertEqual(y.id,'(identifier)')
        two=equal2.second
        self.assertEqual(valueof(two),'2')
        self.assertEqual(two.id,'(literal)')
        casec=listofchoice[4]
        self.assertEqual(casec.id,'default')
        equal3=listofchoice[5]
        z=equal3.first
        self.assertEqual(valueof(z),'z')
        self.assertEqual(z.id,'(identifier)')
        three=equal3.second
        self.assertEqual(valueof(three),'3')
        self.assertEqual(three.id,'(literal)')

    def test_switch_statement_with_condition_and_statement_block(self):
        a='''switch ( choice )
            {
                case ' A ' : x = 1 ;  if ( x == 2 ) { w = v ;
                case ' B ' : s = t ; } default : z = 4 ; }  '''
        """     swtich
                /     \
               (       {
               |        |-case A
               |        |
               |        |---- =
              choice    |    / \
                        |   x   1
                        |--if------------------------=
                        |              |        |   /  \
                        |              ==       |  w    v
                        |             /  \      |--case-B
                        |            x    2     |--=
                        |- default                / \
                        |------------=           s   t
                                    / \
                                   z   4"""
        root=cparser.parse(a)
        self.assertEqual(root.id,'switch')
        self.assertEqual(root.arity,'binary')
        choice=root.first
        self.assertEqual(valueof(choice),'choice')
        self.assertEqual(choice.id,'(identifier)')
        bracket=root.second
        self.assertEqual(bracket.id,'{')
        listofchoice=bracket.first
        casea=listofchoice[0]
        self.assertEqual(casea.id,'case')
        a=casea.first
        self.assertEqual(valueof(a),'A')
        self.assertEqual(a.id,'(identifier)')
        equal=listofchoice[1]
        x=equal.first
        self.assertEqual(valueof(x),'x')
        self.assertEqual(x.id,'(identifier)')
        one=equal.second
        self.assertEqual(valueof(one),'1')
        self.assertEqual(one.id,'(literal)')
        IF=listofchoice[2]
        self.assertEqual(IF.id,'if')
        bracket=IF.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        brace=IF.second
        self.assertEqual(brace.id,'{')
        listofif=brace.first
        equal=listofif[0]
        w=equal.first
        self.assertEqual(valueof(w),'w')
        v=equal.second
        self.assertEqual(valueof(v),'v')
        caseb=listofif[1]
        self.assertEqual(caseb.id,'case')
        b=caseb.first
        self.assertEqual(valueof(b),'B')
        self.assertEqual(a.id,'(identifier)')
        equal1=listofif[2]
        s=equal1.first
        self.assertEqual(valueof(s),'s')
        t=equal1.second
        self.assertEqual(valueof(t),'t')
        casec=listofchoice[3]
        self.assertEqual(casec.id,'default')
        equal3=listofchoice[4]
        z=equal3.first
        self.assertEqual(valueof(z),'z')
        self.assertEqual(z.id,'(identifier)')
        three=equal3.second
        self.assertEqual(valueof(three),'4')
        self.assertEqual(three.id,'(literal)')





################################################################################
################################################################################
################################################################################
# Test-> braces
################################################################################
class TestKeyword_braces(unittest.TestCase):
        pass
##       def testforloop(self):
##           { y ; };



if __name__=='__main__':
    if debug_scope==True or debug_All==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_scope)
        unittest.TextTestRunner(verbosity=2).run(suite)
    if debug_if_else==True or debug_All==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_if_else)
        unittest.TextTestRunner(verbosity=2).run(suite)
    if debug_do_while==True or debug_All==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_do_while)
        unittest.TextTestRunner(verbosity=2).run(suite)
    if debug_forloop==True or debug_All==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_forloop)
        unittest.TextTestRunner(verbosity=2).run(suite)
    if debug_switchcase==True or debug_All==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_switchcase)
        unittest.TextTestRunner(verbosity=2).run(suite)
    if debug_braces==True or debug_All==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_braces)
        unittest.TextTestRunner(verbosity=2).run(suite)


