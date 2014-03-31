#-------------------------------------------------------------------------------
# Name:        PythCparser
# Purpose:     To parse and interpret C language by using Python.
#
# Author:      Goh Eng Fook
#              Lim Bing Ran
#
# Created:     07/03/2013
# Copyright:   (c) 2013-2014, Goh Eng Fook & Lim Bing Ran
# Licence:     GPLv3
#-------------------------------------------------------------------------------
##"Files imported."                                                           ##
from CSymbol import *
from Tokenizer import *
from ConfigureCType import *
##"DefineTable and stringTable created.                                       ##
defineTable={}
stringTable={}
##"Add id to the defineTable if defineTable don't contain it."                ##
def define(id,constant_token):
    global defineTable
    if id not in defineTable:
        defineTable[id]=constant_token
        return
    else:
        retrive_constant_token=defineTable.get(id)
        if constant_token==retrive_constant_token:
            pass
        else:
            raise SyntaxError('Invalid Statement : #define ')
        return
##"Add string to the stringTable if stringTable don't contain it."            ##
def string(id,constant_token):
    global stringTable
    if id not in stringTable:
        stringTable[id]=constant_token
        return
    else:
            raise SyntaxError('Do not expect redeclaration: "{0}".'.format(id))

##"Initialization."                                                           ##
expression=0
tokenizer=0
##"Injection expression from Cparser."                                        ##
def configure_C_Keyword(module):
    global expression
    expression=module
##"Injection tokenizer from Cparser."                                         ##
def configure_tokenizer_Keyword(module):
    global tokenizer
    tokenizer=module
##"Keyword register to symbolTable."                                          ##
def keyword(id):
    sym=symbol(id)
    sym.arity=None
    return sym
##"ParseStatement to perform every specific keyword function."                ##
def parseStatement():
    global tokenizer
    configure_tokenizer_forType(tokenizer)
    configure_expression_forType(expression)
    token=tokenizer.advance()
    temp=token.std()
    return temp
##"The entire different type of function along Ckeyword."                     ##
def CkeywordGrammar():
            global FlowControlStack
            FlowControlStack=[]
################################################################################
# #define std
################################################################################
            def std(self,leftToken=None):
                token=self
                if (tokenizer.peepahead().first=='define'):
                    token.second=tokenizer.advance()
                else:
                    token.second=None
                token.first=tokenizer.advance()
                token.first.type='constant'
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
                token.first.constantidentifiercontent=' '.join(constant_token)
                checkAhead=tokenizer.peepahead()
                if checkAhead.first=='(end)':
                    token.first.constantidentifiercontent=' '.join(constant_token)
                    return token
                if hasattr(checkAhead,'std'):
                    if checkAhead.id=='#' or checkAhead.id=='#define':
                        token.first.constantidentifiercontent=' '.join(constant_token)
                        return token
                    token.first.constantidentifiercontent=' '.join(constant_token)
                    tokenizer.finishdefine(True)
                    return token
                else:
                    tokenizer.finishdefine(True)
                    token.first.constantidentifiercontent=' '.join(constant_token)
                    tokenizer.specialcondition(True)
                    checkAhead=tokenizer.peepahead()
                    return token

            def REPR(self):
                if self.second==None:
                    return '({0} {1} {2})'.format(self.id, self.first,self.first.constantidentifiercontent)
                else:
                    return '({0}{1} {2} {3})'.format(self.id,self.second, self.first,self.first.constantidentifiercontent)

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
# if else std -> if std
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

            def REPR(self):
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

# if else std -> else std                                                     ##
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
# do while std -> while std
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
                        tokenizer.advance(';')
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

# do std                                                                      ##
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
# for std
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
# switch case + default std -> switch std
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

# case std                                                                    ##
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

