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
##"File imported."                                                            ##
from CSymbol import*
##"Initialization."                                                           ##
tokenizer=0
expression=0
##"Injection tokenizer from Ckeyword."                                        ##
def configure_tokenizer_forType(module):
    global tokenizer
    tokenizer=module
##"Injection expression from Ckeyword."                                       ##
def configure_expression_forType(module):
    global expression
    expression=module
##"Keyword register to symbolTable."                                          ##
def keyword(id):
    sym=symbol(id)
    sym.arity=None
    return sym
##"Type to configure." For e.g. int , double ,char.                           ##
def configureType(type,attribute=None,content=None,userDefined=None,setorigin=None):
    global tokenizer
    check_for_redeclaration=[]
    def REPR(self):
        if hasattr(self,'second'):
            if self.second != None :
                return '({0} {1})'.format(self.id ,self.first)
        return '({0} {1})'.format(self.id ,self.first)

    def limitedExpression(self,rightBindingPower):
        token=tokenizer.peepahead()
        while(rightBindingPower<token.leftBindingPower):
            token=token.led(self)
            self=token
            token=tokenizer.peepahead()
        return self

    def std(self,token=None):
        arrayfirst=[]
        arraysecond=[]
        Passonce=False
#  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" #
        if hasattr(self,'attribute'):
            for word in check_for_redeclaration:
                if tokenizer.peepahead().first == word.first and self.attribute!='(enum)':
                    raise SyntaxError('Do not expect redeclaration of "{0}".'.format(word.first))
            if self.attribute=='(configureStructType)' or self.attribute=='(enum)' or self.attribute=='(typedef)':
                if tokenizer.peepahead().id=='(identifier)':
                    self.first=tokenizer.advance()
                    check_for_redeclaration.append(self.first)
                    if self.attribute=='(typedef)':
                        tokenizer.advance(';')
                else:
                    if tokenizer.peepahead().id in symbolTable:
                        raise SyntaxError ('Do not expect redeclaration of "{0}".'.format(self.id))
                    raise SyntaxError ('Expected an "identifier" after {0}'.format(self.id))
#  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" #
            self=self.limitedExpression(0)
            checkahead=tokenizer.peepahead()
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'#
            if hasattr (self ,'type'):
                    if hasattr(self,'second'):
                            Passonce=True
            if hasattr(checkahead,'first'):
                while checkahead.first==',':
                    if hasattr(self,'second'):
                        if Passonce==True:
                            Passonce=False
                            arrayfirst.append(self)
                            arraysecond.append(None)
                        else:
                            arrayfirst.append(self.first)
                            arraysecond.append(self.second)
                    else:
                        arrayfirst.append(self)
                        arraysecond.append(None)
                    if tokenizer.peepahead().first!=';':
                        checkahead=tokenizer.advance()
                    else:
                        checkahead=tokenizer.peepahead()
                    if checkahead.first==';':
                        temp=arrayfirst[0]
                        arrayfirst[0]=temp.first
                        self=symbolTable.get('=')()
                        self.first=temp
                        temp.first=arrayfirst
                        for word in arraysecond:
                            NoValue=False
                            if word != None:
                                NoValue=True
                                break
                        if NoValue == False:
                            self=temp
                            self.first=arrayfirst
                            return self
                        self.second=arraysecond
                        return self
                    self=expression.expression(0)
            return self
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'#
        else:
                storetemp=None
                Passonce=False
                temp=[]
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'#
                if tokenizer.peepahead().id == '(identifier)':
                    self.first=tokenizer.advance()
                    temp.append(self.first)
                    if hasattr(self,'type'):
                        pass
                    else:
                        while tokenizer.peepahead().first == ',' and not expression.functiondeclare:
                            tokenizer.advance()
                            temp.append(tokenizer.advance())
                    if temp.__len__() != 1:
                        self.first=temp
                elif token !=None:
                    self.first=token.led(self)
                elif tokenizer.peepahead().first == ',' or tokenizer.peepahead().id==')':
                    return self
                else:
                    self.first=expression.expression(100)
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'#
                self=self.limitedExpression(0)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'#
                if hasattr(self,'function_attribute'):
                    checkahead=tokenizer.peepahead()
                    if checkahead.first==';':
                        tokenizer.advance()
                    return self
                if hasattr(self,'type'):
                    if hasattr(self,'second'):
                        Passonce=True
                if hasattr(self,'first'):
                    if hasattr(self.first,'type') or Passonce==True:
                        checkahead=tokenizer.peepahead()
                        if checkahead.first==';':
                            storetemp=tokenizer.advance()
                        checkahead=tokenizer.peepahead()
                        while checkahead.first==',':
                            checkahead=tokenizer.advance()
                            if hasattr(self,'second'):
                                if Passonce==True:
                                    Passonce=False
                                    arrayfirst.append(self)
                                    arraysecond.append(None)
                                else:
                                    arrayfirst.append(self.first)
                                    arraysecond.append(self.second)
                            else:
                                arrayfirst.append(self)
                                arraysecond.append(None)

                            if checkahead.first==';':
                                temp=arrayfirst[0]
                                arrayfirst[0]=temp.first
                                self=symbolTable.get('=')()
                                self.first=temp
                                temp.first=arrayfirst
                                for word in arraysecond:
                                    NoValue=False
                                    if word != None:
                                        NoValue=True
                                        break
                                if NoValue == False:
                                    self=temp
                                    self.first=arrayfirst
                                    return self
                                self.second=arraysecond
                                return self
                            self=expression.expression(0)
        if hasattr(self,'type') or (self.id=='=' and hasattr(self,'topass')):
            if hasattr(self,'topass'):
                pass
            else:
                if hasattr(storetemp,'first') or storetemp==None:
                    if storetemp==None:
                        raise SyntaxError('Expected ";"')
                    if storetemp.first!=';':
                        raise SyntaxError('Expected ";"')
        return self
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'#
#Type Declaration                                                             ##
    sym=keyword(type)
    if attribute=='(struct)':
        sym.std=std
        sym.first=None
        sym.second=content
        sym.type=userDefined
        sym.origin=None
        sym.limitedExpression=limitedExpression
        sym.__repr__=REPR
        sym.attribute=None
        for struct in symbolTable:
            if struct == "struct":
                sym.interpreter=symbolTable['struct'].interpreter
                sym.assign=symbolTable['struct'].assign
                sym.findthecontent=symbolTable['struct'].findthecontent

    elif attribute=='(typedef)':
        sym.std=std
        sym.first=None
        sym.attribute='(typedef)'
        sym.second=content
        sym.type=userDefined
        sym.origin=setorigin
        sym.limitedExpression=limitedExpression
        sym.__repr__=REPR
        for struct in symbolTable:
            if struct == "struct":
                sym.interpreter=symbolTable['struct'].interpreter
                sym.assign=symbolTable['struct'].assign
                sym.findthecontent=symbolTable['struct'].findthecontent

    elif attribute == '(enum)':
        sym.std=std
        sym.first=None
        sym.second=content
        sym.type=userDefined
        sym.origin=None
        sym.attribute='(enum)'
        sym.limitedExpression=limitedExpression
        sym.__repr__=REPR
        for enum in symbolTable:
            if enum == "enum":
                sym.interpreter=symbolTable['enum'].interpreter
                sym.assign=symbolTable['enum'].assign

    else:
        sym.topass=None
        sym.type=None
        sym.std=std
        sym.first=None
        sym.second=None
        sym.normal=None
        sym.limitedExpression=limitedExpression
        sym.__repr__=REPR
##                                                                            ##