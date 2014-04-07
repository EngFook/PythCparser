#-------------------------------------------------------------------------------
# Name:         PythCparser
# Purpose:      To parse and interpret C language by using Python.
#
# Author:       Tunku Abdul Rahman University College
#               Microelectronics and Physics Division 2014
#               Goh Eng Fook
#               Lim Bing Ran
#
# Supervise by: Dr. Poh Tze Ven
#
# Created:      07/03/2013
# Copyright:    (c) 2013-2014, Goh Eng Fook & Lim Bing Ran
# License:      GPLv3
#-------------------------------------------------------------------------------
##"Files imported."                                                           ##
from CSymbol import *
##"Injection defineTable from Ckeyword."                                      ##
defineTable={}
def configure_defineTable(table):
    global defineTable
    defineTable=table
##"Class for retrive token."                                                  ##
##"Initialize                                                                 ##
class Tokenizer:
    global array
    def __init__(self,str):
        global defineTable
        self.word=None
        self.current=None
        self.wordAhead=None
        self.storeforpeep=None
        self.test=False
        self.define=False
        self.HasDefine=False
        self.checkfinishdefine=False
##"Split the string and create newline when proceed to next line."            ##
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
##"To pop out the token from the current store array."                        ##
    def advanceToken(self):
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
##"Main function: To pop out the next token and shift the pointer."           ##
## E.g: Tokenizer(' 2 + 3 + 4 + 5 ')   None ' 2 + 3 + 4 = 5 '                 ##
## Pointer ->                           P^
## Once advance() , Pointer ->               P^:pop'2'                        ##
##"Part of code were added for replace the ConstantIdentifier from #define."  ##
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
##"Categorized the retrived token word."                                      ##
        if(self.word=='//' or self.word=='/*'):
            i=True
            while(i):
                if(self.word=='*/'):
                    i=False
                self.word=next(self.gen)
        if expected is not None:
            if expected != self.word:
                raise SyntaxError('Expected {0}, but encounterd {1}'
                                  .format(expected,self.word))
        if self.word in symbolTable:
            sym=symbolTable[self.word]
            return sym()
        elif self.word is None:
            self.current=createSystemToken('(end)')
        elif self.word.isidentifier():
            self.current=createIndentifier(self.word)
        else:
            self.current=createLiteral(self.word)
        self.storeforpeep=self.current
        return self.current
##"For check the next token."                                                 ##
## E.g: Tokenizer(' 2 + 3 + 4 + 5 ')   None ' 2 + 3 + 4 = 5 '                 ##
## Pointer ->                           P^
## Once peepahead() , Pointer ->        P^:pop'2'                             ##
    def peepahead(self):
        if self.wordAhead is None or self.test==True:
            self.wordAhead=self.advance()
        return self.wordAhead
##"For retrive the current token."                                            ##
##!!This function do not performed well but it did not used in this program.!!##
##!!Have to modify at future.!!                                               ##
    def peep(self):
        if self.storeforpeep is None:
            self.peepahead()
            return None
        if self.wordAhead is not None:
            return self.storeforpeep
        else:
            return self.current
##"Condition to set when perform the #define function."                       ##
    def checkdefine(self,bool):
        self.HasDefine=bool
        return
    def finishdefine(self,bool):
        self.checkfinishdefine=bool
        return
    def specialcondition(self,bool):
        self.test=bool
        return
##                                                                            ##