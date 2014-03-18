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
            self=self.limitedExpression(0)
            return self
        else:
            temp=[]
            if tokenizer.peepahead().id == '(identifier)':
                self.first=tokenizer.advance()
                temp.append(self.first)
                while tokenizer.peepahead().first == ',' and not expression.functiondeclare:
                    tokenizer.advance()
                    temp.append(tokenizer.advance())
                if temp.__len__() != 1:
                    self.first=temp
            elif token !=None:
                self.first=token.led(self)
            else:
                self.first=expression.expression(100)
            self=self.limitedExpression(0)
            if tokenizer.peepahead().first == ';':
                tokenizer.advance()
            return self

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
    elif attribute == '(enum)':
        sym.std=std
        sym.first=None
        sym.second=None
        sym.attribute=None
        sym.limitedExpression=limitedExpression
        sym.__repr__=REPR

    else:
        sym.std=std
        sym.first=None
        sym.second=None
        sym.limitedExpression=limitedExpression
        sym.__repr__=REPR
##                                                                            ##