from math import acos,asin
from cmath import * 
from os import readlink
from unittest import result
#accepted input equation and return its type.
def getForm(inputFormular:str):
    inputlen = len(inputFormular)
    if '^' in inputFormular:
        return 'exp'
    elif 'cos' in inputFormular:
        return 'polar'
    elif 'i' in inputFormular:
        return 'general'
    else:
        return "error input type"
'''
    example of outputs:
    2e^3i: {'real':'2','img':'3'}
    3cos2pi+4sin2pii: {'real':"3cos2pi",'img':"4sin2pii"}
    2+3i: {'real':'2','img':'3'}
'''
def extractParts(inputFormular:str):
    formularLen = len(inputFormular)
    realPart = []
    imagePart = []
    if(getForm(inputFormular) == 'exp'):
        for letter in inputFormular:
            if letter is 'e':
                break
            else:
                realPart.append(letter)
        for i in range (formularLen-1,-1,-1):
            if inputFormular[i] is '^':
                break
            else:
                imagePart.append(inputFormular[i])
        imagePart.reverse()
        imagePart.remove('i')
        return {'real':realPart,'img':imagePart}

    elif(getForm(inputFormular) == 'polar'or getForm(inputFormular) == 'general'):
        for letter in inputFormular:
            if letter is '+' or letter is '-':
                break
            else:
                realPart.append(letter)

        for i in range (formularLen-1,-1,-1):
            if inputFormular[i] is '+' or letter is '-':
                if inputFormular[i] is '-':
                    imagePart.append('-')
                break
            else:
                imagePart.append(inputFormular[i])
        imagePart.reverse()
        for i in range(0,len(imagePart)):
            if imagePart[i] == 'i':
                if imagePart[i-1] !='s':
                    del imagePart[i]
        return {'real':realPart,'img':imagePart}
    else:
        return 'wrong input form'

def formTranslation(inputFormular:str,targetForm:str):
    parts = extractParts(inputFormular)
    if targetForm == 'exp':
        if getForm(inputFormular) == 'exp':
            return inputFormular
        real_str = ''.join(parts['real'])
        real = int(real_str)
        img_str = ''.join(parts['img'])
        img = int(img_str)
        if getForm(inputFormular) == 'general':
            moduleArg = polar(complex(real,img))
            resultFormular = str(moduleArg[0]) + 'e^' + str(moduleArg[1]) + 'i'
        elif getForm(inputFormular) == 'polar':
            resultFormular = real_str + 'e^' + img_str + 'i'
        else:
            return 'wrong input form'
        return resultFormular

    elif targetForm == 'polar':
        if getForm(inputFormular) == 'polar':
            return inputFormular
        real_str = ''.join(parts['real'])
        real = int(real_str)
        img_str = ''.join(parts['img'])
        img = int(img_str)
        if getForm(inputFormular) == 'general':
            moduleArg = polar(complex(real,img))
            resultFormular = str(moduleArg[0]) + '(cos ' + str(moduleArg[1]) + ' + sin '+ str(moduleArg[1]) + ' i'
        elif getForm(inputFormular) == 'exp':
            resultFormular = real_str + '(cos ' + img_str + ' + sin '+ img_str + ' i'
        else:
            return 'wrong input form'
        return resultFormular


    elif targetForm == 'general':
        if getForm(inputFormular) == 'general':
            return inputFormular
        real_str = ''.join(parts['real'])
        real = int(real_str)
        img_str = ''.join(parts['img'])
        img = int(img_str)
        resultFormular = str(rect(real,img))
        return resultFormular
    else:
        return 'wrong input form'

print(formTranslation('2+3i','exp'))