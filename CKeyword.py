####################################       "files imported"
from symbol import *
from Tokenizer import *
##########################
expression=0
tokenizer=0
def configure_C_Keyword(module):
    global expression
    expression=module
def configure_tokenizer_Keyword(module):
    global tokenizer
    tokenizer=module
####################################
def keyword(id):
    sym=symbol(id)
    sym.std=None
    sym.arity=None
    return sym

def parseStatement():
    global tokenizer
    token=tokenizer.advance()
    temp=token.std()
    return temp
################################################################################

def CkeywordGrammar():
            def std(self,leftToken=None):
                self.first=tokenizer.advance()
                token=self.first
                token.constantidentifier=tokenizer.advance()
                token.id="constantidentifier"
                if tokenizer.advance().first != '(end)':
                    raise SyntaxError('Cannot be define twice')
                return self

            def REPR(self):
                return '({0} {1} {2})'.format(self.id, self.first,self.first.constantidentifier)

            sym=keyword('#define')
            sym.std=std
            sym.first=None
            sym.arity='unary'
            sym.__repr__=REPR

################################################################################
## if else std -> if std
################################################################################
            def std(self):
                if tokenizer.peepahead().id != '(':
                    raise SyntaxError('Expected a condition start with a open bracket ("(") . ')
                self.first=expression.expression(0)
                if hasattr(tokenizer.peepahead(),'std'):
                    self.second=parseStatement()
                else:
                    if tokenizer.peepahead().first != ';':
                        self.second=expression.expression(0)
                    else:
                        self.second=None
                    tokenizer.advance(';')
                check=tokenizer.peepahead()
                if hasattr(check,'std'):
                    if check.id == 'else':
                        self.third=parseStatement()
                    elif check.id == 'case':
                        return self
                else:
                    self.third=None
                return self

            def REPR(self):##return '({0} {1} {2}) \n{3}'.format(self.id, self.first, self.second ,self.third)##
                if self.third == None:
                    if self.second == None:
                        return '({0} {1}'.format(self.id, self.first)
                    return '({0} {1} {2}'.format(self.id, self.first, self.second)
                if self.second == None:
                    return '({0} {1} {2})'.format(self.id, self.first,self.third)
            sym=keyword('if')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.third=None
            sym.__repr__=REPR
################################################################################
## if else std -> else std
################################################################################
            def std(self,leftToken=None):
                a=tokenizer.peep()
                if a is None:
                    raise SyntaxError ('("if") statement expected before ("else")')
                if hasattr(tokenizer.peepahead(),'std'):
                    self.first=parseStatement()
                else:
                    if tokenizer.peepahead().id == '(':
                        raise SyntaxError('Did not expected open bracket ("(") after ("else")')
                    self.first=expression.expression(0)
                    tokenizer.advance(';')
                return self

            def REPR(self):
                return '({0} {1})'.format(self.id, self.first )
            sym=keyword('else')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR
################################################################################
################################################################################
################################################################################
## Do While std -> while std
################################################################################
            def std(self,leftToken=None):
                sym=symbol(self.id)
                if tokenizer.peepahead().id != '(':
                    raise SyntaxError('Expected a open bracket ("(") after ("while") statement')
                self.first=expression.expression(0)
                if tokenizer.peepahead().first == ';' or tokenizer.peepahead().first == '(end)':
                    tokenizer.advance(';')
                    if tokenizer.peepahead().first == '(end)':
                        self.second=None
                        return self
                if hasattr(tokenizer.peepahead(),'std'):
                        self.second=parseStatement()
                else:
                        self.second=expression.expression(0)

                return self

            def REPR(self):
                if self.second==None:
                    return '({0} {1})'.format(self.id, self.first)
                return '({0} {1} {2})'.format(self.id, self.first,self.second)
            sym=keyword('while')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.__repr__=REPR
################################################################################
## do std
################################################################################
            def std(self,leftToken=None):
                sym=symbol(self.id)
                temp=tokenizer.advance()
                self.first=temp.std()
                temp=tokenizer.peepahead()
                if(tokenizer.peepahead().id == 'while'):
                    self.second=tokenizer.advance().std()
                return self

            def REPR(self):
                return '({0} {1} {2} {3} {4})'.format(self.id,'{', self.first,'}',self.second )
            sym=keyword('do')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.__repr__=REPR
