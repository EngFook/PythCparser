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
import CParser
import CInterperter
## "First Run. "                                                              ##
FirstRun=CParser.oneTimeParse('''
int main ( )
{   char Type_Any_Word_To_Continue ;
    char name ;
    printf ( " Hello! , welcome to use our PythCparser . What is your name ? " ) ;
    scanf ( " %s " , & name ) ;
    printf ( " Hi %s , thank you for viewing our program. \n We are going to show you more Clanguage program interpret by our PythCparser " , name ) ;
    scanf ( " %s " , Type_Any_Word_To_Continue  ) ;
}
''')
CInterperter.Runinterpreter(FirstRun)
################################################################################
#C-program code demonstration:
################################################################################
def  BubbleSort():
    a=CParser.oneTimeParse('''
                    printf ( " This is BubbleSort. " ) ;
                    void BubbleSort ( int [ ] , int ) ;
                    int main ( )
                    {
                        int a [ 5 ] , n , c , d , swap , i ;
                        printf ( " Please input the value into each array for sorting " ) ;
                        for ( i = 0 ; i < 5 ; i ++ )
                        {
                            scanf ( " %d " , a [ i ] ) ;
                        }
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

##def FindGreatestNumber():
##    a=CParser.oneTimeParse("""
##    int main ( )
##    {   float a , b , c ;
##          printf ( " Enter three numbers : " ) ;
##          scanf ( " %d %d %d " , & a , & b , & c ) ;
##          if ( a >= b && a >= c )
##            printf ( " Largest number = %.5f " , a ) ;
##          if ( b >= a && b >= c )
##             printf ( " Largest number = %.5f " , b ) ;
##          if ( c >= a && c >= b )
##             printf ( " Largest number = %.5f " , c ) ;
##          return 0 ;
##    }
##    """)
##    return a
##
##
##
##def CheckLeapYear():
##    a=CParser.oneTimeParse("""
##    int main ( )
##    {
##          int year ;
##           printf ( " Enter a year: " ) ;
##           scanf ( " %d " , & year ) ;
##          if ( year % 4 == 0 )
##          {
##              if ( year % 100 == 0 )
##              {
##                  if ( year % 400 == 0 )
##                     printf ( " %d is a leap year. " , year ) ;
##                  else
##                     printf ( " %d is not a leap year. " , year ) ;
##              }
##              else
##                 printf ( " %d is a leap year. " , year ) ;
##          }
##          else
##             printf ( " %d is not a leap year. " , year ) ;
##          return 0 ;
##    }
##    """ )
##    return a
##

##    #C program to insert an element in an array
##    d=parse(""" int main ( )
##    {
##       int array [ 100 ] , position , c , n , value , d ;
##
##       printf ( " Enter number of elements in array " ) ;
##       scanf ( " %d " , & n ) ;
##
##       printf ( " Enter %d elements " , n ) ;
##
##       for ( c = 0 ; c < n ; c ++ )
##          scanf ( " %d " , array [ c ] ) ;
##
##       printf ( " Enter the location where you wish to insert an element " ) ;
##       scanf ( " %d " , & position ) ;
##
##       printf ( " Enter the value to insert " ) ;
##       scanf ( " %d " , & value ) ;
##
##        for ( c = n - 1 ; c >= position - 1 ; c -- )
##          array [ c + 1 ] = array [ c ] ;
##
##       array [ position - 1 ] = value ;
##
##       printf ( " Resultant array is " ) ;
##
##       for ( d = 0 ; d <= n ; d ++ )
##          printf ( " %d " , array [ d ] ) ;
##
##       return 0 ;
##    } """ )
##
##    CInterperter.Runinterpreter(d)
##
##    #check even or odd
##    e=parse(""" int main ( )
##    {
##       int n ;
##
##       printf ( " Enter an integer " ) ;
##       scanf ( " %d " , & n ) ;
##
##       if ( n % 2 == 0 )
##          printf ( " Even " ) ;
##       else
##          printf ( " Odd " ) ;
##
##       return 0 ;
##    } """ )
##
##    CInterperter.Runinterpreter(e)
##
##    f=parse(""" int main ( )
##    {
##       int number , sum = 0 , temp , remainder ;
##
##       printf ( " Enter an integer " ) ;
##       scanf ( " %d " , & number ) ;
##
##       temp = number ;
##
##       while ( temp != 0 )
##       {
##          remainder = temp % 10 ;
##          sum = sum + remainder * remainder * remainder ;
##          temp = temp / 10 ;
##       }
##
##       if ( number == sum )
##          printf ( " Entered number is an armstrong number. " ) ;
##       else
##          printf ( " Entered number is not an armstrong number.  " ) ;
##
##       return 0 ;
##    } """ )
##
##    CInterperter.Runinterpreter(f)
##
##    g=parse(""" #define MAX 20
##                int main ( ) {
##                int a  = 0 ;
##                for ( a = 0 ; a <= MAX ; a ++ )
##                    printf ( " %d " , a ) ;
##
##                } """ )
##    CInterperter.Runinterpreter(g)
##
##
##    #C programming code for binary search
##    h=oneTimeParse(""" int main ( )
##    {
##       int c , first , last , middle , n , search , array [ 100 ] ;
##
##       printf ( " Enter number of elements " ) ;
##       scanf ( " %d " , & n ) ;
##
##       printf ( " Enter %d integers " , & n ) ;
##
##       for ( c = 0 ; c < n ; c ++ )
##          scanf ( " %d " , array [ c ] ) ;
##
##       printf ( " Enter value to find " ) ;
##       scanf ( " %d " , & search ) ;
##
##       first = 0 ;
##       last = n - 1 ;
##       middle = ( first + last ) / 2 ;
##
##       while ( first <= last )
##       {
##          if ( array [ middle ] < search )
##             first = middle + 1 ;
##          else if ( array [ middle ] == search )
##          {
##             printf ( " %d found at location %d . " , search , middle + 1 ) ;
##             break ;
##          }
##          else
##             last = middle - 1 ;
##
##          middle = ( first + last ) / 2 ;
##       }
##       if ( first > last )
##          printf ( " %d Not found! is not present in the list. " , search ) ;
##
##       return 0 ;
##    } """ )
##
##    CInterperter.Runinterpreter(h)

################################################################################
################################################################################
"""
                         C_program_code_demonstration
                                                                            """

CInterperter.Runinterpreter(BubbleSort())
##CInterperter.Runinterpreter(FindGreatestNumber())
##CInterperter.Runinterpreter(CheckLeapYear())