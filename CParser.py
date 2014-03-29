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


################################################################################
################################################################################
"""
                            Manual Test here.
                                                                             """
a=Parse("""
           int a [ ] = { 1 , 3  , 4 } ; """)
print(a)
##CInterperter.Runinterpreter(a)