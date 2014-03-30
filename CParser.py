#-------------------------------------------------------------------------------
# Name:        PythCparser
# Purpose:     To parse and interpret C language by using Python.
#
# Author:      Goh Eng Fook
#              Lim Bing Ran
#
# Created:     07/03/2013
# Copyright:   (c) 2013-2014, Goh Eng Fook & Lim Bing Ran
# Licence:     GPLv3
#-------------------------------------------------------------------------------
##"On/Off the debugger."                                                      ##
DEBUG=True
def dprint(args, kwargs):
    if DEBUG==True:
        print (args,kwargs)
##"Files imported."                                                           ##
from Tokenizer import *
import CInterperter
import CExpression
import CKeyword
import CScope
##"Injection from Ckeyword and Cexpression."                                  ##
CKeyword.configure_C_Keyword(CExpression)
CExpression.configure_C_Expression(CKeyword)
##"Global Tokenizer."                                                         ##
global tokenizer



##"Refresh the SymbolTable when user defined."                                ##
def clearParseEnviroment():
    temp1=[]
    for temp in symbolTable:
        if hasattr(symbolTable[temp],'attribute'):
            temp1.append(temp)
    temp=0
    while temp < temp1.__len__():
        symbolTable.pop(temp1[temp])
        temp=temp+1
##"Parse the string to analyse."                                              ##
def parse(str):
    array=[]
    CKeyword.defineTable={}
    CKeyword.stringTable={}
    tokenizer=Tokenizer(str)
    token=tokenizer.peepahead()
    CExpression.configure_tokenizer_Expression(tokenizer)
    CKeyword.configure_tokenizer_Keyword(tokenizer)
    while(token.first == ';'):
        tokenizer.advance()
        token=tokenizer.peepahead()
    while(token.first != '(end)'):
        if hasattr(token,'std'):
            temp=CKeyword.parseStatement()
        else:
            temp=CExpression.expression(0)
            tokenizer.advance(';')
        token=tokenizer.peepahead()
        array.append(temp)
    return array

def oneTimeParse(str):
        temp=parse(str)
        clearParseEnviroment()
        return temp

def Parse(str):
    return parse(str)

def Initialization():
    a=""" void printf (  ) ;
          void printf (  )
          {
          }"""
    root=Parse(a)
    CInterperter.Runinterpreter(root)

Initialization()

def Initializationscan():
    a=""" void scanf (  ) ;
          void scanf (  )
          {
          }"""
    root=Parse(a)
    CInterperter.Runinterpreter(root)

Initializationscan()


################################################################################
################################################################################
"""
                            Manual Test here.
                                                                             """

### Bubble sort
##a=Parsea=Parse("""int main ( )
##                {
##                    int a [ 5 ] , n , c , d , swap , i ;
##                    for ( i = 0 ; i < 5 ; i ++ )
##                    {
##                        scanf ( " %d " , a [ i ] ) ;
##                    }
##                    n = 5 ;
##                    printf ( " before: " ) ;
##                    for ( d = 0 ; d < n ; d ++ )
##                    {
##                        printf ( " %d " , a [ d ] ) ;
##                    }
##                    for ( c = 0 ; c < ( n - 1 ) ; c ++ )
##                    {
##                        for ( d = 0 ; d < n - c - 1 ; d ++ )
##                        {
##                            if ( a [ d ] > a [ d + 1 ] )
##                            {
##                                swap = a [ d ] ;
##                                a [ d ] = a [ d + 1 ] ;
##                                a [ d + 1 ] = swap ;
##                            }
##                        }
##                    }
##                    printf ( " after: " ) ;
##                    for ( d = 0 ; d < n ; d ++ )
##                    {
##                        printf ( " %d " , a [ d ] ) ;
##                    }
##                } """)
##
##CInterperter.Runinterpreter(a)


###find the greatest number
##a=Parse("""
##
##
##int main ( ) {   float a , b , c ;
##      printf ( " Enter three numbers : " ) ;
##      scanf ( " %d %d %d " , & a , & b , & c ) ;
##      if ( a >= b && a >= c )
##        printf ( " Largest number = %.5f " , a ) ;
##      if ( b >= a && b >= c )
##         printf ( " Largest number = %.5f " , b ) ;
##      if ( c >= a && c >= b )
##         printf ( " Largest number = %.5f " , c ) ;
##      return 0 ;  }                                           """)
##
##
##
##CInterperter.Runinterpreter(a)

###check leap year
##c=Parse(""" int main ( )
##{
##      int year ;
##       printf ( " Enter a year: " ) ;
##       scanf ( " %d " , year ) ;
##      if ( year % 4 == 0 )
##      {
##          if ( year % 100 == 0 )
##          {
##              if ( year % 400 == 0 )
##                 printf ( " %d is a leap year. " , year ) ;
##              else
##                 printf ( " %d is not a leap year. " , year ) ;
##          }
##          else
##             printf ( " %d is a leap year. " , year ) ;
##      }
##      else
##         printf ( " %d is not a leap year. " , year ) ;
##      return 0 ;  }                       """ )
##
##CInterperter.Runinterpreter(c)

###C program to insert an element in an array
##d=parse(""" int main ( )
##{
##   int array [ 100 ] , position , c , n , value , d ;
##
##   printf ( " Enter number of elements in array " ) ;
##   scanf ( " %d " ,  n ) ;
##
##   printf ( " Enter %d elements " , n ) ;
##
##   for ( c = 0 ; c < n ; c ++ )
##      scanf ( " %d " , array [ c ] ) ;
##
##   printf ( " Enter the location where you wish to insert an element " ) ;
##   scanf ( " %d " , position ) ;
##
##   printf ( " Enter the value to insert " ) ;
##   scanf ( " %d " , value ) ;
##
##    for ( c = n - 1 ; c >= position - 1 ; c -- )
##      array [ c + 1 ] = array [ c ] ;
##
##   array [ position - 1 ] = value ;
##
##   printf ( " Resultant array is " ) ;
##
##   for ( d = 0 ; d <= n ; d ++ )
##      printf ( " %d " , array [ d ] ) ;
##
##   return 0 ;
##} """ )
##
##CInterperter.Runinterpreter(d)

###check even or odd
##e=parse(""" int main ( )
##{
##   int n ;
##
##   printf ( " Enter an integer " ) ;
##   scanf ( " %d " , & n ) ;
##
##   if ( n % 2 == 0 )
##      printf ( " Even " ) ;
##   else
##      printf ( " Odd " ) ;
##
##   return 0 ;
##} """ )
##
##CInterperter.Runinterpreter(e)

f=parse(""" int main ( )
{
   int number , sum = 0 , temp , remainder ;

   printf ( " Enter an integer " ) ;
   scanf ( " %d " ,  number ) ;

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
} """ )

CInterperter.Runinterpreter(f)