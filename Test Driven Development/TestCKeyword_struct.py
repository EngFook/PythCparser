##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
          This module is to test keyword -> struct
                                                                             """
##"Test start here."                                                          ##
class TestKeyword_struct(unittest.TestCase):

    def test_struct(self):
        a=''' struct Number {
                int a ;
                int b ;
                            } ; '''

        """         struct (root[0])
                       |
                -----------------
                |               |
              Number            {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

        """

        root=CParser.parse(a)
        self.assertEqual(root[0].id,'struct')
        Number=root[0].first
        self.assertEqual((Number.id),'StructIdentifier')
        self.assertEqual(valueof(Number),'Number')
        statement=root[0].second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')


    def test_struct_declare_one_statement(self):
        a=''' struct Number1 {
                int a ;
                int b ;
                            } ;
              struct Number1 x ; '''

        """         struct (root[0])
                       |
                -----------------
                |               |
              Number1           {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

                    struct Number1  (root[1])
                       |
                       |
                       x

                                            """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'struct')
        Number=root[0].first
        self.assertEqual((Number.id),'StructIdentifier')
        self.assertEqual(valueof(Number),'Number1')
        statement=root[0].second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        self.assertEqual(root[1].id,'struct Number1')
        x=root[1].first
        self.assertEqual(valueof(x),'x')

    def test_struct_declare_two_statement(self):
        a=''' struct Number2 {
                int a ;
                int b ;
                            } ;
              struct Number2 x ;
              struct Number2 y ; '''

        """         Struct (root[0])
                       |
                -----------------
                |               |
              Number2           {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

                    struct (root[1])
                       |
                       x


                    struct (root[2])
                       |
                       y

                                            """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'struct')
        Number=root[0].first
        self.assertEqual((Number.id),'StructIdentifier')
        self.assertEqual(valueof(Number),'Number2')
        statement=root[0].second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        self.assertEqual(root[1].id,'struct Number2')
        x=root[1].first
        self.assertEqual(valueof(x),'x')
        self.assertEqual(root[2].id,'struct Number2')
        y=root[2].first
        self.assertEqual(valueof(y),'y')

    def test_struct_declare_two_statement_same_variable_raiseSyntax(self):
        a=''' struct Number2 {
                int a ;
                int b ;
                            } ;
              struct Number2 x ;
              struct Number2 x ; '''

        """         Struct (root[0])
                       |
                -----------------
                |               |
              Number2           {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

                    struct (root[1])
                       |
                       x


                    struct (root[2])
                       |
                    raiseSyntax

                                            """
        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_struct_declare_two_statement_raiseSyntax(self):
        a=''' struct Number2 {
                int a ;
                int b ;
                            } ;
              struct Number2 x ;
              Number2 y ; '''

        """         Struct (root[0])
                       |
                -----------------
                |               |
              Number2           {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

                    struct (root[1])
                       |
                       x


                   (root[2])
                       |
                  raiseSyntax

                                            """
        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_struct_declare_one_statemnent_with_assign_value(self):
        a=''' struct Num {
                int a ;
                int b ;
                            } ;
              struct Num x = { 2 , 3 } ;

                                                '''

        """         Struct (root[0])
                       |
                -----------------
                |               |
              Num               {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

                              = (root[1])
                             / \
                   struct Num   {___
                          |         |-2
                          x         |-3



                                            """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'struct')
        Number=root[0].first
        self.assertEqual((Number.id),'StructIdentifier')
        self.assertEqual(valueof(Number),'Num')
        statement=root[0].second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        self.assertEqual(root[1].id,'=')
        struct=root[1].first
        self.assertEqual(struct.id ,'struct Num')
        x=struct.first
        self.assertEqual(valueof(x),'x')
        brace=root[1].second
        self.assertEqual(brace.id,'{')
        two=brace.first[0]
        self.assertEqual(valueof(two),'2')
        three=brace.first[1]
        self.assertEqual(valueof(three),'3')

    def test_struct_declare_two_statemnent_with_assign_value_(self):
        a=''' struct Num2 {
                int a ;
                int b ;
                            } ;
              struct Num2 x = { 2 , 3 } ;
              struct Num2 y = { 4 , 5 } ;

                                                '''

        """         Struct (root[0])
                       |
                -----------------
                |               |
              Num2              {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

                              = (root[1])
                             / \
                   struct Num2  {___
                          |         |-2
                          x         |-3

                              = (root[1])
                             / \
                   struct Num2  {___
                          |         |-4
                          y         |-5


                                            """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'struct')
        Number=root[0].first
        self.assertEqual((Number.id),'StructIdentifier')
        self.assertEqual(valueof(Number),'Num2')
        statement=root[0].second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        self.assertEqual(root[1].id,'=')
        struct=root[1].first
        self.assertEqual(struct.id ,'struct Num2')
        x=struct.first
        self.assertEqual(valueof(x),'x')
        brace=root[1].second
        self.assertEqual(brace.id,'{')
        two=brace.first[0]
        self.assertEqual(valueof(two),'2')
        three=brace.first[1]
        self.assertEqual(valueof(three),'3')
        struct=root[2].first
        self.assertEqual(struct.id ,'struct Num2')
        y=struct.first
        self.assertEqual(valueof(y),'y')
        brace=root[2].second
        self.assertEqual(brace.id,'{')
        four=brace.first[0]
        self.assertEqual(valueof(four),'4')
        five=brace.first[1]
        self.assertEqual(valueof(five),'5')

    def test_struct_with_declare_type(self):
        a=''' struct Datatype {
                int a ;
                int b ;
                            } data1 ;

                                                '''

        """         struct (root[0])
                       |
                -------------------------------------
                |               |                   |
             Datatype           {                   [---data1
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

                                            """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'struct')
        Datatype=root[0].first
        self.assertEqual(valueof(Datatype),'Datatype')
        statement=root[0].second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        data1=root[0].third[0]
        self.assertEqual(valueof(data1),'data1')

    def test_struct_without_declare_type(self):
        a=''' struct {
                int a ;
                int b ;
                            } data1 ;

                                                '''

        """         struct (root[0])
                       |
                -------------------------------------
                |               |                   |
              None              {                   [---data1
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b

                                            """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'struct')
        none=root[0].first
        self.assertIsNone(none)
        statement=root[0].second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        data1=root[0].third[0]
        self.assertEqual(valueof(data1),'data1')

    def test_struct_declare_two_statemnent_with_same_variable_raiseSyntax(self):
        a=''' struct Num3 {
                int a ;
                int b ;
                            } ;
              struct Num3 x = { 2 , 3 }
              struct Num3 x = { 4 , 5 }

                                                '''
        self.assertRaises(SyntaxError,CParser.parse,a)
################################################################################
################################################################################
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_struct)
        unittest.TextTestRunner(verbosity=2).run(suite)