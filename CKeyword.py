####################################       "files imported"
from Symbol import *
from Tokenizer import *
#######################################
array=[]
def configure_array(module):
    global array
    array=module
######################
defineTable={} #set the define list.
def define(id,constant_token): #to add id to the symbolTable if symbolTable don't contain it
    global defineTable
    if id not in defineTable:
        defineTable[id]=constant_token
        return
    else:
        retrive_constant_token=defineTable.get(id)
        if constant_token==retrive_constant_token:
            pass
        else:
            array.clear()
            raise SyntaxError('Invalid Statement : #define ')
        return
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
    sym.arity=None
    return sym
def parseStatement():
    global tokenizer
    token=tokenizer.advance()
    temp=token.std()
    return temp
################################################################################

def CkeywordGrammar():
            global FlowControlStack
            FlowControlStack=[]
            def std(self,leftToken=None):
                token=self
                if (tokenizer.peepahead().first=='define'):
                    token.second=tokenizer.advance()
                else:
                    token.second=None
                token.first=tokenizer.advance()
                token.first.id='ConstantIdentifier'
                constant_token=[]
                checkAhead=tokenizer.peepahead()
                tokenizer.checkdefine(True)
                while  checkAhead.first != '(end)' and checkAhead.first != '(newline)':
                    while tokenizer.peepahead().first==' \ ':
                        tokenizer.advance()
                    if checkAhead.id =='(identifier)' or checkAhead.id == '(literal)':
                            constant_token.append(tokenizer.advance().first)
                    else:
                            constant_token.append(tokenizer.advance().id)
                    checkAhead=tokenizer.peepahead()
                define(token.first.first,constant_token)
                configure_defineTable(defineTable)
                tokenizer.checkdefine(False)
                checkAhead=tokenizer.peepahead()
                while checkAhead.first=='(newline)':
                    tokenizer.advance()
                    checkAhead=tokenizer.peepahead()
                token.first.constantidentifier=' '.join(constant_token)
                checkAhead=tokenizer.peepahead()
                if checkAhead.first=='(end)':
                    token.first.constantidentifier=' '.join(constant_token)
                    return token
                if hasattr(checkAhead,'std'):
                    if checkAhead.id=='#' or checkAhead.id=='#define':
                        token.first.constantidentifier=' '.join(constant_token)
                        return token
                    token.first.constantidentifier=' '.join(constant_token)
                    tokenizer.finishdefine(True)
                    return token
                else:
                    tokenizer.finishdefine(True)
                    token.first.constantidentifier=' '.join(constant_token)
                    tokenizer.specialcondition(True)
                    checkAhead=tokenizer.peepahead()
                    return token

            def REPR(self):
                if self.second==None:
                    return '({0} {1} {2})'.format(self.id, self.first,self.first.constantidentifier)
                else:
                    return '({0}{1} {2} {3})'.format(self.id,self.second, self.first,self.first.constantidentifier)

            sym=keyword('#')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.arity='unary'
            sym.__repr__=REPR
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
                    FlowControlStack.append(tokenizer.peepahead())
                    self.second=parseStatement()
                    FlowControlStack.pop()
                    if previous == -1 :
                        for check in self.second.first:
                            if check.id == 'case' :
                                raise SyntaxError('It is not inside switch loop')
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

                else:
                    self.third=None
                return self

            def REPR(self):##return '({0} {1} {2}) \n{3}'.format(self.id, self.first, self.second ,self.third)##
                if self.third == None:
                    if self.second == None:
                        return '{0} {1}'.format(self.id, self.first)
                    return '( {0} {1} {2} )'.format(self.id, self.first, self.second)
                if self.second == None:
                    return '( {0} {1} {2} )'.format(self.id, self.first,self.third)
                return '( {0} {1} {2} {3})'.format(self.id, self.first,self.second,self.third)


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
                    FlowControlStack.append(tokenizer.peepahead())
                    self.second=parseStatement()
                    if previous == -1 :
                        for check in self.second.first:
                            if check.id == 'case' :
                                raise SyntaxError('It is not inside switch loop')
                    FlowControlStack.pop()
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
                temp=tokenizer.advance()
                if(temp.id == 'while'):
                    self.second=temp.std()
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
                        tokenizer.advance(';')
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
                FlowControlStack.append(token)
                temp=token.std()
                FlowControlStack.pop()
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
                    self.first=expression.expression(0)
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
#############################################################################@@@
            global previous
            global rootindex
            global root
            root=None
            previous=-1
            rootindex=0

            def std(self):
                global previous
                global rootindex
                global root
                previous=previous+1
                array=[]
                check=tokenizer.peepahead()
                while check.id !='}':
                        if hasattr(check,'std'):
                           if(check.id== 'case' or check.id =='default'):
                                temp=check.std()
                           else:
                            temp=parseStatement()
                        else:
                            temp=expression.expression(0)
                            tokenizer.advance(';')
                        array.append(temp)
                        index=array.index(temp)
                        if previous :
                            if temp.id == 'case':
                                self.back[temp.first.first]=root,rootindex+1
                        else:
                            root=self
                            rootindex=index
                            if temp.id == 'case':
                                self.back[temp.first.first]=None
                        if hasattr(temp,'std'):
                            if temp.id == 'case':
                                case=temp.first
                                self.address[case.first]=index,self
                        check=tokenizer.peepahead()
                        if check == '(newline)':
                            tokenizer.advance()
                            check=tokenizer.peepahead()
                tokenizer.advance('}')
                check=tokenizer.peepahead()
                self.first=array
                previous=previous-1
                if previous == -1 :
                    rootindex=0
                return self

            def REPR(self):
                self.second = '}'
                return '{0} {1} {2}'.format(self.id, self.first,self.second)

            sym=keyword('{')
            sym.std=std
            sym.back={}
            sym.address={}
            sym.first=None
            sym.test='o-o'
            sym.second=None
            sym.__repr__=REPR

            def REPR(self):
                if hasattr(self,'second'):
                    if self.second != None :
                        return '({0} {1} {2})'.format(self.id ,self.first,self.second)
                return '({0} {1})'.format(self.id ,self.first)

            def limitedExpression(self,rightBindingPower):
                global tokenizer
                token=tokenizer.peepahead()
                while(rightBindingPower<token.leftBindingPower):
                    token=token.led(self)
                    self=token
                    token=tokenizer.peepahead()
                return self

            def std(self):
                if tokenizer.peepahead().id == '(identifier)':
                    self.first=tokenizer.advance()
                else:
                    self.first=expression.expression(100)
                self=self.limitedExpression(0)
                if tokenizer.peepahead().first == ';':
                    tokenizer.advance()
                return self

            sym=keyword('int')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.limitedExpression=limitedExpression
            sym.__repr__=REPR

            sym=keyword('double')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.limitedExpression=limitedExpression
            sym.__repr__=REPR

            def std(self):
                self.first=expression.expression(0)
                tokenizer.advance()
                return self

            def REPR(self):
                return '({0} {1})'.format(self.id ,self.first)

            sym=keyword('return')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR

            def std(self):
                if FlowControlStack != []:
                    self.braces=FlowControlStack[-1]
                tokenizer.advance(';')
                return self

            def REPR(self):
                return '{0}'.format(self.id)

            sym=keyword('break')
            sym.std=std
            sym.braces=None
            sym.first=None
            sym.__repr__=REPR

            sym=keyword('continue')
            sym.std=std
            sym.braces=None
            sym.first=None
            sym.__repr__=REPR


################################################################################
################################################################################
CkeywordGrammar() # all C keywordGrammar



