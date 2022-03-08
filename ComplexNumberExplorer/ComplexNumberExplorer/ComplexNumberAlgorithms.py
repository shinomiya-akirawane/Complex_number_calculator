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
    elif 'j' in inputFormular:
        return 'general'
    else:
        return "error input type"

def list2str(l):
    str = ''.join(l)
    return str
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
        imagePart.remove('j')
        return {'real':realPart,'img':imagePart}

    elif(getForm(inputFormular) == 'general'):
        if inputFormular[0] == '-':
            realPart.append('-')
            inputFormular = inputFormular.replace('-','',1)
        for letter in inputFormular:
            if letter is '+' or letter is '-':
                break
            else:
                realPart.append(letter)

        for i in range (len(inputFormular)-1,-1,-1):
            if inputFormular[i] is '+' or inputFormular[i] is '-':
                if inputFormular[i] is '-':
                    imagePart.append('-')
                break
            else:
                imagePart.append(inputFormular[i])
        imagePart.reverse()
        imagePart.remove('j')
        return {'real':realPart,'img':imagePart}
    elif getForm(inputFormular) == 'polar':
        for letter in inputFormular:
            if letter is '(':
                break
            else:
                realPart.append(letter)

        for i in range (formularLen-1,-1,-1):
            if inputFormular[i] == 'n':
                break
            else:
                imagePart.append(inputFormular[i])
        imagePart.reverse()
        imagePart.remove(')')
        return {'real':realPart,'img':imagePart}
    else:
        return 'wrong input form'

def formTranslation(inputFormular:str,targetForm:str):
    parts = extractParts(inputFormular)
    if targetForm == 'exp':
        if getForm(inputFormular) == 'exp':
            return inputFormular
        real_str = list2str(parts['real'])
        real = float(real_str)
        img_str = list2str(parts['img'])
        img = float(img_str)
        if getForm(inputFormular) == 'general':
            moduleArg = polar(complex(real,img))
            resultFormular = str(moduleArg[0]) + 'e^' + str(moduleArg[1]) + 'j'
        elif getForm(inputFormular) == 'polar':
            resultFormular = real_str + 'e^' + img_str + 'j'
        else:
            return 'wrong input form'
        return resultFormular

    elif targetForm == 'polar':
        if getForm(inputFormular) == 'polar':
            return inputFormular
        real_str = list2str(parts['real'])
        real = float(real_str)
        img_str = list2str(parts['img'])
        img = float(img_str)
        if getForm(inputFormular) == 'general':
            moduleArg = polar(complex(real,img))
            resultFormular = str(moduleArg[0]) + '(cos ' + str(moduleArg[1]) + ' + sin '+ str(moduleArg[1]) + ' j)'
        elif getForm(inputFormular) == 'exp':
            resultFormular = real_str + '(cos ' + img_str + ' + sin '+ img_str + ' j'
        else:
            return 'wrong input form'
        return resultFormular


    elif targetForm == 'general':
        if getForm(inputFormular) == 'general':
            return inputFormular
        real_str = list2str(parts['real'])
        real = float(real_str)
        img_str = list2str(parts['img'])
        img = float(img_str)
        resultFormular = str(rect(real,img))
        return resultFormular
    else:
        return 'wrong input form'

def complexAdd(z1:str,z2:str,targetForm):
    z1Form = getForm(z1)
    z2Form = getForm(z2)
    if  z1Form is not 'general':
        z1 = formTranslation(z1,'general')
    elif z2Form is not 'general':
        z2 = formTranslation(z2,'general')
    z1 = complex(z1)
    z2 = complex(z2)
    result = str(z1 + z2)
    result = result.replace('(','')
    result = result.replace(')','')
    result = formTranslation(result,targetForm)
    return result

def complexSubtract(z1:str,z2:str,targetForm):
    z1Form = getForm(z1)
    z2Form = getForm(z2)
    if z1Form is not 'general':
        z1 = formTranslation(z1,'general')
    if z2Form != 'general':
        z2 = formTranslation(z2,'general')
    z1 = complex(z1)
    z2 = complex(z2)
    result = str(z1 - z2)
    result = result.replace('(','')
    result = result.replace(')','')
    result = formTranslation(result,targetForm)
    return result

def complexMultiple(z1:str,z2:str,targetForm):
    z1Form = getForm(z1)
    z2Form = getForm(z2)
    if z1Form is not 'general':
        z1 = formTranslation(z1,'general')
    if z2Form != 'general':
        z2 = formTranslation(z2,'general')
    z1 = complex(z1)
    z2 = complex(z2)
    result = str(z1 * z2)
    result = result.replace('(','')
    result = result.replace(')','')
    result = formTranslation(result,targetForm)
    return result

def complexDivide(z1:str,z2:str,targetForm):
    z1Form = getForm(z1)
    z2Form = getForm(z2)
    if z1Form is not 'general':
        z1 = formTranslation(z1,'general')
    if z2Form != 'general':
        z2 = formTranslation(z2,'general')
    z1 = complex(z1)
    z2 = complex(z2)
    result = str(z1 / z2)
    result = result.replace('(','')
    result = result.replace(')','')
    result = formTranslation(result,targetForm)
    return result
