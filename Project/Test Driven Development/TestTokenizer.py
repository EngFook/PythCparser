##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
                     This module is to test -> Tokenizer
                                                                             """
##"Test start."                                                               ##
class TestTokenizer(unittest.TestCase):

    def testAdvanceTokenShouldReturnThreeWordWithOneFinalEnd(self):
        global tokenzier
        tokenizer=Tokenizer('a b c ')
        gen=tokenizer.advanceToken()
        a=next(gen)
        self.assertEqual(a,'a')
        b=next(gen)
        self.assertEqual(b,'b')
        c=next(gen)
        self.assertEqual(c,'c')
        d=next(gen)
        self.assertIsNone(d)

    def testadvanceMultipleTime(self):
        global tokenzier
        tokenizer=Tokenizer('a b c ;')
        a=tokenizer.advance()
        self.assertEqual(valueof(a),'a')
        b=tokenizer.advance()
        self.assertEqual(valueof(b),'b')
        c=tokenizer.advance()
        self.assertEqual(valueof(c),'c')

    def testadvanceShouldReturnEndWhenNoMoreToken(self):
        global tokenzier
        tokenizer=Tokenizer('a')
        a=tokenizer.advance()
        self.assertEqual(valueof(a),'a')
        end=tokenizer.advance()
        self.assertEqual(valueof(end),'(end)')
        end=tokenizer.advance()
        self.assertEqual(valueof(end),'(end)')

    def testAdvanceShouldReturnEndWhenGivenEmptyString(self):
        global tokenzier
        tokenizer=Tokenizer('')
        end=tokenizer.advance()
        self.assertEqual(valueof(end),'(end)')

    def testAdvanceShouldReturnEndWhenGivenStringWithSpaces (self):
        global tokenzier
        tokenizer=Tokenizer(' ')
        end=tokenizer.advance()
        self.assertEqual(valueof(end),'(end)')

    def testAdvanceShouldReturnEndWhenGivenNone (self):
        global tokenzier
        tokenizer=Tokenizer(None)
        end=tokenizer.advance()
        self.assertEqual(valueof(end),'(end)')

    def testPeepAheadOnce(self):
        global tokenizer
        tokenizer=Tokenizer('a b')
        a=tokenizer.peepahead()
        self.assertEqual(valueof(a),'a')
        a=tokenizer.peepahead()
        self.assertEqual(valueof(a),'a')
        a=tokenizer.advance()
        self.assertEqual(valueof(a),'a')
        b=tokenizer.peepahead()
        self.assertEqual(valueof(b),'b')
        b=tokenizer.peepahead()
        self.assertEqual(valueof(b),'b')
        b=tokenizer.advance()
        self.assertEqual(valueof(b),'b')

    def testAdvanceBeforePeepAheadShouldPass(self):
        global tokenizer
        tokenizer=Tokenizer('a b')
        a=tokenizer.advance()
        self.assertEqual(valueof(a),'a')
        b=tokenizer.peepahead()
        self.assertEqual(valueof(b),'b')

    def testAdvanceBeforePeepAheadTwiceShouldPass(self):
        global tokenizer
        tokenizer=Tokenizer('a')
        a=tokenizer.advance()
        self.assertEqual(valueof(a),'a')
        end=tokenizer.advance()
        self.assertEqual(valueof(end),'(end)')
        end=tokenizer.peepahead()
        self.assertEqual(valueof(end),'(end)')

    def testShouldRaiseSyntaxErrorWhenAdvanceWhenExpectingDifferentWord(self):
        global tokenizer
        tokenizer=Tokenizer('a')
        self.assertRaises(SyntaxError,tokenizer.advance,'b')

    def testAdvanceShouldRaiseSyntaxErrorWhenExpectingDifferentWordWhenEncounterEnd(self):
        global tokenizer
        tokenizer=Tokenizer('a')
        tokenizer.advance('a')
        self.assertRaises(SyntaxError,tokenizer.advance,'a')
################################################################################
################################################################################
if __name__=='__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestTokenizer)
        unittest.TextTestRunner(verbosity=2).run(suite)