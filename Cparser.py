DEBUG=True # on/off the debugger
def dprint(args, kwargs):
    if DEBUG==True:
        print (args,kwargs)
############################        "files imported"
from Tokenizer import *
import CInterperter
import CExpression
import CKeyword
import CScope
############################
############################
CKeyword.configure_C_Keyword(CExpression)
CExpression.configure_C_Expression(CKeyword)
############################

global tokenizer
def parse(str):
    tokenizer=Tokenizer(str)
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


a=parsex("""int a , b , c ;""")
a[0].interpreter()
print(a)

