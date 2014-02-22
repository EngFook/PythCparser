##########################       "files imported"
from Symbol import *
from Tokenizer import *
##########################
Keyword=0
tokenizer=0
def configure_C_Expression(module):
    global Keyword
    Keyword=module
def configure_tokenizer_Expression(module):
    global tokenizer
    tokenizer=module
##########################
def nud(self,token):
    self.first=temp.nud()
    return self

def REPR(self): #for print number or symbol instead of address
    return '({0} {1} {2})'.format(self.first,self.id, self.second)

def infix(id, bindingPower,Type=True):
    sym=symbol(id)
    sym.left=Type
    sym.first=None
    sym.second=None
    sym.arity='binary'
    sym.leftBindingPower=bindingPower
    sym.__repr__=REPR
    return sym

def REPR(self):
    return '({0} {1})'.format(self.id ,self.first)

def prefix(id, bindingPower):
    sym=symbol(id)
    sym.first=None
    sym.arity='unary'
    sym.leftBindingPower=bindingPower
    sym.__repr__=REPR
    return sym

def expression(rightBindingPower):
    global tokenizer
    token=tokenizer.advance()
    temp=token.nud()
    token=tokenizer.peepahead()
    while(rightBindingPower<token.leftBindingPower):
            token=token.led(temp)
            temp=token
            token=tokenizer.peepahead()
    return temp
