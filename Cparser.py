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

##def intepreter(token):
##    if(token.id != '(literal)' and token.id != '(identifier)' ):
##        intepreter(token.first)
##        if(token.id == '*'):
##            print('a pointer to')
##        elif(token.arity=='special'):
##            print(token.id)
##        elif(token.arity=="postunary"):
##            if(token.id == '['):
##                print("array ",token.second," at")
##            else:
##                print("function which take in ",token.second)
##    else:
##        print(token.first," is")


a=parse(''' #define max for (
        {
        max x = 5 ; x > 0 ; x ++ ) ;
        } }''')
print(a)