# default std                                                                 ##
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
# Braces std
################################################################################
            global previous
            global rootindex
            global root
            root=None
            previous=-1
            rootindex=0


            def std(self,symboltoken=None):
                if symboltoken==None or symboltoken=='(enum)' or hasattr (symboltoken,'topass'):
                    global previous
                    global rootindex
                    global root
                    previous=previous+1
                    array=[]
                    arrayinput=False
                    check=tokenizer.peepahead()
                    while check.id !='}':
                            if hasattr(check,'std'):
                               if(check.id== 'case' or check.id =='default'):
                                    temp=check.std()
                               else:
                                    temp=parseStatement()
                            else:
                                if symboltoken=='(enum)':
                                    enumtoken=tokenizer.peepahead()
                                    enumtoken.enumtype='onlyallowdigit'
                                temp=expression.expression(0)
                                if check.id=='(identifier)' and tokenizer.peepahead().first==',':
                                    tokenizer.advance(',')
                                elif check.id=='(identifier)' and tokenizer.peepahead().id=='}':
                                        if symboltoken==None:
                                            tokenizer.advance(';')
                                        else:
                                            pass
                                else:
                                    if check.id=='(literal)' and tokenizer.peepahead().first==',':
                                        array.append(check)
                                        check=tokenizer.peepahead()
                                        tokenizer.advance()
                                        while check.first == ',':
                                            array.append(tokenizer.advance())
                                            if tokenizer.peepahead().first!=',':
                                                arrayinput=True
                                                break
                                            else:
                                                check=tokenizer.advance()


                                    if check.id=='(literal)' and tokenizer.peepahead().id=='}':
                                        if hasattr (symboltoken,'topass'):
                                            pass
                                        else:
                                            tokenizer.advance(';')
                                    else:
                                        tokenizer.advance(';')
                            if arrayinput!=True:
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
                else:
                    content=symboltoken.second.first
                    arraykeypair={}
                    array=[]
                    arrayset2=[]
                    for word in content:
                        checkAhead=tokenizer.peepahead()
                        if checkAhead.id=='}':
                            break
                        array.append(checkAhead)
                        if checkAhead.id=='.':
                            dot=tokenizer.advance()
                            checkAhead=tokenizer.peepahead()
                            dot.first=checkAhead
                            while(checkAhead.id!='}'):
                                for word in content:
                                    if checkAhead.first==word.first.first:
                                        tokenizer.advance()
                                        if tokenizer.peepahead().id=='=':
                                            plus=tokenizer.advance()
                                            plus.first=dot
                                            arrayset2.append(plus)
                                            checkAhead=tokenizer.peepahead()
                                            plus.second=checkAhead
                                            arraykeypair[word]=checkAhead
                                            tokenizer.advance()
                                            checkAhead=tokenizer.peepahead()
                                            if checkAhead.first==',':
                                                tokenizer.advance(',')
                                                pass
                                                checkAhead=tokenizer.peepahead()
                                                if checkAhead.id=='.':
                                                    dot=tokenizer.advance()
                                                    pass
                                            elif checkAhead.id=='}':
                                                break
                                            else:
                                                raise SyntaxError('Invalid Statement')
                                            checkAhead=tokenizer.peepahead()
                                            dot.first=checkAhead
                                        else:
                                            raise SyntaxError ('Expected "=" after {0}'.format(word))
                            tokenizer.advance('}')
                            symboltoken.first.content=arraykeypair
                            self.first=arrayset2
                            return self
                        elif checkAhead.id=='(literal)':
                            arraykeypair[word]=tokenizer.advance()
                            if tokenizer.peepahead().first==',':
                                tokenizer.advance(',')
                        else:
                            break
                    tokenizer.advance('}')
                    symboltoken.first.content=arraykeypair
                    self.first=array
                    return self

            def REPR(self):
                self.second = '}'
                return '{0} {1} {2}'.format(self.id, self.first,self.second)

            sym=keyword('{')
            sym.std=std
            sym.back={}
            sym.address={}
            sym.first=None
            sym.second=None
            sym.__repr__=REPR
################################################################################
# Type std -> configure Type
################################################################################
            configureType('int')
            configureType('short')
            configureType('double')
            configureType('char')
            configureType('float')
            configureType('void')
################################################################################
# return + break and continue std -> return std
################################################################################
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

