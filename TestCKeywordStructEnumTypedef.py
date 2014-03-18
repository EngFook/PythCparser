##"Files imported."                                                           ##
import unittest
import Cparser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
    This module is for test keyword -> enum, struct, typedef
                                                                """
'''
    Set On/Off -> False = Off ; True = On
    To debug_all: set debug_all=True
                                            '''
debug_all=True
##"Test start here."                                                          ##
class TestKeyword_struct_enum_typedef(unittest.TestCase):
################################################################################
#Test-> enum
################################################################################
    def test_enum_with_workdays(self):
        a=''' enum DAY1
                        {
                            saturday ,
                            sunday  ,
                            monday ,
                            tuesday ,
                            wednesday ,
                            thursday ,
                            friday
                                        } workday ;         '''

        """                    enum (root[0])
                                |
                       ---------------------------------
                       |               |               |
                      DAY1             |               |
                                       |             workday
                                       {
                                       |
                                       ----saturday
                                       |
                                       ----sunday
                                       |
                                       ----monday
                                       |
                                       ----tuesday
                                       |
                                       ----wednesday
                                       |
                                       ----thursday
                                       |
                                       ----friday
                                                              """
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'enum')
        DAY=root[0].first
        self.assertEqual(valueof(DAY),'DAY1')
        brace=root[0].second
        self.assertEqual(brace.id,'{')
        saturday=brace.first[0]
        self.assertEqual(valueof(saturday),'saturday')
        sunday=brace.first[1]
        self.assertEqual(valueof(sunday),'sunday')
        monday=brace.first[2]
        self.assertEqual(valueof(monday),'monday')
        tuesday=brace.first[3]
        self.assertEqual(valueof(tuesday),'tuesday')
        wednesday=brace.first[4]
        self.assertEqual(valueof(wednesday),'wednesday')
        thursday=brace.first[5]
        self.assertEqual(valueof(thursday),'thursday')
        friday=brace.first[6]
        self.assertEqual(valueof(friday),'friday')
        workday=root[0].third[0]
        self.assertEqual(valueof(workday),'workday')

    def test_enum_with_workdays_and_value_assigned(self):
        a=''' enum DAY2
                        {
                            saturday ,
                            sunday = 0  ,
                            monday ,
                            tuesday ,
                            wednesday ,
                            thursday ,
                            friday
                                        } workday ;         '''

        """                    enum (root[0])
                                |
                       ---------------------------------
                       |               |               |
                      DAY2             |               [ __
                                       |                  |- workday
                                       {
                                       |
                                       ----saturday
                                       |
                                       ----sunday = 0
                                       |
                                       ----monday
                                       |
                                       ----tuesday
                                       |
                                       ----wednesday
                                       |
                                       ----thursday
                                       |
                                       ----friday
                                                              """
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'enum')
        DAY=root[0].first
        self.assertEqual(valueof(DAY),'DAY2')
        brace=root[0].second
        self.assertEqual(brace.id,'{')
        saturday=brace.first[0]
        self.assertEqual(valueof(saturday),'saturday')
        equal=brace.first[1]
        self.assertEqual(equal.id,'=')
        sunday=equal.first
        self.assertEqual(valueof(sunday),'sunday')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        monday=brace.first[2]
        self.assertEqual(valueof(monday),'monday')
        tuesday=brace.first[3]
        self.assertEqual(valueof(tuesday),'tuesday')
        wednesday=brace.first[4]
        self.assertEqual(valueof(wednesday),'wednesday')
        thursday=brace.first[5]
        self.assertEqual(valueof(thursday),'thursday')
        friday=brace.first[6]
        self.assertEqual(valueof(friday),'friday')
        workday=root[0].third[0]
        self.assertEqual(valueof(workday),'workday')

    def test_enum_with_included_digit_raiseSyntax(self):
        a=''' enum DAY3
                        {
                            saturday ,
                            sunday = 0  ,
                            100 ,
                            tuesday ,
                            wednesday ,
                            thursday ,
                            friday
                                        } workday ;         '''

        """                    enum (root[0])
                                |
                       ---------------------------------
                       |               |               |
                      DAY3             |               [ __
                                       |                  |- workday
                                       {
                                       |
                                       ----saturday
                                       |
                                       ----sunday = 0
                                       |
                                       ----monday
                                       |
                                       ----tuesday
                                       |
                                       ----wednesday
                                       |
                                       ----thursday
                                       |
                                       ----friday
                                                              """
        self.assertRaises(SyntaxError,Cparser.parse,a)

    def test_enum_with_workdays_and_value_assigned_and_declaration(self):
        a=''' enum DAY4
                        {
                            saturday ,
                            sunday = 0  ,
                            monday ,
                            tuesday ,
                            wednesday ,
                            thursday ,
                            friday
                                        } workday ;

                enum DAY4 x ; '''

        """                    enum (root[0])
                                |
                       ---------------------------------
                       |               |               |
                      DAY4             |               [ __
                                       |                  |- workday
                                       {
                                       |
                                       ----saturday
                                       |
                                       ----sunday = 0
                                       |
                                       ----monday
                                       |
                                       ----tuesday
                                       |
                                       ----wednesday
                                       |
                                       ----thursday
                                       |
                                       ----friday


                        enum DAY4 (root[1])
                            |
                            x
                                                              """
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'enum')
        DAY=root[0].first
        self.assertEqual(valueof(DAY),'DAY4')
        brace=root[0].second
        self.assertEqual(brace.id,'{')
        saturday=brace.first[0]
        self.assertEqual(valueof(saturday),'saturday')
        equal=brace.first[1]
        self.assertEqual(equal.id,'=')
        sunday=equal.first
        self.assertEqual(valueof(sunday),'sunday')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        monday=brace.first[2]
        self.assertEqual(valueof(monday),'monday')
        tuesday=brace.first[3]
        self.assertEqual(valueof(tuesday),'tuesday')
        wednesday=brace.first[4]
        self.assertEqual(valueof(wednesday),'wednesday')
        thursday=brace.first[5]
        self.assertEqual(valueof(thursday),'thursday')
        friday=brace.first[6]
        self.assertEqual(valueof(friday),'friday')
        workday=root[0].third[0]
        self.assertEqual(valueof(workday),'workday')
        self.assertEqual(root[1].id,'enum DAY4')
        x=root[1].first
        self.assertEqual(valueof(x),'x')

    def test_enum_with_workdays_and_value_assigned_and_declaration_alots(self):
        a=''' enum DAY5
                        {
                            saturday ,
                            sunday = 0  ,
                            monday ,
                            tuesday ,
                            wednesday ,
                            thursday ,
                            friday
                                        } workday , manyday , tireday ;

                enum DAY5 x ;
                enum DAY5 y ; '''

        """                    enum (root[0])
                                |
                       ---------------------------------
                       |               |               |
                      DAY5             |               [ __
                                       |                  |- workday
                                       {                  |- manyday
                                       |                  |- tireday
                                       ----saturday
                                       |
                                       ----sunday = 0
                                       |
                                       ----monday
                                       |
                                       ----tuesday
                                       |
                                       ----wednesday
                                       |
                                       ----thursday
                                       |
                                       ----friday


                        enum DAY5 (root[1])
                            |
                            x

                        enum DAY5 (root[2])
                            |
                            y
                                                              """
        root=Cparser.parse(a)
        self.assertEqual(root[0].id,'enum')
        DAY=root[0].first
        self.assertEqual(valueof(DAY),'DAY5')
        brace=root[0].second
        self.assertEqual(brace.id,'{')
        saturday=brace.first[0]
        self.assertEqual(valueof(saturday),'saturday')
        equal=brace.first[1]
        self.assertEqual(equal.id,'=')
        sunday=equal.first
        self.assertEqual(valueof(sunday),'sunday')
        zero=equal.second
        self.assertEqual(valueof(zero),'0')
        monday=brace.first[2]
        self.assertEqual(valueof(monday),'monday')
        tuesday=brace.first[3]
        self.assertEqual(valueof(tuesday),'tuesday')
        wednesday=brace.first[4]
        self.assertEqual(valueof(wednesday),'wednesday')
        thursday=brace.first[5]
        self.assertEqual(valueof(thursday),'thursday')
        friday=brace.first[6]
        self.assertEqual(valueof(friday),'friday')
        workday=root[0].third[0]
        self.assertEqual(valueof(workday),'workday')
        manyday=root[0].third[1]
        self.assertEqual(valueof(manyday),'manyday')
        tireday=root[0].third[2]
        self.assertEqual(valueof(tireday),'tireday')
        self.assertEqual(root[1].id,'enum DAY5')
        x=root[1].first
        self.assertEqual(valueof(x),'x')
        self.assertEqual(root[2].id,'enum DAY5')
        y=root[2].first
        self.assertEqual(valueof(y),'y')

    def test_enum_with_workdays_and_value_assigned_and_declaration_raiseSyntax(self):
        a=''' enum DAY5
                        {
                            saturday ,
                            sunday = 0  ,
                            monday ,
                            tuesday ,
                            wednesday ,
                            thursday ,
                            friday
                                        } workday , manyday , tireday ;

                enum DAY5 x ;
                DAY5 y ; '''

        """                    enum (root[0])
                                |
                       ---------------------------------
                       |               |               |
                      DAY5             |               [ __
                                       |                  |- workday
                                       {                  |- manyday
                                       |                  |- tireday
                                       ----saturday
                                       |
                                       ----sunday = 0
                                       |
                                       ----monday
                                       |
                                       ----tuesday
                                       |
                                       ----wednesday
                                       |
                                       ----thursday
                                       |
                                       ----friday


                        enum DAY5 (root[1])
                            |
                            x

                        enum DAY5 (root[2])
                            |
                        raise SyntaxError
                                                              """
        self.assertRaises(SyntaxError,Cparser.parse,a)
################################################################################
#Test-> struct
################################################################################
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

        root=Cparser.parse(a)
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
        root=Cparser.parse(a)
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
        root=Cparser.parse(a)
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
        self.assertRaises(SyntaxError,Cparser.parse,a)

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
        self.assertRaises(SyntaxError,Cparser.parse,a)

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
        root=Cparser.parse(a)
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
        root=Cparser.parse(a)
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
        root=Cparser.parse(a)
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
        root=Cparser.parse(a)
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

        self.assertRaises(SyntaxError,Cparser.parse,a)
##################################################################################
# Test-> typedef
##################################################################################
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
        root=Cparser.parse(a)
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
        root=Cparser.parse(a)
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
        self.assertRaises(SyntaxError,Cparser.parse,a)

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
        root=Cparser.parse(a)
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
        root=Cparser.parse(a)
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

        self.assertRaises(SyntaxError,Cparser.parse,a)

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
        root=Cparser.parse(a)
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
                     alias                              [
                                                       / \
                                                      80  None

                                                                    """
        root=Cparser.parse(a)
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
    if debug_all==True:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_struct_enum_typedef)
        unittest.TextTestRunner(verbosity=2).run(suite)