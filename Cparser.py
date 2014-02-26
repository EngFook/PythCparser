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

a=parse('''int func ( int x , int y )
            {
                x = a ;
                y = b ;
                return a + b ;
            } ''')

print(a)
##print("break 1 :",a.second.first[1].second.first[1].braces)
##print("break 2 :",a.second.first[2].braces)