##"Files imported."                                                           ##
from Symbol import *
from Tokenizer import *
##"Initialization."                                                           ##
Keyword=0
tokenizer=0
##"Injection keyword from Cparser."                                           ##
def configure_C_Expression(module):
    global Keyword
    Keyword=module
##"Injection tokenizer from Cparser."                                         ##
def configure_tokenizer_Expression(module):
    global tokenizer
    tokenizer=module
##"For return self value purpose."                                            ##
def nud(self,token):
    self.first=temp.nud()
    return self
##"Print style."                                                              ##
def REPR(self):
    if self.arity == 'binary':
        return '({0} {1} {2})'.format(self.first,self.id, self.second)
    else:
        return '({0} {1})'.format(self.id, self.first)
##"Id categorized to infix.For e.g '+' for '2 + 3' , '-' for '10 - 5'         ##
def infix(id, bindingPower,Type=True):
    sym=symbol(id)
    sym.left=Type
    sym.first=None
    sym.second=None
    sym.arity='binary'
    sym.leftBindingPower=bindingPower
    return sym
##"Id categorized to prefix.For e.g '+' for '+2' , '-' for '-5'               ##
def prefix(id, bindingPower):
    sym=symbol(id)
    sym.first=None
    sym.arity='unary'
    sym.leftBindingPower=bindingPower
    return sym
##"Expression to perform every specific expression function."                 ##
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
##"The entire different type of function along CExpression."                  ##
def CexpressionGrammar():
################################################################################
# 1st function
################################################################################
            def REPR(self): #for print number or symbol instead of address
                if(self.arity=='unary'):
                    return '({0} {1})'.format(self.id ,self.first)
                elif(self.arity=='binary'):
                    if self.second==None:
                        return '({0} {1})'.format(self.id,self.first)
                    return '({0} {1} {2})'.format(self.first,self.id, self.second)

            def led(self,leftToken):
                if hasattr(leftToken,'limitedExpression'):
                    token=None
                    leftToken=expression(self.leftBindingPower)
                else:
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
            sym.__repr__=REPR
            sym.led=led
            sym.nud=nud

            sym=infix('&',40)
            sym.__repr__=REPR
            sym.led=led
            sym.nud=nud

            sym=infix('|',40)
            sym.__repr__=REPR
            sym.led=led

            sym=infix('^',40)
            sym.__repr__=REPR
            sym.led=led

            sym=infix('-',40)
            sym.__repr__=REPR
            sym.led=led
            sym.nud=nud

            sym=infix('/',60)
            sym.led=led
            sym.__repr__=REPR

            sym=infix('%',60)
            sym.led=led
            sym.__repr__=REPR

            sym=infix('*',60)
            sym.led=led
            sym.nud=nud
            sym.__repr__=REPR
################################################################################
# 2nd function
################################################################################
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
################################################################################
# 3rd function
################################################################################
            def REPR(self):
                if(self.arity=='postunary'):
                    return '({0}{1})'.format(self.first,self.id )
                else:
                    return '({0} {1})'.format(self.id ,self.first)

            def led (self,leftToken):
                raise SyntaxError('{0} should come before a word.Invalid Logic'.format(self.first))

            sym=prefix('!',90)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led
            sym=prefix('~',90)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led
################################################################################
# 4th function
################################################################################
            def nud(self):
                raise SyntaxError('{0} should come after a word.Invalid Logic'.format(self.first))

            def led(self,leftToken):
                token=tokenizer.advance()
                if tokenizer.peepahead().id=='{':
                    self.first=leftToken
                    token=tokenizer.advance()
                    self.second=token.std(leftToken)
                    return self
                token=expression(self.leftBindingPower-1)
                self.first=leftToken
                self.second=token
                return self

            def REPR(self):
                if self.arity == 'unary' :
                    return '({0} {1})'.format(self.id ,self.first)
                elif self.arity == 'binary':
                    return '({0} {1} {2})'.format(self.first,self.id, self.second)

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
            sym=infix('+=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('-=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('*=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('/=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('%=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('~=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('!=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('<<=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('>>=',10)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('<',12)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('>',12)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('<=',12)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('>=',12)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('<<',15)
            sym.__repr__=REPR
            sym.led=led
            sym=infix('>>',15)
            sym.__repr__=REPR
            sym.led=led
################################################################################
# 5th function
################################################################################
            def REPR(self): #for print number or symbol instead of address
                if self.arity == 'unary' :
                    return '({0} {1})'.format(self.id ,self.first)
                elif self.arity == 'binary':
                    if self.second==None:
                        return '({0}{1})'.format(self.id ,self.first)
                    return '({0} {1} {2})'.format(self.first,self.id, self.second)

            def led(self,leftToken):
                if(leftToken.id == '(identifier)'):
                    tokenizer.advance()
                    token=expression(self.leftBindingPower)
                    self.first=leftToken
                    self.second=token
                    return self
                else:
                    raise SyntaxError("Input should be identifier!")
            sym=infix('.',80)
            sym.__repr__=REPR
            sym.arity='unary'
            sym.led=led
            sym=infix('->',80)
            sym.__repr__=REPR
            sym.led=led
################################################################################
# 6th function
################################################################################
            def REPR(self): #for print number or symbol instead of address
                if hasattr(self,'third'):
                    if self.third !=None:
                        return '({0} {1} {2} )'.format(self.first,self.second,self.third)
                    elif self.second == None and self.third == None:
                        return '( {0} )'.format(self.first)
                    elif self.second == None:
                        return '({0} {1})'.format(self.first,self.second)
                    else:
                        '({0})'.format(self.first)
                    if(self.arity=='grouping'):
                        return '{0} {1} '.format(self.id,self.first)
                    else:
                        return '({0}) ({1})'.format(self.first,self.second)

            def nud(self):
                self.arity='grouping'
                token=expression(0)
                self.second=None
                self.first=token
                tokenizer.advance()
                self.CheckFunctionType=False
                return self
            global functiondeclare
            functiondeclare=False
            def led(self,leftToken):
                global functiondeclare
                if leftToken.arity == 'binary':
                    raise SyntaxError('Should not enter "{0}" '.format(self.id))
                self.arity='function'
                tokenizer.advance()
                temp=[]
                comma=False
                check=tokenizer.peepahead()
                while(check.id != ')'):
                    if hasattr(tokenizer.peepahead(),'std'):
                        functiondeclare=True
                        token=Keyword.parseStatement()
                        functiondeclare=False
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

            sym=infix('(',50)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led
            sym.third=None
            sym.CheckFunctionType=True
################################################################################
# 7th function
################################################################################
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

                    return '{0}{1}]'.format(self.id,self.first)
                else:
                    return '({0} [{1}] )'.format(self.first,self.second)

            sym=infix('[',50)
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
################################################################################
# 8th function
################################################################################
            def nud(self):
                self.first=expression(0)
                tokenizer.advance("'")
                return self.first

            def REPR(self):
                return '{0} {1} {2}'.format(self.id,self.first,self.id)

            sym=infix("'",0)
            sym.__repr__=REPR
            sym.nud=nud
            sym.led=led

            def nud(self):
                pass
################################################################################
################################################################################
##"Call C expressionGrammar."                                                 ##
CexpressionGrammar()
##                                                                            ##