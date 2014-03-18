##"Files imported."                                                           ##
import unittest
import CParser
from CKeyword import defineTable
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
    This module is to test keyword -> #define
                                                    """
'''
    Set On/Off -> False = Off ; True = On
    To debug_all: set debug_all=True
                                            '''
debug_all=True
##"Test start here."                                                          ##
class TestKeyword_define(unittest.TestCase):
    def test_define_statement(self):
        a='#define Str 10 + ('
        """ #define (root[0])
               |
              Str
               |
            ' 10 + ('       """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'10 + (')

    def test_define_statement_with_spaces(self):
        a='#  define Str 10 + ('
        """    # (root[0])
               |
            define
               |
              Str
               |
            ' 10 + ('       """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#')
        define=root[0].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'10 + (')

    def test_two_define_statement_with_no_spaces(self):
        a='''#define Str 10 + (
             #define Strtwo 20 * y'''
        """ #define (root[0])
               |
              Str
               |
            ' 10 + ('

            #define (root[1])
               |
              Strtwo
               |
            ' 20 * y '      """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'10 + (')
        self.assertEqual(root[1].id,'#define')
        Strsymbol=root[1].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Strtwo')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'20 * y')

    def test_two_define_statement_with_spaces(self):
        a='''# define Str 10 + (
             # define Strtwo 20 * y'''
        """    # (root[0])
               |
            define
               |
              Str
               |
            ' 10 + ('

               # (root[1])
               |
            define
               |
              Strtwo
               |
            ' 20 * y '      """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#')
        define=root[0].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'10 + (')
        self.assertEqual(root[1].id,'#')
        define=root[1].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[1].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Strtwo')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'20 * y')

    def test_two_define_statement_with_no_spaces_and_spaces(self):
        a='''#define Str 10 + (
             # define Strtwo 20 * y'''
        """ #define (root[0])
               |
              Str
               |
            ' 10 + ( '

               # (root[1])
               |
            define
               |
              Strtwo
               |
            ' 20 * y '      """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'10 + (')
        self.assertEqual(root[1].id,'#')
        define=root[1].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[1].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Strtwo')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'20 * y')

    def test_two_define_statement_with_spaces_and_no_spaces(self):
        a='''# define Str 10 + (
             #define Strtwo 20 * y'''
        """    # (root[0])
               |
            define
               |
              Str
               |
            ' 10 + ( '

            #define (root[1])
               |
              Strtwo
               |
            ' 20 * y '      """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#')
        define=root[0].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'10 + (')
        self.assertEqual(root[1].id,'#define')
        Strsymbol=root[1].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Strtwo')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'20 * y')

    def test_define_statement_with_backslash(self):
        a='''#define Str \
             10 + ('''
        """ #define (root[0])
               |
              Str
               |
            ' 10 + ('       """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'10 + (')

    def test_define_statement_with_multiple_backslash(self):
        a='''#define Str \
             \
             \
             10 + ('''
        """ #define (root[0])
               |
              Str
               |
            ' 10 + ('       """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'10 + (')

    def test_two_define_statement_with_same_constantidentifier_but_different_constant_raiseSyntax(self):
        a='''#define Str 10 + (
             # define Str 20 * y'''
        """    # (root[0])
               |
            define
               |
              Str
               |
            ' 10 + ( '

            #define (root[1])
               |
              Str
               |
            ' 20 * y '      """

        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_complicated_define(self):
        a='''   #define StrAAA \
                \
                \
                123 + 123
                # define StrBBB 333
                # define StrCCC A1B2C3
                # define StrDDD 652
                \
                \
                # define StrEEE 123
                #define StrFFF zzzz
                                        '''
        """(root[0])->
           (root[1])->
           (root[2])->      Same as the structure above
           (root[3])->
           (root[4])->
           (root[5])->
                                """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'StrAAA')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'123 + 123')

        self.assertEqual(root[1].id,'#')
        define=root[1].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[1].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'StrBBB')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'333')

        self.assertEqual(root[2].id,'#')
        define=root[2].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[2].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'StrCCC')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'A1B2C3')

        self.assertEqual(root[3].id,'#')
        define=root[3].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[3].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'StrDDD')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'652')

        self.assertEqual(root[4].id,'#')
        define=root[4].second
        self.assertEqual(valueof(define),'define')
        Strsymbol=root[4].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'StrEEE')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'123')

        self.assertEqual(root[5].id,'#define')
        Strsymbol=root[5].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'StrFFF')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'zzzz')

    def test_define_replace_constantidentifier_to_expression(self):
          a='''#define Str  2 + 3 +
           { Str 4 + 5 * 6 * 7 * 8 ; }'''
          """       #define (root[0])
                       |
                      Str
                       |
                     2 + 3 +


                       { (root[1])
                       |
                       ------_____+____
                            /          \
                           +            *
                         /   \         /  \
                        +     4       *    8
                       / \          /  \
                      2   3        *    7
                                  / \
                                 5   6
                                            """
          root=CParser.parse(a)
          self.assertEqual(root[0].id,'#define')
          Strsymbol=root[0].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Str')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'2 + 3 +')
          brace=root[1]
          self.assertEqual(brace.id,'{')
          plus1=brace.first[0]
          self.assertEqual(plus1.id,'+')
          self.assertEqual(plus1.arity,'binary')
          plus2=plus1.first
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
          multiply=plus1.second
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

    def test_define_replace_constantidentifier_to_expression_in_middle(self):
          a='''#define Str 5 * 6 *
                { 2 + 3 + 4 + Str 7 * 8 ; }'''
          """       #define (root[0])
                       |
                      Str
                       |
            '       5 * 6 *

                       { (root[1])
                       |
                       ------_____+____
                            /          \
                           +            *
                         /   \         /  \
                        +     4       *    8
                       / \          /  \
                      2   3        *    7
                                  / \
                                 5   6          """

          root=CParser.parse(a)
          self.assertEqual(root[0].id,'#define')
          Strsymbol=root[0].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Str')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'5 * 6 *')
          brace=root[1]
          self.assertEqual(brace.id,'{')
          plus1=brace.first[0]
          self.assertEqual(plus1.id,'+')
          self.assertEqual(plus1.arity,'binary')
          plus2=plus1.first
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
          multiply=plus1.second
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

    def test_statement_define_with_replace_constantidentifier_for_if_statement(self):
        a=''' #define Str if ( x
            { Str == 2 ) else  y = 5 ; }'''
        """          #define (root[0])
                       |
                      Str
                       |
                    if ( x


                          { (root[1])
                          |
                          if
                          |
                          |____________
                          |          else
                          |           |
                          (           |
                          |           |
                          |           |
                          |           |
                          ==          |
                         /  \         |
                        x    2        |
                                      |
                                      |
                                      |
                                      |-------=
                                            /   \
                                           y     5
                                                    """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'if ( x')
        brace=root[1]
        self.assertEqual(brace.id,'{')
        if_id=brace.first[0]
        self.assertEqual(if_id.id,'if')
        bracket=if_id.first
        self.assertEqual(bracket.id,'(')
        equalequal=bracket.first
        self.assertEqual(equalequal.id,'==')
        x=equalequal.first
        self.assertEqual(valueof(x),'x')
        two=equalequal.second
        self.assertEqual(valueof(two),'2')
        else1=if_id.second
        self.assertEqual(else1.id,'else')
        equal=else1.first
        self.assertEqual(equal.id,'=')
        y=equal.first
        self.assertEqual(valueof(y),'y')
        five=equal.second
        self.assertEqual(valueof(five),'5')

    def test_define_replace_constantidentifier_for_forloop(self):
        a='''#define Str for ( x = 0 ; x
            { Str = 5 ; x ++ ) x + y = z ; }'''
        """        #define (root[0])
                       |
                      Str
                       |
                    for ( x = 0 ; x


               { (root[1])
               |
              for-----------------------------
                  |         |      |        |
                  =         |      ++       =
                 / \        =      |      /  \
                x   0      / \     x     +    z
                          x   5         / \
                                       x   y
                                                    """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'for ( x = 0 ; x')
        brace=root[1]
        self.assertEqual(brace.id,'{')
        for_id=brace.first[0]
        self.assertEqual(for_id.id,'for')
        equal=for_id.first
        self.assertEqual(equal.id,'=')
        x=equal.first
        self.assertEqual(valueof(x),'x')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        equal2=for_id.second
        self.assertEqual(equal2.id,'=')
        x2=equal2.first
        self.assertEqual(valueof(x2),'x')
        five=equal2.second
        self.assertEqual(valueof(five),'5')
        plusplus=for_id.third
        self.assertEqual(plusplus.id,'++')
        x3=plusplus.first
        self.assertEqual(valueof(x3),'x')
        equal3=for_id.four
        self.assertEqual(equal3.id,'=')
        plus=equal3.first
        self.assertEqual(plus.id,'+')
        x=plus.first
        self.assertEqual(valueof(x),'x')
        y=plus.second
        self.assertEqual(valueof(y),'y')
        z=equal3.second
        self.assertEqual(valueof(z),'z')

    def test_define_replace_constantidentifier_for_forloop_Str_is_in_between(self):
        a='''#define Str x = 0 ; x
            { for ( Str = 5 ; x ++ ) x + y = z ; }'''
        """        #define (root[0])
                       |
                      Str
                       |
                   x = 0 ; x

               { (root[1])
               |
              for-----------------------------
                  |         |      |        |
                  =         |      ++       =
                 / \        =      |      /  \
                x   0      / \     x     +    z
                          x   5         / \
                                       x   y
                                                    """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'#define')
        Strsymbol=root[0].first
        self.assertEqual((Strsymbol.id),'ConstantIdentifier')
        self.assertEqual(valueof(Strsymbol),'Str')
        statement=Strsymbol.constantidentifier
        self.assertEqual(Strsymbol.constantidentifier,'x = 0 ; x')
        brace=root[1]
        self.assertEqual(brace.id,'{')
        for_id=brace.first[0]
        self.assertEqual(for_id.id,'for')
        equal=for_id.first
        self.assertEqual(equal.id,'=')
        x=equal.first
        self.assertEqual(valueof(x),'x')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        equal2=for_id.second
        self.assertEqual(equal2.id,'=')
        x2=equal2.first
        self.assertEqual(valueof(x2),'x')
        five=equal2.second
        self.assertEqual(valueof(five),'5')
        plusplus=for_id.third
        self.assertEqual(plusplus.id,'++')
        x3=plusplus.first
        self.assertEqual(valueof(x3),'x')
        equal3=for_id.four
        self.assertEqual(equal3.id,'=')
        plus=equal3.first
        self.assertEqual(plus.id,'+')
        x=plus.first
        self.assertEqual(valueof(x),'x')
        y=plus.second
        self.assertEqual(valueof(y),'y')
        z=equal3.second
        self.assertEqual(valueof(z),'z')

    def test_two_define_replace_constantidentifier_to_expression(self):
          a=''' #define Strtwo 100 + 200 +
                #define Str  2 + 3 +
                { Str 4 + 5 * 6 * 7 * 8 ; }'''
          """       #define (root[0])
                       |
                      Strtwo
                       |
                   100 + 200 +

                    #define (root[1])
                       |
                      Str
                       |
                     2 + 3 +

                       { (root[2])
                       |
                       ------_____+____
                            /          \
                           +            *
                         /   \         /  \
                        +     4       *    8
                       / \          /  \
                      2   3        *    7
                                  / \
                                 5   6
                                                """
          root=CParser.parse(a)
          self.assertEqual(root[0].id,'#define')
          Strsymbol=root[0].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strtwo')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'100 + 200 +')
          self.assertEqual(root[1].id,'#define')
          Strsymbol=root[1].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Str')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'2 + 3 +')
          brace=root[2]
          self.assertEqual(brace.id,'{')
          plus1=brace.first[0]
          self.assertEqual(plus1.id,'+')
          self.assertEqual(plus1.arity,'binary')
          plus2=plus1.first
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
          multiply=plus1.second
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

    def test_three_define_replace_constantidentifier_to_expression(self):
          a=''' #define Strthree 12345 + 12345678 +
                #define Str  2 + 3 +
                #define Strtwo 100 + 200 +
                { Str 4 + 5 * 6 * 7 * 8 ; }'''
          """       #define (root[0])
                       |
                      Strthree
                       |
                12345 + 12345678 +

                    #define (root[1])
                       |
                      Str
                       |
                     2 + 3 +

                    #define (root[2])
                       |
                      Strtwo
                       |
                   100 + 200 +

                       { (root[3])
                       |
                       ------_____+____
                            /          \
                           +            *
                         /   \         /  \
                        +     4       *    8
                       / \          /  \
                      2   3        *    7
                                  / \
                                 5   6
                                                    """
          root=CParser.parse(a)
          self.assertEqual(root[0].id,'#define')
          Strsymbol=root[0].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strthree')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'12345 + 12345678 +')
          self.assertEqual(root[1].id,'#define')
          Strsymbol=root[1].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Str')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'2 + 3 +')
          self.assertEqual(root[2].id,'#define')
          Strsymbol=root[2].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strtwo')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'100 + 200 +')
          brace=root[3]
          self.assertEqual(brace.id,'{')
          plus1=brace.first[0]
          self.assertEqual(plus1.id,'+')
          self.assertEqual(plus1.arity,'binary')
          plus2=plus1.first
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
          multiply=plus1.second
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

    def test_three_define_replace_constantidentifier_to_expression_withbackslash_and_inorder_sequence(self):
          a=''' #define Str  \
                2 + 3 +
                #define Strthree \
                \
                \
                12345 + 12345678 +
                #define Strtwo 100 + 200 +
                { Str 4 + 5 * 6 * 7 * 8 ; }'''
          """       #define (root[0])
                       |
                      Str
                       |
                     2 + 3 +

                    #define (root[1])
                       |
                      Strthree
                       |
                 12345 + 12345678 +

                    #define (root[2])
                       |
                      Strtwo
                       |
                   100 + 200 +

                       { (root[3])
                       |
                       ------_____+____
                            /          \
                           +            *
                         /   \         /  \
                        +     4       *    8
                       / \          /  \
                      2   3        *    7
                                  / \
                                 5   6
                                                    """
          root=CParser.parse(a)
          self.assertEqual(root[0].id,'#define')
          Strsymbol=root[0].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Str')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'2 + 3 +')
          self.assertEqual(root[1].id,'#define')
          Strsymbol=root[1].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strthree')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'12345 + 12345678 +')
          self.assertEqual(root[2].id,'#define')
          Strsymbol=root[2].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strtwo')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'100 + 200 +')
          brace=root[3]
          self.assertEqual(brace.id,'{')
          plus1=brace.first[0]
          self.assertEqual(plus1.id,'+')
          self.assertEqual(plus1.arity,'binary')
          plus2=plus1.first
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
          multiply=plus1.second
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

    def test_comepletely_define_replace_constantidentifier_to_expression_with_backslash_and_inorder_sequence_in_middle(self):
          a=''' #define Strtwo 100 + 200 +
                #define Strthree \
                \
                \
                12345 + 12345678 +
                #          define Str 4 + 5 *
                { 2 + 3 + Str 6 * 7 * 8 ; }'''
          """       #define (root[0])
                       |
                      Strtwo
                       |
                   100 + 200 +

                    #define (root[1])
                       |
                      Strthree
                       |
                 12345 + 12345678 +

                    #define (root[2])
                       |
                      Str
                       |
                     4 + 5 *

                       { (root[3])
                       |
                       ------_____+____
                            /          \
                           +            *
                         /   \         /  \
                        +     4       *    8
                       / \          /  \
                      2   3        *    7
                                  / \
                                 5   6
                                                    """
          root=CParser.parse(a)
          self.assertEqual(root[0].id,'#define')
          Strsymbol=root[0].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strtwo')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'100 + 200 +')
          self.assertEqual(root[1].id,'#define')
          Strsymbol=root[1].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strthree')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'12345 + 12345678 +')
          self.assertEqual(root[2].id,'#')
          define=root[2].second
          self.assertEqual(valueof(define),'define')
          Strsymbol=root[2].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Str')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'4 + 5 *')
          brace=root[3]
          self.assertEqual(brace.id,'{')
          plus1=brace.first[0]
          self.assertEqual(plus1.id,'+')
          self.assertEqual(plus1.arity,'binary')
          plus2=plus1.first
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
          multiply=plus1.second
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

    def test_define_replace_constantidentifier_to_expression_with_straigh_away_replace(self):
          a=''' #define Strtwo 100 + 200 +
                #define Strthree \
                \
                \
                12345 + 12345678 +
                #          define Str 2 + 3 +
                Str 4 + 5 * 6 * 7 * 8 ; '''
          """       #define (root[0])
                       |
                      Strtwo
                       |
                   100 + 200 +

                    #define (root[1])
                       |
                      Strthree
                       |
                 12345 + 12345678 +

                    #define (root[2])
                       |
                      Str
                       |
                     2 + 3 +

                       { (root[3])
                       |
                       ------_____+____
                            /          \
                           +            *
                         /   \         /  \
                        +     4       *    8
                       / \          /  \
                      2   3        *    7
                                  / \
                                 5   6
                                                    """
          root=CParser.parse(a)
          self.assertEqual(root[0].id,'#define')
          Strsymbol=root[0].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strtwo')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'100 + 200 +')
          self.assertEqual(root[1].id,'#define')
          Strsymbol=root[1].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strthree')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'12345 + 12345678 +')
          self.assertEqual(root[2].id,'#')
          define=root[2].second
          self.assertEqual(valueof(define),'define')
          Strsymbol=root[2].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Str')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'2 + 3 +')
          plus1=root[3]
          self.assertEqual(plus1.id,'+')
          self.assertEqual(plus1.arity,'binary')
          plus2=plus1.first
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
          multiply=plus1.second
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

    def test_comepletely_define_replace_constantidentifier_to_statement_for(self):
          a=''' #define Strtwo 100 + 200 +
                # define Str for ( x = 0 ; x
                # define Strthree \
                \
                \
                2 + 3 +
              Str = 5 ; x ++ ) x + y = z ; '''

          """  #define (root[0])
                       |
                      Strtwo
                       |
                   100 + 200 +

                    #define (root[1])
                       |
                      Str
                       |
                 for ( x = 0 ; x

                    #define (root[2])
                       |
                      Strthree
                       |
                     2 + 3 +

               { (root[3])
               |
              for-----------------------------
                  |         |      |        |
                  =         |      ++       =
                 / \        =      |      /  \
                x   0      / \     x     +    z
                          x   5         / \
                                       x   y
                                                    """
          root=CParser.parse(a)
          self.assertEqual(root[0].id,'#define')
          Strsymbol=root[0].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strtwo')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'100 + 200 +')
          self.assertEqual(root[1].id,'#')
          define=root[1].second
          self.assertEqual(valueof(define),'define')
          Strsymbol=root[1].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Str')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'for ( x = 0 ; x')
          self.assertEqual(root[2].id,'#')
          define=root[2].second
          self.assertEqual(valueof(define),'define')
          Strsymbol=root[2].first
          self.assertEqual((Strsymbol.id),'ConstantIdentifier')
          self.assertEqual(valueof(Strsymbol),'Strthree')
          statement=Strsymbol.constantidentifier
          self.assertEqual(Strsymbol.constantidentifier,'2 + 3 +')
          for_id=root[3]
          self.assertEqual(for_id.id,'for')
          equal=for_id.first
          self.assertEqual(equal.id,'=')
          x=equal.first
          self.assertEqual(valueof(x),'x')
          zero=equal.second
          self.assertEqual(valueof(zero),'0')
          equal2=for_id.second
          self.assertEqual(equal2.id,'=')
          x2=equal2.first
          self.assertEqual(valueof(x2),'x')
          five=equal2.second
          self.assertEqual(valueof(five),'5')
          plusplus=for_id.third
          self.assertEqual(plusplus.id,'++')
          x3=plusplus.first
          self.assertEqual(valueof(x3),'x')
          equal3=for_id.four
          self.assertEqual(equal3.id,'=')
          plus=equal3.first
          self.assertEqual(plus.id,'+')
          x=plus.first
          self.assertEqual(valueof(x),'x')
          y=plus.second
          self.assertEqual(valueof(y),'y')
          z=equal3.second
          self.assertEqual(valueof(z),'z')
################################################################################
################################################################################
if __name__ == '__main__':
    if debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_define)
        unittest.TextTestRunner(verbosity=2).run(suite)