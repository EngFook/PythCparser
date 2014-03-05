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
array=[]
newarray=[]
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

def parsex(str):
    passtheexpression=False
    tokenizer=Tokenizer(str)
    token=tokenizer.peepahead()
    token=tokenizer.peepahead()
    CExpression.configure_tokenizer_Expression(tokenizer)
    CKeyword.configure_tokenizer_Keyword(tokenizer)
    store=token
    while(token.first == ';'):
        tokenizer.advance()
        token=tokenizer.peepahead()
    while(store.first != '(end)'):
        if hasattr(token,'std') and passtheexpression == False:
            temp=CKeyword.parseStatement()
        else:
            temp=CExpression.expression(0)
            tokenizer.advance(';')
        store=tokenizer.peepahead()
        array.append(temp)
        CKeyword.configure_array(array)
        if hasattr(store,'std'):
            passtheexpression=False
        else:
            passtheexpression=True
    newarray.clear()
    for i in array:
        newarray.append(i)
    array.clear()
    CKeyword.defineTable={}
    return newarray


a=parsex('''{
                int a = 1 ;
                int b = 2 ;
                {
                    int a = 3 ;
                    int b = 4 ;
                    {
                        int a = 5 ;
                        int b = 6 ;
                    }
                }
            }''')

##print(a)

