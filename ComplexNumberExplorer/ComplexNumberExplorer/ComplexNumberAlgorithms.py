from math import acos,asin
from cmath import * 
import matplotlib.pyplot as plt
import numpy as np
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
    if l == []:
        return ''
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

def equationSeparator(equation:str):
    leftHandSide = ''
    rightHandSide = []
    for letter in equation:
        if letter == '=':
            break
        else:
            leftHandSide += letter
    leftHandSide = leftHandSide.replace(' ','')
    for i in range(len(equation)-1,0,-1):
        if equation[i] == '=':
            break
        else:
            rightHandSide.append(equation[i])
    rightHandSide.reverse()
    rightHandSide=list2str(rightHandSide)
    rightHandSide = rightHandSide.replace(' ','')
    result = {'leftSide':leftHandSide,'rightSide':rightHandSide}
    return result

def signFiliper(temp):
    if temp[1] == '-':
        temp.remove('-')
        temp.remove('-')
    for i in range(1,len(temp)-1):
        if temp[i] == '+':
            temp[i] = '-'
        elif temp[i] == '-':
            temp[i] = '+'
    return temp

def preSideFormular(sideKind,formular):
    numParts = []
    paraParts = []
    for i in range (0,len(formular)-1):
        temp = []
        if formular[i] == '(':
            j=i+1
            while(formular[j]!=')'):
                temp.append(formular[j])
                j+=1
            if j+2 > len(formular):
                if formular[i-1] == '-':
                    temp.insert(0,'-')
                    temp = signFiliper(temp)
                elif formular[i-1] == '*':
                    temp.insert(0,'*')
                numParts.append(temp)
                continue
            if formular[j+2] == 'z' and formular[j+1] == '*':
                if formular[i-1] == '-':
                    temp.insert(0,'-')
                    temp = signFiliper(temp)
                paraParts.append(temp)
            elif formular[i-2] == 'z' and formular[i-1] == '/':
                if formular[i-3] == '-':
                    temp.insert(0,'-')
                    temp = signFiliper(temp)
                temp.insert(0,'1/')
                paraParts.append(temp)
            elif formular[i-1] == '*':
                temp.insert(0,'*')
                numParts.append(temp)
            else:
                if formular[i-1] == '-':
                    temp.insert(0,'-')
                    temp = signFiliper(temp)
                numParts.append(temp)
    if paraParts == []:
        for i in range(0,len(formular)):
            if formular[i] == 'z' and formular[i-1] == '-':
                paraParts.append('-1')
            elif formular[i] == 'z':
                paraParts.append('1')
    result = {sideKind+'ParaList':paraParts,sideKind+'NumList':numParts}
    return result

def Listlist2ListStr(partDic):
    for k in partDic:
        for i in range (0,len(partDic[k])):
            partDic[k][i] = list2str(partDic[k][i])
    return partDic

def multipleMerge(PartDic):
    for k in PartDic:
        for l in range(0,len(PartDic[k])):
            if '*' in PartDic[k][l]:
                PartDic[k][l] = PartDic[k][l].replace('*','')
                PartDic[k][l] = complexMultiple(PartDic[k][l],PartDic[k][l-1],'general')
                PartDic[k][l-1] = ''
    for k in PartDic:
        if '' in PartDic[k]:
            PartDic[k].remove('')
    return PartDic

def addMerge(PartDic):
    for k in PartDic:
        l = len(PartDic[k])
        while(l > 1):
            PartDic[k][0] = complexAdd(PartDic[k][0],PartDic[k][1],'general')
            del PartDic[k][1]
            l = len(PartDic[k])
    return PartDic
# equations like: p1z -/+/*// (a+bi) = (c+di)
def linearEquationSolver(equation:str):
    separator = equationSeparator(equation)
    leftSide = separator['leftSide']
    rightSide = separator['rightSide']
    leftPartDic =  preSideFormular('left',leftSide)
    rightPartDic = preSideFormular('right',rightSide)
    leftPartDic = Listlist2ListStr(leftPartDic)
    rightPartDic = Listlist2ListStr(rightPartDic)
    leftPartDic = multipleMerge(leftPartDic)
    rightPartDic = multipleMerge(rightPartDic)
    leftPartDic = addMerge(leftPartDic)
    rightPartDic = addMerge(rightPartDic)
    if len(leftPartDic['leftNumList']):
        leftPartDic['leftNumList'][0] = list(leftPartDic['leftNumList'][0])
        leftPartDic['leftNumList'][0].insert(0,'-')
        rightPartDic['rightNumList'].append(list2str(signFiliper(leftPartDic['leftNumList'][0])))
        leftPartDic['leftNumList'][0].clear()
        rightPartDic = addMerge(rightPartDic)
    if len(leftPartDic['leftNumList']) != 0 or len(rightPartDic['rightParaList']) != 0:
        print('merge not complete')
        print('leftNumList',leftPartDic['leftNumList'])
        print('rightParaList',rightPartDic['rightParaList'])
        return
    result = complexDivide(rightPartDic['rightNumList'][0],leftPartDic['leftParaList'][0],'general')
    return result
# +, -, *, /
def coordinatesGeneratorForSimpleCal(equation:str):
    pass
# a + bj
def coordinatesGeneratorForSingleNum(num:str):
    parts = extractParts(num)
    real = float(list2str(parts['real']))
    img = float(list2str(parts['img']))
    x = real
    y = img
    axisLen = max(abs(x),abs(y))*2
    plt.xlabel('real')
    plt.xlim(min(-axisLen,axisLen),max(-axisLen,axisLen))
    plt.ylabel('image')
    plt.ylim(min(-axisLen,axisLen),max(-axisLen,axisLen))
    plt.title(num)
    plt.grid(True)
    plt.quiver(0,0,x,y,scale = 1,scale_units = 'xy', angles = 'xy')
    plt.show()
#print(linearEquationSolver('-(1+2j)*z=-(1+2j)*(3+4j)'))
coordinatesGeneratorForSingleNum('-2+4j')