################################################################################
def CexpressionGrammar():

            def REPR(self): #for print number or symbol instead of address
                if(self.arity=='unary'):
                    return '({0} {1})'.format(self.id ,self.first)
                elif(self.arity=='binary'):
                    return '({0} {1} {2})'.format(self.first,self.id, self.second)

            def led(self,leftToken):
                token=tokenizer.advance()
                token=expression(self.leftBindingPower)
                self.first=leftToken
                self.second=token
                return self

            def nud(self):
                self.leftBindingPower=95
                self.arity='unary'
                token=expression(self.leftBindingPower)
                self.first=token
                return self

            sym=infix('+',40)
            sym.led=led
            sym.nud=nud
            sym.__repr__=REPR
            sym=infix('-',40)
            sym.led=led
            sym.nud=nud
            sym.__repr__=REPR
            sym=infix('/',60)
            sym.led=led
            sym.__repr__=REPR
            sym=infix('*',60)
            sym.led=led
            sym.nud=nud
            sym.__repr__=REPR

            def REPR(self):
                if(self.arity=='postunary'):
                    return '({0}{1})'.format(self.first,self.id )
                else:
                    return '({0} {1})'.format(self.id ,self.first)

            def led(self,leftToken):
                self.arity='postunary'
                temp=tokenizer.peep()
                self.first=temp
                tokenizer.advance()
                return self

            sym=prefix('--',90)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led
            sym=prefix('++',90)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led

            def REPR(self): #for print number or symbol instead of address
                if(self.arity=='unary'):
                    return '({0} {1})'.format(self.id ,self.first)
                elif(self.arity=='binary'):
                    return '({0} {1} {2})'.format(self.first,self.id, self.second)

            def nud(self):
                raise SyntaxError('{0} should come after a word.Invalid Logic'.format(self.first))

            def led(self,leftToken):
                token=tokenizer.advance()
                token=expression(self.leftBindingPower-1)
                self.first=leftToken
                self.second=token
                return self

            sym=infix('**',70)
            sym.led=led
            sym.__repr__=REPR
            sym=infix('==',10)
            sym.led=led
            sym.__repr__=REPR
            sym=infix('=',10)
            sym.led=led
            sym.__repr__=REPR
            sym.nud=led
            sym=infix('=+',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('=-',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('=*',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('=/',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('=%',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('=~',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('=!',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('=<<',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('=>>',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('<',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('>',10)
            sym.__repr__=REPR
            sym.led=led

            def led(self,leftToken):
                if(leftToken.id == '(identifier)'):
                    tokenizer.advance()
                    token=expression(self.leftBindingPower)
                    self.first=leftToken
                    self.second=token
                    return self
                else:
                    raise SyntaxError("Input should be identifier!")
            sym=infix('.',40)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('->',40)
            sym.__repr__=REPR
            sym.led=led


            def REPR(self): #for print number or symbol instead of address
                if hasattr(self,'third') and hasattr(self,'third'):
                    return '({0})'.format(self.first)
                if hasattr(self,'third'):
                    return '({0}) ({1}) {2}'.format(self.first,self.second,self.third)
                if(self.arity=='grouping'):
                    return '{0} {1}'.format(self.id,self.first)
                else:
                    return '({0}) ({1})'.format(self.first,self.second)

            def nud(self):
                self.arity='grouping'
                token=expression(0)
                self.first=token
                tokenizer.advance()
                self.CheckFunctionType=False
                return self

            def led(self,leftToken):
                self.arity='postunary'
                tokenizer.advance()
                temp=[]
                comma=False
                check=tokenizer.peepahead()
                while(check.id != ')'):
                    if hasattr(tokenizer.peepahead(),'std'):
                        token=Keyword.parseStatement()
                    else:
                        token=expression(0)
                    if tokenizer.peepahead().first == ',':
                        comma=True
                    temp.append(token)
                    check=tokenizer.advance()
                self.first=leftToken
                if(comma):
                    self.second=temp
                else:
                    self.second=token
                if hasattr(leftToken,'CheckFunctionType'):
                    if leftToken.CheckFunctionType :
                        raise SyntaxError('Should not enter "{0}" '.format(leftToken.id))
                check =tokenizer.peepahead()
                if hasattr(check,'std'):
                    if self.second != None :
                        self.third=Keyword.parseStatement()
                return self

            sym=infix('(',100)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led
            sym.third=None
            sym.CheckFunctionType=True

            def led(self,leftToken):
                self.arity='postunary'
                tokenizer.advance()
                temp=[]
                comma=False
                check=tokenizer.peepahead()
                while(check.id != ']'):
                    if hasattr(tokenizer.peepahead(),'std'):
                        token=Keyword.parseStatement()
                    else:
                        token=expression(0)
                    if tokenizer.peepahead().first == ',':
                        comma=True
                    temp.append(token)
                    check=tokenizer.advance()
                self.first=leftToken
                if(comma):
                    self.second=temp
                else:
                    self.second=token
                return self

            def REPR(self): #for print number or symbol instead of address
                if(self.arity=='grouping'):
                    return '{0} {1}'.format(self.id,self.first)
                else:
                    return '({0} [{1}] )'.format(self.first,self.second)

            sym=infix('[',100)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led

            def REPR(self):
                return '{0}'.format(self.id)

            sym=infix(')',0)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led
            sym=infix('}',0)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led
            sym=infix(']',0)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led

##            '''def led(self,leftToken=None):
##                self.arity='postunary'
##                sym=symbol(self.id)
##                sym.__repr__=REPR
##                temp=[]
##                temp1=sym()
##                temp1.id=None
##                while(temp1.id != '*/'):
##                    temp1=tokenizer.advance()
##                    if(temp1.id == '(identifier)' or temp1.id == '(literal)'):
##                        temp.append(temp1.first)
##                    else:
##                        temp.append(temp1.id)
##               	temp.remove(temp1.id)
##                temp=''.join(temp)
##                self.first=temp
##                return self
##            sym=infix('/*',100)
##            sym.__repr__=REPR
##            sym.nud=led
##            sym.led=led
##            sym=infix('*/',0)
##            sym.__repr__=REPR
##            sym.nud=led
##            sym.led=led
##
##            def led(self,leftToken=None):   # same as above.
##                self.arity='unary'
##                sym=symbol(self.id)
##                sym.__repr__=REPR
##                temp=[]
##                temp1=sym()
##                while(temp1.first != '(end)'):
##                    temp1=tokenizer.advance()
##                    if(temp1.id == '(identifier)' or temp1.id == '(literal)'):
##                        temp.append(temp1.first)
##                    else:
##                        temp.append(temp1.id)
##               	temp.remove(temp1.id)
##                temp=''.join(temp)
##                self.first=temp
##                return self
##            sym=infix('#',100)
##            sym.__repr__=REPR
##            sym.nud=led
##            sym.led=led'''

################################################################################
CexpressionGrammar() # call C expressionGrammar
