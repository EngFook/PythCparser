##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
                  This module is to test keyword -> typedef
                                                                             """
##"Test start here."                                                          ##
class TestKeyword_typedef(unittest.TestCase):

    def test_typedef_struct(self):
        a='''typedef struct {
                    int a ;
                    int b ;
                            } Data ;'''

        """                 typedef (root[0])
                                |
                       ----------------------------------
                       |                                |
                       |                                []--Data
                       |
                       |
                     Struct
                       |
                -----------------
                |               |
               None             {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b
                                                           """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'typedef')
        struct=root[0].first
        self.assertEqual((struct.id),'struct')
        self.assertIsNone(struct.first)
        statement=struct.second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        data=root[0].second[0]
        self.assertEqual(valueof(data),'Data')

    def test_typedef_struct_with_declare_type(self):
        a='''typedef struct Datatype1 {
                    int a ;
                    int b ;
                            } Datatype ;'''

        """                 typedef (root[0])
                                |
                       ----------------------------------
                       |                                |
                       |                                []--Datatype
                       |
                       |
                     Struct
                       |
                -----------------
                |               |
               Data             {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b
                                                           """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'typedef')
        struct=root[0].first
        self.assertEqual((struct.id),'struct')
        Data=struct.first
        self.assertEqual(valueof(Data),'Datatype1')
        statement=struct.second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        data=root[0].second[0]
        self.assertEqual(valueof(data),'Datatype')

    def test_typedef_struct_with_declare_type_twice_raiseSyntax(self):
        a='''typedef struct Datatype1 {
                    int a ;
                    int b ;
                            } Datatype , Datatype ;'''

        """                 typedef (root[0])
                                |
                       ----------------------------------
                       |                                |
                       |                                []--Data
                       |
                       |
                     Struct
                       |
                -----------------
                |               |
               Data             {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b
                                                           """
        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_typedef_struct_with_declaration(self):
        a='''typedef struct {
                    int a ;
                    int b ;
                            } Data2 ;
                    Data2 x ;                '''

        """                 typedef (root[0])
                                |
                       ----------------------------------
                       |                                |
                       |                               Data2
                       |
                     Struct
                       |
                -----------------
                |               |
               None             {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b


                        Data2 (root[1])
                         |
                         x

                                                          """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'typedef')
        struct=root[0].first
        self.assertEqual((struct.id),'struct')
        self.assertIsNone(struct.first)
        statement=struct.second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        Data=root[0].second[0]
        self.assertEqual(valueof(Data),'Data2')
        Data2=root[1]
        self.assertEqual((Data2.id),'Data2')
        x=Data2.first
        self.assertEqual(valueof(x),'x')


    def test_typedef_struct_with_two_declaration(self):
        a='''typedef struct {
                    int a ;
                    int b ;
                            } Data3 ;
                    Data3 x ;
                    typedef Data3 y ;'''

        """                 typedef (root[0])
                                |
                       ----------------------------------
                       |                                |
                       |                               Data3
                       |
                     Struct
                       |
                -----------------
                |               |
               None             {
                                |_____int
                                |      |
                                |      a
                                |
                                |______int
                                        |
                                        b


                         Data3 (root[1])
                          |
                          x

                        typedef (root[2])
                        /   \
                     Data3     y

                                                          """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'typedef')
        struct=root[0].first
        self.assertEqual((struct.id),'struct')
        self.assertIsNone(struct.first)
        statement=struct.second
        inta=statement.first[0]
        self.assertEqual(inta.id,'int')
        a=inta.first
        self.assertEqual(valueof(a),'a')
        intb=statement.first[1]
        self.assertEqual(intb.id,'int')
        b=intb.first
        self.assertEqual(valueof(b),'b')
        Data=root[0].second[0]
        self.assertEqual(valueof(Data),'Data3')

        Data3=root[1]
        self.assertEqual(Data3.id,'Data3')
        x=Data3.first
        self.assertEqual(valueof(x),'x')

        typedef2=root[2]
        self.assertEqual(typedef2.id,'typedef')
        Data3=typedef2.first
        self.assertEqual(Data3.id,'Data3')
        y=Data3.first
        self.assertEqual(valueof(y),'y')

    def test_typedef_struct_with_two_declaration_same_variable_raiseSyntax(self):
        a='''typedef struct {
                    int a ;
                    int b ;
                            } Data66 ;
                    Data66 x ;
                    typedef Data66 x ;               '''

        self.assertRaises(SyntaxError,CParser.parse,a)

    def test_typedef_char_alias(self):
        a=''' typedef char alias [ 80 ]'''

        """                 typedef (root[0])
                                |
                       ----------------------------------
                       |                                |
                       |                               char
                       |                                |
                     alias                              [
                                                        |
                                                        80

                                                                    """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'typedef')
        alias=root[0].first
        self.assertEqual(valueof(alias),'alias')
        char=root[0].second
        self.assertEqual(char.id,'char')
        bracket=char.first
        self.assertEqual(bracket.id,'[')
        eighty=bracket.first
        self.assertEqual(valueof(eighty),'80')

    def test_typedef_char_alias_with_pointer(self):
        a=''' typedef char * alias [ 80 ]'''

        """                 typedef (root[0])
                                |
                       ----------------------------------
                       |                                |
                       |                               char
                       |                                |
                       |                                *
                       |                                |
                     alias                              ['
                                                        |
                                                        80

                                                                    """
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'typedef')
        alias=root[0].first
        self.assertEqual(valueof(alias),'alias')
        char=root[0].second
        self.assertEqual(char.id,'char')
        pointer=char.first
        self.assertEqual(pointer.id,'*')
        bracket=pointer.first
        self.assertEqual(bracket.id,'[')
        eighty=bracket.first
        self.assertEqual(valueof(eighty),'80')
################################################################################
################################################################################
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_typedef)
        unittest.TextTestRunner(verbosity=2).run(suite)