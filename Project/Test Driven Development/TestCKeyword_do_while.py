##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
          This module is to test keyword -> do while
                                                                             """
##"Test start here."                                                          ##
class TestKeyword_do_while(unittest.TestCase):

    def test_while_statement_with_body_raiseSyntax(self):
        a='while x'
        """while
             |
             x
                """
        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_while_statement_with_condition_only(self):
        a='while ( x < 1 ) ;'
        """ while
             |
             (
             |
             <
            / \
           x   1"""
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'while')
        bracket=root[0].first
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
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'while')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        smaller=bracket.first
        self.assertEqual(smaller.id,'<')
        x=smaller.first
        self.assertEqual(valueof(x),'x')
        one=smaller.second
        self.assertEqual(valueof(one),'1')
        plusplus=root[0].second
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

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'while')
        bracket=root[0].first
        self.assertEqual(bracket.id,'(')
        smaller=bracket.first
        self.assertEqual(smaller.id,'<')
        x=smaller.first
        self.assertEqual(valueof(x),'x')
        one=smaller.second
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
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'do')
        bracket=root[0].first
        self.assertEqual(bracket.id,'{')
        plusplus=bracket.first[0]
        self.assertEqual(plusplus.id,'++')
        x=plusplus.first
        self.assertEqual(valueof(x),'x')
        while1=root[0].second
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
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_do_while)
        unittest.TextTestRunner(verbosity=2).run(suite)