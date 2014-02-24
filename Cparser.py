DEBUG=True # on/off the debugger
def dprint(args, kwargs):
    if DEBUG==True:
        print (args,kwargs)
############################        "files imported"
from Tokenizer import *
import CExpression
import CKeyword
array=[]
############################
############################
CKeyword.configure_C_Keyword(CExpression)
CExpression.configure_C_Expression(CKeyword)
############################

global tokenizer
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

##def parsex(str):
##    tokenizer=Tokenizer(str)
##    token=tokenizer.peepahead()
##    CExpression.configure_tokenizer_Expression(tokenizer)
##    CKeyword.configure_tokenizer_Keyword(tokenizer)
##    store=token
##    while(token.first == ';'):
##        tokenizer.advance()
##        token=tokenizer.peepahead()
##    while(store.first != '(end)'):
##        if hasattr(token,'std'):
##            temp=CKeyword.parseStatement()
##            tokenizer.advance(';')
##
##        else:
##            temp=CExpression.expression(0)
##            tokenizer.advance(';')
##
##        store=tokenizer.peepahead()
##        array.append(temp)
##    return array


string=parse(""" #define Str for ( x = 0
                {  Str ; x = 5 ; x ++ ) x + y = z ; }""")

print(string)
