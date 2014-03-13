##"SymbolTable created."                                                      ##
symbolTable={}
##"Class for raise SyntaxError when no led and nud function."                 ##
class SymbolBase: # Class for the parse engine purpose
    def led(self):
        raise SyntaxError('No led(.) function defined!')
    def nud(self):
        raise SyntaxError('No nud(.) function defined!')
##"Add id to the symbolTable if symbolTable don't contain it."                ##
def symbol(id,bindingPower = 0,Type=True): #
    global symbolTable
    if id not in symbolTable:
        class Symbol(SymbolBase):
            pass
        sym=Symbol
        sym.id=id
        sym.left=Type
        sym.leftBindingPower=bindingPower
        symbolTable[id]=sym
        return sym
    else:
        return symbolTable[id]
##"For return self value purpose."                                            ##
def nud(self):
    return self
##"Print style."                                                              ##
def printCharacter(self):
	    return '{0}'.format(self.first)
##"Create Literal when it is digit."                                          ##
def createLiteral(value): # create literal
    sym=symbol('(literal)')
    sym.first=None
    sym.arity=None
    sym.__repr__=printCharacter
    sym.nud=nud
    symObj=sym()
    symObj.first=value
    return symObj
##"Create Identifier when it is alphebat."                                    ##
def createIndentifier(value): # create identifier
    sym=symbol('(identifier)')
    sym.first=None
    sym.content=None
    sym.arity=None
    sym.__repr__=printCharacter
    sym.nud=nud
    symObj=sym()
    symObj.first=value
    return symObj
##"Create SystemToken when it is (end)."                                      ##
def createSystemToken(value): # create identifier
    sym=symbol('(SystemToken)')
    sym.first=None
    sym.arity=None
    sym.__repr__=printCharacter
    sym.nud=nud
    symObj=sym()
    symObj.first=value
    return symObj
##                                                                            ##