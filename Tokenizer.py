######################       "files imported"
from Symbol import *
######################
class Tokenizer: # Class for Split Token
    def __init__(self,str):
        self.wordAhead=None
        self.word=None
        self.storeforpeep=None
        self.current=None
        self.storecon1=None
        self.define=True
        self.array1=[]
        self.count=0
        if str is not None:
            self.array=str.split()
        else:
            self.array=[]
        self.gen=self.advanceToken()

    def advanceToken(self):

            for word in self.array:
                if self.define == True:
                    self.count=self.count+1
                    yield word
                for word in self.array1:
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
            if self.current.first==self.storecon1:
                self.define=False
                i=0
                while i != self.count:
                    del self.array[0]
                    i=i+1
                count=0
                for i in self.storecon:
                    if count==0:
                        self.array1.append(self.storecon[count])
                    else:
                        self.array1.append(self.storecon[count].id)
                    count=count+1
                count=0
                for i in self.array:
                    self.array1.append(self.array[count])
                    count=count+1
                if self.array1[0].id in symbolTable:
                    temp=self.array1[0]
                    del self.array1[0]
                    return temp
                else:
                    raise SyntaxError ('Invalid statement')
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
    def storeconstantidentifier(self,token=None,token1=None):
        self.storecon=token
        self.storecon1=token1
        return