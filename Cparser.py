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
##"Parse the string to analyse."          'temporary'                         ##
def parse(str):
    tokenizer=Tokenizer(str)
    token=tokenizer.peepahead()
    token=tokenizer.peepahead()
    CExpression.configure_tokenizer_Expression(tokenizer)
    CKeyword.configure_tokenizer_Keyword(tokenizer)
    while(token.first == ';'):
        tokenizer.advance(';')
        token=tokenizer.peepahead()
    if token.first=='(end)':
        return
    if hasattr(token,'std'):
        temp=CKeyword.parseStatement()
    else:
        temp=CExpression.expression(0)
        tokenizer.advance(';')
    return temp
##"Parse the string to analyse."                                              ##
def parsex(str):
    array=[]
    CKeyword.defineTable={}
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
################################################################################
################################################################################
"""
    Manual Test here.
##                        """
a=parsex('''struct DataQ {
                    int a ;
                    int b ;
                            }  Data99 ;

''')

print(a)

