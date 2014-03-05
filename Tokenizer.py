######################       "files imported"
from Symbol import *
##########################
defineTable={}
def configure_defineTable(table):
    global defineTable
    defineTable=table
##################################
######################
class Tokenizer: # Class for Split Token
    global array
    def __init__(self,str):
        self.wordAhead=None
        self.word=None
        self.storeforpeep=None
        self.current=None
        self.variable_of_define=[]
        self.define=False
        self.count=0
        self.checksemicolumn=None
        self.array_constant=[]
        self.checkconstantidentifierarray=[]
        self.statement_of_define=[]
        self.arraystore=[]
        self.HasDefine=False
        self.checkfinishdefine=False
        self.once=False
        self.value=0
        self.test=False

        if str is not None:
            s=''
            sentences=str.split('\n')
            for sentence in sentences:
                s=s+sentence +' (newline) '
            self.array=s.split()
            del self.array[-1]
        else:
            self.array=[]
        self.gen=self.advanceToken()

    def advanceToken(self):
        global defineTable
        for word in self.array:
            if self.define==True:
                for token in self.array_constant:
                    yield token
                while True:
                    self.array_constant=[]
                    break
            yield word
        while True:
            yield None

    def advance(self,expected=None):
        if self.test==True:
            self.test=False
            if self.word in defineTable:
                self.array_constant=defineTable.get(self.word)
                self.define=True
                self.word=self.array_constant[0]
                del self.array_constant[0]
                self.wordAhead=None
        else:
            if self.wordAhead is not None:
                if expected is not None:
                    if expected is not self.word:
                        raise SyntaxError('Expected {0}, but encounterd {1}'.format(expected,self.word))
                temp=self.wordAhead
                self.wordAhead=None
                return temp
            self.word=next(self.gen)
            while self.HasDefine != True and self.word == '(newline)':
                self.word=next(self.gen)


        if self.checkfinishdefine==True:
            if self.word in defineTable:
                self.array_constant=defineTable.get(self.word)
                self.define=True
                self.word=self.array_constant[0]
                del self.array_constant[0]

        if(self.word=='//' or self.word=='/*'):
            i=True
            while(i):
                if(self.word=='*/'):
                    i=False
                self.word=next(self.gen)
        if expected is not None:
            if expected != self.word:
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
        if self.wordAhead is None or self.test==True:
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

    def checkdefine(self,bool):
        self.HasDefine=bool
        return

    def finishdefine(self,bool):
        self.checkfinishdefine=bool
        return

    def specialcondition(self,bool):
        self.test=bool
        return