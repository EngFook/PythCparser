######################       "files imported"
from Symbol import *
######################
class Tokenizer: # Class for Split Token
    def __init__(self,str):
        self.wordAhead=None
        self.word=None
        self.storeforpeep=None
        self.current=None
        self.variable_of_define=None
        self.define=False
        self.count=0
        self.checksemicolumn=None
        self.array_constantidentifier=[]
        self.HasDefine=False
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
            for word in self.array:
                if self.define == False:
                    self.count=self.count+1
                    yield word
                for word in self.array_constantidentifier:
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
        while self.HasDefine != True and self.word == '(newline)':
            self.word=next(self.gen)
        ##################################### Code Added For #define constant identifier
        if self.word==self.variable_of_define:
            self.define=True
            count=0
            while count != self.count:
                del self.array[0]
                count=count+1
            count=0
            for i in self.statement_of_define:
                if count==0:
                    self.array_constantidentifier.append(self.statement_of_define[count])
                elif self.statement_of_define[count].id =='(identifier)':
                    change_to_str=self.statement_of_define[count]
                    change_to_str=''.join(change_to_str.first)
                    self.array_constantidentifier.append(change_to_str)
                elif self.statement_of_define[count].id =='(literal)':
                    change_to_str=self.statement_of_define[count]
                    change_to_str=''.join(change_to_str.first)
                    self.array_constantidentifier.append(change_to_str)
                else:
                    self.array_constantidentifier.append(self.statement_of_define[count].id)
                count=count+1
            count=0
            for i in self.array:
                self.array_constantidentifier.append(self.array[count])
                count=count+1
            if self.array_constantidentifier[0].id in symbolTable:
                temporary=self.array_constantidentifier[0]
                del self.array_constantidentifier[0]
                return temporary
            else:
                raise SyntaxError ('Invalid Statement')
        ################################################################################
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

    def storeconstantidentifier(self,token_string=None,token_variable=None):
        self.statement_of_define=token_string
        self.variable_of_define=token_variable
        return

    def checkdefine(self,bool):
        self.HasDefine=bool
        return
