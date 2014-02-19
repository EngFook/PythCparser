######################       "files imported"
from symbol import *
######################
class Tokenizer: # Class for Split Token
    def __init__(self,str):
        self.wordAhead=None
        self.word=None
        self.storeforpeep=None
        self.current=None
        if str is not None:
            self.array=str.split()
        else:
            self.array=[]
        self.gen=self.advanceToken()

    def advanceToken(self):
        for word in self.array:
            yield word
        while True:
            yield None

    def advance(self,expected=None):
        if self.wordAhead is not None:
            if expected is not None:
                if expected is not self.word:
                    raise SyntaxError('Expected {0}, but encounterd {1}'.format(expected,self.word))
            temp=self.wordAhead
            self.wordAhead=None
            return temp
        self.word=next(self.gen)
        if(self.word=='//' or self.word=='/*'):
            i=True
            while(i):
                if(self.word=='*/'):
                    i=False
                self.word=next(self.gen)
        if expected is not None:
            if expected is not self.word:
                raise SyntaxError('Expected {0}, but encounterd {1}'.format(expected,self.word))
        if self.word in symbolTable:
            sym=symbolTable[self.word]
            return sym()
        elif self.word is None:
            self.current=createSystemToken('(end)')
        elif self.word.isdigit():
            self.current=createLiteral(self.word)
        else:
            self.current=createIndentifier(self.word)
        self.storeforpeep=self.current
        return self.current

    def peepahead(self):
        if self.wordAhead is None:
            self.wordAhead=self.advance()
        return self.wordAhead

    def peep(self):
        if self.storeforpeep is None:
            self.peepahead()
            return None
        if self.wordAhead is not None:
            return self.storeforpeep
        else:
            return self.current