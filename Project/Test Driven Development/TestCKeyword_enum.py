##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
          This module is to test keyword -> enum
                                                                             """
##"Test start here."                                                          ##
class TestKeyword_enum(unittest.TestCase):

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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        self.assertRaises(SyntaxError,CParser.parse,a)

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
        root=CParser.parse(a)
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
        root=CParser.parse(a)
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
        self.assertRaises(SyntaxError,CParser.parse,a)
################################################################################
################################################################################
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_enum)
        unittest.TextTestRunner(verbosity=2).run(suite)