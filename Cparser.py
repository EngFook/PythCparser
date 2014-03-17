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


def refreshSymbolTable():
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
    refreshSymbolTable()
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

a=parse('''typedef struct {
                        int a ;
                        int b ;
                                } Data ;''')
print ( a)
a[0].interpreter()