# break std                                                                   ##
# continue std                                                                ##
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
# struct std
################################################################################
            def std(self,attribute=None):
                array=[]
                check_for_redeclaration=[]
                check_for_redeclaration2=[]
                CheckAhead=tokenizer.peepahead()
                if CheckAhead.id=='(identifier)':
                    temp=''.join(self.id +' '+ CheckAhead.first)
                    if temp in symbolTable:
                        token=symbolTable.get(temp)()
                        token.attribute='(configureStructType)'
                        tokenizer.advance()
                        token=token.std(token)
                        tokenizer.advance(';')
                        return token
                    self.first=tokenizer.advance()
                    self.first.id='StructIdentifier'
                else:
                    self.first=None
                    self.second=parseStatement()
                    if attribute!='typedef':
                        array2=[]
                        while tokenizer.peepahead().id=='(identifier)' and tokenizer.peepahead().first!=';' and attribute!='typedef':
                            for word in check_for_redeclaration:
                                if tokenizer.peepahead().first == word.first:
                                    raise SyntaxError('Do not expect redeclaration of "{0}".'.format(word.first))
                            check_for_redeclaration.append(tokenizer.peepahead())
                            array2.append(tokenizer.advance())
                            if tokenizer.peepahead().first==',':
                                tokenizer.advance(',')
                            elif tokenizer.peepahead().first==';':
                                self.third=array2
                                for word in self.third:
                                    temp=''.join('NamELesS' +' '+ word.first)
                                    configureType(temp,'(struct)',self.second)
                                tokenizer.advance(';')
                                break;
                            else:
                                raise SyntaxError('Invalid Statement.')
                    return self
                if tokenizer.peepahead().id=='{':
                    self.second=parseStatement()
                else:
                    raise SyntaxError('Expect a "{0}" after "{1}".'.format('{',self.first))
                while tokenizer.peepahead().id=='(identifier)' and tokenizer.peepahead().first!=';' and attribute!='typedef':
                    for word in check_for_redeclaration2:
                                if tokenizer.peepahead().first == word.first:
                                    raise SyntaxError('Do not expect redeclaration of "{0}".'.format(word.first))
                    check_for_redeclaration2.append(tokenizer.peepahead())
                    array.append(tokenizer.advance())
                    if tokenizer.peepahead().first==',':
                        tokenizer.advance(',')
                    elif tokenizer.peepahead().first==';':
                        self.third=array
                        break;
                    else:
                        raise SyntaxError('Invalid Statement.')
                if attribute=='typedef':
                    pass
                else:
                    tokenizer.advance(';')
                configureType(temp,'(struct)',self.second)
                return self
            def REPR(self):
                if self.second==None:
                    return '({0} {1})'.format(self.id, self.first)
                if self.first==None:
                    if self.third!=None:
                        return '({0} {1} {2})'.format(self.id, self.second,self.third)
                    return '({0} {1})'.format(self.id, self.second)
                if self.third==None:
                    return '({0} {1} {2})'.format(self.id, self.first, self.second)
                return '({0} {1} {2} {3})'.format(self.id, self.first, self.second,self.third)

            sym=keyword('struct')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.third=None
            sym.__repr__=REPR
################################################################################
# typedef std
################################################################################
            def std(self,leftToken=None):
                array1=[]
                if hasattr(self,'struct'):
                    self.first=tokenizer.advance()
                    tokenizer.advance(';')
                    return self
                else:
                    CheckAhead=tokenizer.peepahead()
                if CheckAhead.id=='struct':
                    store=tokenizer.advance()
                    self.first=store.std('typedef')
                    check_for_redeclaration=[]
                    while tokenizer.peepahead().id=='(identifier)' and tokenizer.peepahead().first!=';':
                        for word in check_for_redeclaration:
                                if tokenizer.peepahead().first == word.first:
                                    raise SyntaxError('Do not expect redeclaration of "{0}".'.format(word.first))
                        check_for_redeclaration.append(tokenizer.peepahead())
                        array1.append(tokenizer.advance())
                        if tokenizer.peepahead().first==',':
                            tokenizer.advance(',')
                        elif tokenizer.peepahead().first==';':
                            self.second=array1
                            for word in self.second:
                                    configureType(word,'(struct)',self.first)
                            break;
                        else:
                            raise SyntaxError('Invalid Statement.')
                    for word in self.second:
                        configureType(word.first,'(typedef)',self.first.second,None,self.first)
                    tokenizer.advance(';')
                elif hasattr(CheckAhead,'std') and CheckAhead.id!='char':
                    self.first=parseStatement()
                    self.second=None
                    return self
                else:
                        if hasattr(CheckAhead,'topass'):
                            CheckAhead.topass=True
                        token=tokenizer.advance()
                        token2=None
                        if tokenizer.peepahead().id=='*':
                            token2=tokenizer.advance()
                        self.first=tokenizer.advance()
                        self.second=token.std(token2)
                return self
            def REPR(self):
                if self.second==None:
                    return '({0} {1})'.format(self.id, self.first)
                return '({0} {1} {2})'.format(self.id, self.first, self.second)

            sym=keyword('typedef')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.__repr__=REPR