################################################################################
################################################################################
################################################################################
## for std
################################################################################
            def std(self,leftToken=None):
                tokenizer.advance('(')
                check=tokenizer.peepahead()
                if hasattr(check,'std'):
                    raise SyntaxError('Did not expected to declare a type "{0}" '.format(check.id))
                else:
                    self.first=expression.expression(0)
                a=tokenizer.peepahead()
                tokenizer.advance(';')
                self.second=expression.expression(0)
                tokenizer.advance(';')
                self.third=expression.expression(0)
                tokenizer.advance(')')
                check=tokenizer.peepahead()
                if check.first !='(end)':
                    if check.first == ';':
                        sym.four=None
                        temp=self
                        return temp
                    if hasattr(check,'std'):
                        self.four=parseStatement()
                    else:
                        self.four=expression.expression(0)
                        tokenizer.advance(';')
                    temp=self
                else:
                    tokenizer.advance(';')
                    sym.four=None
                    temp=self
                return temp

            def REPR(self):
                if self.four == None :
                    self.four = ')'
                    return '({0} {1} {2} {3}{4}'.format(self.id, self.first, self.second,self.third,self.four)
                return '({0} {1} {2} {3}) \n{4}'.format(self.id, self.first, self.second ,self.third ,self.four)
            sym=keyword('for')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.third=None
            sym.four=None
            sym.__repr__=REPR
################################################################################
################################################################################
################################################################################
## Switch Case std -> switch std
################################################################################
            def std(self,leftToken=None):
                temp={}
                tokenizer.advance('(')
                self.first=expression.expression(0)
                tokenizer.advance(')')
                token=tokenizer.advance('{')
                temp=token.std()
                self.second=temp
                return self

            def REPR(self):
                return '{0} {1} {2}'.format(self.id, self.first , self.second )
            sym=keyword('switch')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.arity='binary'
            sym.__repr__=REPR
################################################################################
## case std
################################################################################
            def std(self):
                if self.id == 'case':
                    tokenizer.advance()
                    tokenizer.advance("'")
                    self.first=tokenizer.advance()
                    tokenizer.advance("'")
                    tokenizer.advance(':')
                    return self
                elif hasattr(self,'std'):
                    tokenizer.advance()
                    temp=self.std()
                    casearray.append(temp)
                return casearray

            def REPR(self):
                return '{0} {1}'.format(self.id, self.first)
            sym=keyword('case')
            sym.std=std
            sym.first=None
            sym.arity='case'
            sym.__repr__=REPR

            def std(self):
                tokenizer.advance()
                tokenizer.advance(':')
                return self

            def REPR(self):
                return '{0}'.format(self.id)
            sym=keyword('default')
            sym.std=std
            sym.arity='case'
            sym.__repr__=REPR
################################################################################
################################################################################
################################################################################
## Braces std
################################################################################
            def std(self,leftToken=None):
                array=[]
                check=tokenizer.peepahead()
                while check.id !='}':
                        if hasattr(check,'std'):
                            if( check.id == 'if'):
                                temp=parseStatement()
                            else : temp=check.std()
                        else:
                            temp=expression.expression(0)
                            tokenizer.advance(';')
                        array.append(temp)
                        check=tokenizer.peepahead()
                tokenizer.advance('}')
                check=tokenizer.peepahead()
                self.first=array
                return self

            def REPR(self):
                if self.second == None:
                    self.second = '}'
                    return '{0} {1} {2}'.format(self.id, self.first,self.second)
                return '{0} {1} {2} '.format(self.id, self.first ,self.second)

            sym=keyword('{')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.__repr__=REPR

            def REPR(self):
                return '({0} {1})'.format(self.id ,self.first)

            def std(self):
                self.first=expression.expression(90)
                return self

            sym=keyword('int')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR

            sym=keyword('double')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR


################################################################################
################################################################################
CkeywordGrammar() # all C keywordGrammar




