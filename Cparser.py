DEBUG=True # on/off the debugger
def dprint(args, kwargs):
    if DEBUG==True:
        print (args,kwargs)
############################        "files imported"
from Tokenizer import *
import CExpression
import CKeyword
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


a=parsex(''' #define Strtwo 100 + 200 +
                # define Str for ( x = 0 ; x
                #define Strthree \
                \
                \
                2 + 3 +
              Str = 5 ; x ++ ) x + y = z ; ''')

print(a)
