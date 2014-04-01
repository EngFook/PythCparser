#-------------------------------------------------------------------------------
# Name:        PythCparser
# Purpose:     To parse and interpret C language by using Python.
#
# Author:      Goh Eng Fook
#              Lim Bing Ran
#
# Created:     31/03/2013
# Copyright:   (c) 2013-2014, Goh Eng Fook & Lim Bing Ran
# Licence:     GPLv3
#-------------------------------------------------------------------------------
##"Files imported."                                                           ##
from CParser import *
import CInterperter
from CScope import *
##"Initialization."                                                           ##
def NextDemonstrationCode():
    a=oneTimeParse('''
                        char Type_Any_Word_To_Continue ;
                        scanf ( " %s " , Type_Any_Word_To_Continue  ) ;

                   ''')
    return a

def clear():
        clearParseEnviroment()
        scope.__init__()
        Initializationscan()
        Initialization()
        CInterperter.Runinterpreter(NextDemonstrationCode())

def end():
    a=oneTimeParse('''
                        char Type_Any_Word_To_Exit ;
                        printf ( " Program End. " ) ;
                        scanf ( " %s " , Type_Any_Word_To_Exit  ) ;

                   ''')
    clearParseEnviroment()
    scope.__init__()
    Initializationscan()
    Initialization()
    CInterperter.Runinterpreter(a)
## "First Run. "                                                              ##
FirstRun=oneTimeParse('''
int main ( )
{   char Type_Any_Word_To_Continue ;
    printf ( " These desmonstrations are without scanf. " ) ;
    scanf ( " %s " , Type_Any_Word_To_Continue  ) ;
}
''')
CInterperter.Runinterpreter(FirstRun)
################################################################################
#C-program code demonstration:
################################################################################
def  BubbleSort():
    a=oneTimeParse('''
                    printf ( " 1st C program is BubbleSort. " ) ;
                    void BubbleSort ( int [ ] , int ) ;
                    int main ( )
                    {
                        int a [ 5 ] , n , c , d , swap , i ;
                        a [ 0 ] = 35 ;
                        a [ 1 ] = 2 ;
                        a [ 2 ] = 3 ;
                        a [ 3 ] = 14 ;
                        a [ 4 ] = 42 ;
                        n = 5 ;
                        printf ( " Before sorting the array : " ) ;
                        for ( d = 0 ; d < n ; d ++ )
                        {
                            printf ( " %d " , a [ d ] ) ;
                        }
                        BubbleSort ( a [ ] , n ) ;
                        printf ( " After sorting the array : " ) ;
                        for ( d = 0 ; d < n ; d ++ )
                        {
                            printf ( " %d " , a [ d ] ) ;
                        }
                    }
                    void BubbleSort ( int a [ ] , int size )
                    {
                        int c , d ;

                        for ( c = 0 ; c < (   size - 1 ) ; c ++ )
                        {
                            for ( d = 0 ; d < size - c - 1 ; d ++ )
                            {
                                if ( a [ d ] > a [ d + 1 ] )
                                {
                                    swap = a [ d ] ;
                                    a [ d ] = a [ d + 1 ] ;
                                    a [ d + 1 ] = swap ;
                                }
                            }
                        }
                    }
    ''')
    return a

def FindGreatestNumber():
    a=oneTimeParse('''
    int main ( )
    {   float a , b , c ;
          printf ( " 2nd C program is to find "Greatest Number". " ) ;
          printf ( " Please enter three numbers : " ) ;
          a = 1 ;
          b = 3 ;
          c = 2 ;
          if ( a >= b && a >= c )
            printf ( " Largest number = %.5f " , a ) ;
          if ( b >= a && b >= c )
             printf ( " Largest number = %.5f " , b ) ;
          if ( c >= a && c >= b )
             printf ( " Largest number = %.5f " , c ) ;
          return 0 ;
    }
    ''')
    return a

def CheckLeapYear():
    a=oneTimeParse('''
    int main ( )
    {
          int year ;
          printf ( " 3rd C program is to Check Leap Year. " ) ;
          printf ( " Enter a year: " ) ;
          year = 1992 ;
          if ( year % 4 == 0 )
          {
              if ( year % 100 == 0 )
              {
                  if ( year % 400 == 0 )
                     printf ( " %d is a leap year. " , year ) ;
                  else
                     printf ( " %d is not a leap year. " , year ) ;
              }
              else
                 printf ( " %d is a leap year. " , year ) ;
          }
          else
             printf ( " %d is not a leap year. " , year ) ;
          return 0 ;
    }
    ''' )
    return a

def ProgramToInsertAnElementInAnArray():
    a=oneTimeParse('''
       int main ( )
    {
       int array [ 100 ] , position , c , n , value , d ;
       printf ( " 4th C program is to Insert An Element Into An Array. " ) ;
       printf ( " Enter number of elements in array " ) ;
       n = 5 ;

       printf ( " Enter %d elements " , n ) ;

       array [ 0 ] = 1 ;
       array [ 1 ] = 2 ;
       array [ 2 ] = 3 ;
       array [ 3 ] = 4 ;
       array [ 4 ] = 5 ;

       printf ( " Enter the location where you wish to insert an element " ) ;
       position = 6 ;

       printf ( " Enter the value to insert " ) ;
       value = 1000 ;

        for ( c = n - 1 ; c >= position - 1 ; c -- )
          array [ c + 1 ] = array [ c ] ;

       array [ position - 1 ] = value ;

       printf ( " Resultant array is " ) ;

       for ( d = 0 ; d <= n ; d ++ )
          printf ( " %d " , array [ d ] ) ;

       return 0 ;
    }
    ''' )

    return a

################################################################################
################################################################################
"""
                         C_program_code_demonstration
                                                                             """
#start
CInterperter.Runinterpreter(BubbleSort())
clear()
CInterperter.Runinterpreter(FindGreatestNumber())
clear()
CInterperter.Runinterpreter(CheckLeapYear())
clear()
CInterperter.Runinterpreter(ProgramToInsertAnElementInAnArray())
clear()
end()