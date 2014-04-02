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
# Created:      02/04/2014
# Copyright:    (c) 2013-2014, Goh Eng Fook & Lim Bing Ran
# Licence:      GPLv3
#-------------------------------------------------------------------------------
##"Files imported."                                                           ##
from CSymbol import *
##"Function to rebuild the string."                                           ##
##"This function is to reduce the sensitivity of the program but not all."    ##
def Rebuildstring(str):
    s=''
    sentences=str.split('\n')
    for sentence in sentences:
        s=s+sentence +' (newline) '
    returnhere=False
    meet=False
    countright=0
    countleft=-1
    combine=False
    stringright=''
    arraysymtoken=[]
    temp=s.split()
    temporary=[]
    string=''
    temp1=None
    for word in temp:
        if word == '(newline)':
            string=string+' '.join(temporary)+' '+'\n'+' '
            temporary=[]
        elif word in symbolTable and word is not '"' or word=='printf' or word == 'scanf':
            temporary.append(word)
        else:
            store1=[]
            store=[]
            count=-1
            for i in word:
                if meet==True:
                    if i.startswith('"'):
                        meet=False
                        store1.append(' '+i)
                        store.append(''.join(store1))
                    else:
                        store1.append(i)
                elif i.startswith('('):
                    returnhere=True
                    storename=''.join(store)+' '+i
                    store=[]
                    store.append(storename)
                elif i.startswith (';'):
                    semicolumn=' '+ i
                elif i.startswith ('"'):
                    store1.append(i +' ')
                    meet=True
                else:
                    semicolumn=''
                    store.append(i)
            if returnhere==True:
                temporary.append(' '.join(store)+semicolumn)
            else:
                for j in store:
                    countleft=countleft+1
                    countright=countright+1
                    if j in symbolTable:
                        combine=True
                        arraysymtoken.append(countright-1)
                        countleft=0
                if combine==True:
                    combine=False
                    while countleft>0:
                        stringleft=store[0]
                        stringleft=stringleft+' '
                        countleft=countleft-1
                    arraysymtoken.reverse()
                    for countget in arraysymtoken:
                        once=True
                        while countright>countget:
                            if once==True:
                                once=False
                                stringright1=store[countright-1]
                            stringright1=' '+stringright1
                            countright=countright-1
                        stringright=' '+''.join(store[countget])+stringright1+stringright
                    word=stringleft +stringright+semicolumn
                    temporary.append(word)
                else:
                    countleft=0
                    countright=0
                    keep=[]
                    for i in word:
                        if i.startswith (';'):
                            semicolumn=' '+ i
                        else:
                            semicolumn=''
                            keep.append(i)
                    word=''.join(keep)+semicolumn
                    temporary.append(word)
    return string
################################################################################