################################################################################
# enum std
################################################################################
            def std(self,Tokenstore=None):
                CheckAhead=tokenizer.peepahead()
                if CheckAhead.id=='(identifier)':
                    temp=''.join(self.id +' '+ CheckAhead.first)
                    if temp in symbolTable:
                        token=symbolTable.get(temp)()
                        token.attribute='(enum)'
                        tokenizer.advance()
                        temporary=token.std(token)
                        tokenizer.advance(';')
                        return temporary
                self.first=tokenizer.advance()
                self.first.id='EnumIdentifier'
                token=tokenizer.advance()
                if tokenizer.peepahead().id != '(identifier)':
                    raise SyntaxError('Do not allow digit')
                else:
                    self.second=token.std('(enum)')
                temp=''.join(self.id +' '+ self.first.first)
                configureType(temp,'(enum)',self.second)
                if tokenizer.peepahead().first==';':
                    self.third=None
                else:
                    array=[]
                    while tokenizer.peepahead().first!=';':
                        array.append(tokenizer.advance())
                        if tokenizer.peepahead().first==',':
                            tokenizer.advance(',')
                        elif tokenizer.peepahead().first==';':
                            pass
                        else:
                            raise SyntaxError('Do not expected "{0}" , invalid statement.'.format(tokenizer.peepahead()))
                    self.third=array
                tokenizer.advance(';')
                for word in self.second.first:
                    if word.id =='=':
                        if word.second.id=='(literal)':
                            return self
                        elif word.second.id == '(identifier)':
                             raise SyntaxError ('Expected a digit but not {0}.'.format(word.second))
                        else:
                            def scan(token):
                                if hasattr(token,'first'):
                                        if token.first.id=='(identifier)':
                                            raise SyntaxError ('Expected a digit but not {0}.'.format(token.first))
                                if hasattr(token,'second'):
                                        if token.second.id=='(identifier)':
                                            raise SyntaxError ('Expected a digit but not {0}.'.format(token.second))

                            def scanstartingpoint(token):
                                if token.second.id =='(literal)':
                                    if token.first.id!='(literal)':
                                        scanstartingpoint(token.first)
                                    return
                                elif token.second.id =='(identifier)':
                                    raise SyntaxError ('Expected a digit but not {0}.'.format(token.second))
                                else:
                                    scan(token.second)
                                    scanstartingpoint(token.second)
                                    if token.first.id =='(literal)':
                                        return
                                    elif token.first.id =='(identifier)':
                                        raise SyntaxError ('Expected a digit but not {0}.'.format(token.second))
                                    else:
                                        scan(token.first)
                                        scanstartingpoint(token.first)

                            scanstartingpoint(word.second)


                return self

            def REPR(self):
                    if hasattr(self,'struct'):
                        return '({0} {1})'.format(self.id, self.first)
                    return '({0} {1} {2} {3})'.format(self.id, self.first, self.second, self.third)

            sym=keyword('enum')
            sym.std=std
            sym.first=None
            sym.second=None
            sym.third=None
            sym.__repr__=REPR
################################################################################
# string std
################################################################################
            def std(self,Tokenstore=None):
                temp=''
                tokenizer.checkdefine(True)
                CheckAhead=tokenizer.advance()
                while CheckAhead.id !='"':
                    if temp=='':
                        space=''
                    else:
                        space=' '
                    if CheckAhead.id == '(identifier)' or CheckAhead.id == '(literal)':
                        if CheckAhead.first=='(newline)':
                            temp=temp+'\n\t\t\t'
                        else:
                            temp=temp+''.join(space + CheckAhead.first)
                    else:
                        temp=temp+''.join(space + CheckAhead.id)
                    CheckAhead=tokenizer.advance()
                length=len(temp)
                tokenizer.checkdefine(False)
                if Tokenstore==None:
                    temp=createIndentifier(temp)
                    temp.type='string'
                    return temp
                while length>int(Tokenstore.first.second.first):
                    temp=temp[:-1]
                    length=length-1
                    temp=''.join(temp)
                    if length==int(Tokenstore.first.second.first):
                        print ("Warning : array out of range " )
                        break
                tokenizer.advance(';')

                string(Tokenstore.first.first.first,createIndentifier(temp))
                self.first=createIndentifier(temp)
                self.id='(identifier)'
                self.type='stringIdentifier'
                return self.first

            def REPR(self):
                    return '({0})'.format(self.first)

            sym=keyword('"')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR
################################################################################
# Type std
################################################################################
            def REPR(self):
                if hasattr (self,'first'):
                    return '({0} {1})'.format(self.id,self.first)
                else:
                    return '({0})'.format(self.id)

            def std(self,previous=None):
                if tokenizer.peepahead().id != 'int' :
                    raise SyntaxError ('Should enter int nt {0}.'.format(tokenizer.peepahead().id))
                temp=tokenizer.advance().std()
                temp1=self.id + ' '+'int'
                sym=symbol(temp1)
                sym.__repr__=REPR
                sym.arity='binary'
                sym.interpreter=symbolTable['short'].interpreter
                sym.std=symbolTable['short'].std
                sym.assign=symbolTable['short'].assign
                sym.value=0xffff
                temp2=symbolTable[temp1]()
                if temp.id == '=':
                    temp2.first=temp.first.first
                    temp.first=temp2
                    return temp
                elif temp.id == 'int':
                    temp2.first=temp.first
                    return temp2

            sym=keyword('short')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR

            def std(self):
                List= ['double','int']
                if tokenizer.peepahead().id not in List:
                    raise SyntaxError ('Enter the wrong format after {0}.'.format(self.id))
                temp=tokenizer.advance().std()
                if temp.id != '=':
                    temp1=self.id + ' '+temp.id
                    if temp.id == 'double':
                        value=None
                    else:
                        value=0xffffffff
                else:
                    temp1=self.id +' '+temp.first.id
                    if temp.first.id == 'double':
                        value=None
                    else:
                        value=0xffffffff
                sym=symbol(temp1)
                sym.__repr__=REPR
                sym.arity='binary'
                sym.interpreter=symbolTable['long'].interpreter
                sym.std=symbolTable['long'].std
                sym.assign=symbolTable['long'].assign
                sym.value=value
                temp2=symbolTable[temp1]()
                if temp.id == '=':
                    temp2.first=temp.first.first
                    temp.first=temp2
                    return temp
                else:
                    temp2.first=temp.first
                    return temp2

            sym=keyword('long')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR

            def std(self):
                List= ['short','int','char']
                if tokenizer.peepahead().id not in List:
                    raise SyntaxError ('Enter the wrong format after {0}.'.format(self.id))
                temp=tokenizer.advance().std(self.id)
                if temp.id != '=':
                    temp1=self.id + ' '+temp.id
                    if temp.id == 'short int':
                        value=0xffff
                    elif temp.id == 'int':
                        value=0xffffffff
                    else:
                        value=0xff
                else:
                    temp1=self.id +' '+temp.first.id
                    if temp.first.id == 'short int':
                        value=0xffff
                    elif temp.first.id == 'int':
                        value=0xffffffff
                    else:
                        value=0xff
                sym=symbol(temp1)
                sym.__repr__=REPR
                sym.arity='binary'
                sym.interpreter=symbolTable['unsigned'].interpreter
                sym.std=symbolTable['unsigned'].std
                sym.assign=symbolTable['unsigned'].assign
                sym.value=value
                temp2=symbolTable[temp1]()
                if temp.id == '=':
                    temp2.first=temp.first.first
                    temp.first=temp2
                    return temp
                else:
                    temp2.first=temp.first
                    return temp2

            sym=keyword('unsigned')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR

            def std(self):
                if tokenizer.peepahead().id != 'char' :
                    raise SyntaxError ('Should enter char nt {0}.'.format(tokenizer.peepahead().id))
                temp=tokenizer.advance().std()
                temp1=self.id + ' '+'char'
                sym=symbol(temp1)
                sym.__repr__=REPR
                sym.arity='binary'
                sym.interpreter=symbolTable['signed'].interpreter
                sym.std=symbolTable['signed'].std
                sym.assign=symbolTable['signed'].assign
                sym.value=0xff
                temp2=symbolTable[temp1]()
                if temp.id == '=':
                    temp2.first=temp.first.first
                    temp.first=temp2
                    return temp
                elif temp.id == 'char':
                    temp2.first=temp.first
                    return temp2

            sym=keyword('signed')
            sym.std=std
            sym.first=None
            sym.__repr__=REPR
################################################################################
################################################################################
##"Call C keywordGrammar."                                                    ##
CkeywordGrammar()
##                                                                            ##
