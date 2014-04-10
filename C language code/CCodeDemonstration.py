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
    a=oneTimeParse('''
                    printf ( " 1st C program is BubbleSort. " ) ;
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

def FindGreatestNumber():
    a=oneTimeParse('''
    int main ( )
    {   float a , b , c ;
          printf ( " 2nd C program is to find "Greatest Number". " ) ;
          printf ( " Please enter three numbers : " ) ;
          scanf ( " %d %d %d " , & a , & b , & c ) ;
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
          scanf ( " %d " , & year ) ;
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
       scanf ( " %d " , & n ) ;

       printf ( " Enter %d elements " , n ) ;

       for ( c = 0 ; c < n ; c ++ )
          scanf ( " %d " , array [ c ] ) ;

       printf ( " Enter the location where you wish to insert an element " ) ;
       scanf ( " %d " , & position ) ;

       printf ( " Enter the value to insert " ) ;
       scanf ( " %d " , & value ) ;

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

def CheckEvenOdd():
    a=parse('''
    #define number 2
    int main ( )
    {
       int n ;
       printf ( " 5th C program is to check even or odd. " ) ;
       printf ( " Enter an integer " ) ;
       scanf ( " %d " , & n ) ;

       if ( n % number == 0 )
          printf ( " Even " ) ;
       else
          printf ( " %d is Odd " , n ) ;

       return 0 ;
    }
    ''' )
    return a

# ------------------------------------------------------------------------------
# This program computes all Armstrong numbers in the range of
# 0 and 999.  An Armstrong number is a number such that the sum
# of its digits raised to the third power is equal to the number
# itself.  For example, 371 is an Armstrong number, since
# 3**3 + 7**3 + 1**3 = 371.
# ------------------------------------------------------------------------------
def CheckArmstrongNumber():
    a=parse('''
    int main ( )
    {
       int number , sum = 0 , temp , remainder ;
       printf ( " 6th C program is to check Armstrong Number. " ) ;
       printf ( " Enter an integer " ) ;
       scanf ( " %d " , & number ) ;

       temp = number ;

       while ( temp != 0 )
       {
          remainder = temp % 10 ;
          sum = sum + remainder * remainder * remainder ;
          temp = temp / 10 ;
       }

       if ( number == sum )
          printf ( " Entered number is an armstrong number. " ) ;
       else
          printf ( " Entered number is not an armstrong number.  " ) ;

       return 0 ;
    }
    ''' )
    return a

def BinarySearch():
    a=oneTimeParse('''
    int main ( )
    {
       int c , first , last , middle , n , search , array [ 100 ] ;

       printf ( " 7th C program is binary search. " ) ;
       printf ( " Enter number of elements " ) ;
       scanf ( " %d " , & n ) ;

       printf ( " Enter %d integers " , & n ) ;

       for ( c = 0 ; c < n ; c ++ )
          scanf ( " %d " , array [ c ] ) ;

       printf ( " Enter value to find " ) ;
       scanf ( " %d " , & search ) ;

       first = 0 ;
       last = n - 1 ;
       middle = ( first + last ) / 2 ;

       while ( first <= last )
       {
          if ( array [ middle ] < search )
             first = middle + 1 ;
          else if ( array [ middle ] == search )
          {
             printf ( " %d found at location %d . " , search , middle + 1 ) ;
             break ;
          }
          else
             last = middle - 1 ;

          middle = ( first + last ) / 2 ;
       }
       if ( first > last )
          printf ( " %d Not found! is not present in the list. " , search ) ;

       return 0 ;
    }
    ''' )
    return a

def SwitchCaseCheckResultGrade():
    a=oneTimeParse('''
    int main ( )
                        {
                            int Marks , choice ;
                            printf ( " 8th C program is to Check Result Grade. " ) ;
                            printf ( " Please enter your marks. " ) ;
                            scanf ( " %d " , & Marks ) ;

                            if ( Marks  > 90 && Marks  <= 100 ) choice = 1 ;
                            else if ( Marks  > 70 && Marks  <= 90 ) choice = 2 ;
                            else if ( Marks  > 50 && Marks  <= 70 ) choice = 3 ;
                            else if ( Marks  > 30 && Marks  <= 50 ) choice = 4 ;
                            else if ( Marks  > 0  && Marks  <= 30 ) choice = 5 ;
                            printf ( " Your marks : %d " , Marks ) ;
                             switch ( choice )
                             {
                                case 1 : printf ( " Get A! Excellent ! " ) ;
                                case 2 : printf ( " Get B, Good " ) ;
                                case 3 : printf ( " Get C.. OK ~ " ) ;
                                case 4 : printf ( " Just a D.. Mmmmm....  Study harder please. " ) ;
                                case 5 : printf ( " ByeBye... " ) ;
                                default    :  printf ( " What is your marks anyway? " ) ;
                             }
                        }
    ''')
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
CInterperter.Runinterpreter(CheckEvenOdd())
clear()
CInterperter.Runinterpreter(CheckArmstrongNumber())
clear()
CInterperter.Runinterpreter(BinarySearch())
clear()
CInterperter.Runinterpreter(SwitchCaseCheckResultGrade())
end()