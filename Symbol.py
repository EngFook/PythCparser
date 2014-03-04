symbolTable={}  #set the symbol list.
class SymbolBase: # Class for the parse engine purpose
    def led(self):
        raise SyntaxError('No led(.) function defined!')
    def nud(self):
        raise SyntaxError('No nud(.) function defined!')

def symbol(id,bindingPower = 0,Type=True): #to add id to the symbolTable if symbolTable don't contain it
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

def nud(self):  # this nud() is for return self value purpose
    return self


def printCharacter(self):
	    return '{0}'.format(self.first)

def createLiteral(value): # create literal
    sym=symbol('(literal)')
    sym.first=None
    sym.arity=None
    sym.__repr__=printCharacter
    sym.nud=nud
    symObj=sym()
    symObj.first=value
    return symObj

def createIndentifier(value): # create identifier
    sym=symbol('(identifier)')
    sym.first=None
    sym.arity=None
    sym.__repr__=printCharacter
    sym.nud=nud
    symObj=sym()
    symObj.first=value
    return symObj

def createSystemToken(value): # create identifier
    sym=symbol('(SystemToken)')
    sym.first=None
    sym.arity=None
    sym.__repr__=printCharacter
    sym.nud=nud
    symObj=sym()
    symObj.first=value
    return symObj

