##"Files imported."                                                           ##
import unittest
import CParser
from Tokenizer import *
def valueof(symObj):
    return symObj.first
##                                                                            ##
"""
          This module is to test keyword -> switch case
                                                                             """
##"Test start here."                                                          ##
class TestKeyword_switch_case(unittest.TestCase):

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
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'switch')
        choice=root[0].first
        self.assertEqual(valueof(choice),'choice')
        self.assertEqual(choice.id,'(identifier)')
        bracket=root[0].second
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

    def test_back_address_switch_statement_with_condition_and_statement_block(self):
        a='''switch ( choice )
            {
                case ' A ' : x = 1 ;
                case ' C ' : y = 2 ; if ( x == 2 ) { w = v ;
                case ' B ' : s = t ; } default : z = 4 ; }  '''
        root=CParser.parse(a)
        bracket=root[0].second
        self.assertEqual(bracket.id,'{')
        listofchoice=bracket.address
        bracket=listofchoice['A'][1]
        listofchoice1=bracket.first
        casea=listofchoice1[0]
        self.assertEqual(casea.id,'case')
        a=casea.first
        self.assertEqual(valueof(a),'A')
        self.assertEqual(a.id,'(identifier)')
        self.assertEqual(bracket.id,'{')
        bracket=listofchoice['B'][1]
        listofchoice1=bracket.first
        equal=listofchoice1[0]
        w=equal.first
        self.assertEqual(valueof(w),'w')
        self.assertEqual(w.id,'(identifier)')
        v=equal.second
        self.assertEqual(valueof(v),'v')
        self.assertEqual(v.id,'(identifier)')

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
        root=CParser.parse(a)
        self.assertEqual(root[0].id,'switch')
        choice=root[0].first
        self.assertEqual(valueof(choice),'choice')
        self.assertEqual(choice.id,'(identifier)')
        bracket=root[0].second
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
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyword_switch_case)
        unittest.TextTestRunner(verbosity=2).run(suite)