from math import *
from cmath import *
from cmath import polar as complexPolar
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

IMAGE_ADDRESS = 'Y:\CN_Explorer\ComplexNumberExplorer\statics\draw\img1.png'
IMG_SIZE = (7.4,5.4)
class FormTranslation:
    @staticmethod
    def list2str(l):
        if l == []:
            return ''
        else:
            str = ''.join(l)
            return str
    @staticmethod
    def list2strPro(complexList):
        for list in range(0,len(complexList)):
            complexList[list] = FormTranslation.list2str(complexList[list])
        return complexList
    @staticmethod
    #accepted input equation and return its type.
    def getForm(inputFormular:str):
        if '^' in inputFormular:
            return 'exp'
        elif 'cos' in inputFormular:
            return 'polar'
        elif 'j' in inputFormular:
            return 'general'
        else:
            return "error input type"
    @staticmethod
    def formTranslation(inputFormular:str,targetForm:str):
        parts = StrPreOperation.extractParts(inputFormular)
        if targetForm == 'exp':
            if FormTranslation.getForm(inputFormular) == 'exp':
                return inputFormular
            real_str = FormTranslation.list2str(parts['real'])
            real = float(real_str)
            img_str = FormTranslation.list2str(parts['img'])
            if FormTranslation.getForm(inputFormular) == 'general':
                img = float(img_str)
                moduleArg = complexPolar(complex(real,img))
                resultFormular = str(moduleArg[0]) + 'e^' + str(moduleArg[1]) + 'j'
            elif FormTranslation.getForm(inputFormular) == 'polar':
                num = ''
                for i in range(0,len(img_str)-1):
                    if img_str[i] == 'p':
                        break
                    num += img_str[i]
                num = float(num)
                img = num*pi
                img_str = str(img)
                resultFormular = real_str + 'e^' + img_str + 'j'
            else:
                return 'wrong input form'
            return resultFormular

        elif targetForm == 'polar':
            if FormTranslation.getForm(inputFormular) == 'polar':
                return inputFormular
            real_str = FormTranslation.list2str(parts['real'])
            real = float(real_str)
            img_str = FormTranslation.list2str(parts['img'])
            if FormTranslation.getForm(inputFormular) == 'general':
                img = float(img_str)
                num = complex(real,img)
                moduleArg = complexPolar(num)
                resultFormular = str(moduleArg[0]) + '(cos ' + str(moduleArg[1]) + ' + sin '+ str(moduleArg[1]) + ' j)'
            elif FormTranslation.getForm(inputFormular) == 'exp':
                num = ''
                for i in range(0,len(img_str)-1):
                    if img_str[i] == 'p':
                        break
                    num += img_str[i]
                num = float(num)
                img = num*pi
                img_str = str(img)                
                resultFormular = real_str + '(cos ' + img_str + ' + sin '+ img_str + ' j'
            else:
                return 'wrong input form'
            return resultFormular


        elif targetForm == 'general':
            if FormTranslation.getForm(inputFormular) == 'general':
                return inputFormular
            real_str = FormTranslation.list2str(parts['real'])
            real = float(real_str)
            img_str = FormTranslation.list2str(parts['img'])
            if 'pi' in img_str:
                num = ''
                for i in range(0,len(img_str)-1):
                    if img_str[i] == 'p':
                        break
                    num += img_str[i]
                num = float(num)
                img = num*pi
            else:
                img = float(img_str)
            resultFormular = rect(real,img)
            resultFormular = complex(round(resultFormular.real,1),round(resultFormular.imag,1))
            return str(resultFormular)
        else:
            return 'wrong input form'
class StrPreOperation:
    '''
        example of outputs:
        2e^3j: {'real':'2','img':'3'}
        3(cos2pi+sin2pij): {'real':"3",'img':"2pi"}
        2+3j: {'real':'2','img':'3'}
    '''
    @staticmethod
    def removeSpaces(string:str):
        if ' ' in string:
            string = string.replace(' ','')
        return string

    @staticmethod
    def extractParts(inputFormular:str):
        StrPreOperation.removeSpaces(inputFormular)
        formularLen = len(inputFormular)
        realPart = []
        imagePart = []
        if(FormTranslation.getForm(inputFormular) == 'exp'):
            for letter in inputFormular:
                if letter is 'e':
                    break
                else:
                    realPart.append(letter)
            realPart = FormTranslation.list2str(realPart)
            for i in range (formularLen-1,-1,-1):
                if inputFormular[i] is '^':
                    break
                else:
                    imagePart.append(inputFormular[i])
            imagePart.reverse()
            imagePart = FormTranslation.list2str(imagePart)
            if 'pi' in imagePart:
                num = ''
                for i in range(0,len(imagePart)-1):
                    if imagePart[i] == 'p':
                        break
                    num += imagePart[i]
                num = float(num)
                imagePart = list(str(num*pi))
            else:
                imagePart = list(imagePart)
            if 'j' in imagePart:
                imagePart.remove('j')
            return {'real':realPart,'img':imagePart}

        elif(FormTranslation.getForm(inputFormular) == 'general'):
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
        elif FormTranslation.getForm(inputFormular) == 'polar':
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
            imagePart.remove('j')
            if ')' in imagePart:
                imagePart.remove(')')
            return {'real':realPart,'img':imagePart}
        else:
            return 'wrong input form'
    @staticmethod
    def equationSeparator(equation:str):
        StrPreOperation.removeSpaces(equation)
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
        rightHandSide=FormTranslation.list2str(rightHandSide)
        rightHandSide = rightHandSide.replace(' ','')
        result = {'leftSide':leftHandSide,'rightSide':rightHandSide}
        return result
    @staticmethod
    def preSideFormular(sideKind:str,formular:str):
        StrPreOperation.removeSpaces(sideKind)
        StrPreOperation.removeSpaces(formular)
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
                        temp = MathOperation.signFiliper(temp)
                    elif formular[i-1] == '*':
                        temp.insert(0,'*')
                    numParts.append(temp)
                    continue
                if formular[j+2] == 'z' and formular[j+1] == '*':
                    if formular[i-1] == '-':
                        temp.insert(0,'-')
                        temp = MathOperation.signFiliper(temp)
                    paraParts.append(temp)
                elif formular[i-2] == 'z' and formular[i-1] == '/':
                    if formular[i-3] == '-':
                        temp.insert(0,'-')
                        temp = MathOperation.signFiliper(temp)
                    temp.insert(0,'1/')
                    paraParts.append(temp)
                elif formular[i-1] == '*':
                    temp.insert(0,'*')
                    numParts.append(temp)
                else:
                    if formular[i-1] == '-':
                        temp.insert(0,'-')
                        temp = MathOperation.signFiliper(temp)
                    numParts.append(temp)
        if paraParts == []:
            for i in range(0,len(formular)):
                if formular[i] == 'z' and formular[i-1] == '-':
                    paraParts.append('-1')
                elif formular[i] == 'z'and formular[i-1] != '*':
                    paraParts.append('1')
        
        result = {sideKind+'ParaList':paraParts,sideKind+'NumList':numParts}
        return result
    @staticmethod
    def extractEquation(equation:str):
        StrPreOperation.removeSpaces(equation)
        modules = []
        index = 0
        for i in range(0,len(equation)):
            if equation[i] == '(':
                modules.append([])
                j=i+1
                while(equation[j] !=')'):
                    modules[index].append(equation[j])
                    j+=1
                index+=1
        modules = FormTranslation.list2strPro(modules)
        for i in range (0,len(modules)):
            if FormTranslation.getForm(modules[i]) != 'general':
                modules[i] = FormTranslation.formTranslation(modules[i],'general')
        return modules

class MathOperation:
    @staticmethod
    def complexAdd(z1:str,z2:str,targetForm):
        z1Form = FormTranslation.getForm(z1)
        z2Form = FormTranslation.getForm(z2)
        if  z1Form is not 'general':
            z1 = FormTranslation.formTranslation(z1,'general')
        elif z2Form is not 'general':
            z2 = FormTranslation.formTranslation(z2,'general')
        z1 = complex(z1)
        z2 = complex(z2)
        result = str(z1 + z2)
        result = result.replace('(','')
        result = result.replace(')','')
        result = FormTranslation.formTranslation(result,targetForm)
        return result
    @staticmethod
    def complexSubtract(z1:str,z2:str,targetForm):
        z1Form = FormTranslation.getForm(z1)
        z2Form = FormTranslation.getForm(z2)
        if z1Form is not 'general':
            z1 = FormTranslation.formTranslation(z1,'general')
        if z2Form != 'general':
            z2 = FormTranslation.formTranslation(z2,'general')
        z1 = complex(z1)
        z2 = complex(z2)
        result = str(z1 - z2)
        result = result.replace('(','')
        result = result.replace(')','')
        result = FormTranslation.formTranslation(result,targetForm)
        return result
    @staticmethod
    def complexMultiple(z1:str,z2:str,targetForm):
        z1Form = FormTranslation.getForm(z1)
        z2Form = FormTranslation.getForm(z2)
        if z1Form is not 'general':
            z1 = FormTranslation.formTranslation(z1,'general')
        if z2Form != 'general':
            z2 = FormTranslation.formTranslation(z2,'general')
        z1 = complex(z1)
        z2 = complex(z2)
        result = str(z1 * z2)
        result = result.replace('(','')
        result = result.replace(')','')
        result = FormTranslation.formTranslation(result,targetForm)
        return result
    @staticmethod
    def complexDivide(z1:str,z2:str,targetForm):
        z1Form = FormTranslation.getForm(z1)
        z2Form = FormTranslation.getForm(z2)
        if z1Form is not 'general':
            z1 = FormTranslation.formTranslation(z1,'general')
        if z2Form != 'general':
            z2 = FormTranslation.formTranslation(z2,'general')
        z1 = complex(z1)
        z2 = complex(z2)
        result = str(z1 / z2)
        result = result.replace('(','')
        result = result.replace(')','')
        result = FormTranslation.formTranslation(result,targetForm)
        return result
    @staticmethod
    def signFiliper(temp:list):
        if temp[1] == '-':
            temp.remove('-')
            temp.remove('-')
        for i in range(1,len(temp)-1):
            if temp[i] == '+':
                temp[i] = '-'
            elif temp[i] == '-':
                temp[i] = '+'
        return temp
    @staticmethod
    def multipleMerge(PartDic:dict):
        for k in PartDic:
            for l in range(0,len(PartDic[k])):
                if '*' in PartDic[k][l]:
                    PartDic[k][l] = PartDic[k][l].replace('*','')
                    PartDic[k][l] = MathOperation.complexMultiple(PartDic[k][l],PartDic[k][l-1],'general')
                    PartDic[k][l-1] = ''
        for k in PartDic:
            if '' in PartDic[k]:
                PartDic[k].remove('')
        return PartDic
    @staticmethod
    def addMerge(PartDic):
        for k in PartDic:
            l = len(PartDic[k])
            while(l > 1):
                PartDic[k][0] = MathOperation.complexAdd(PartDic[k][0],PartDic[k][1],'general')
                del PartDic[k][1]
                l = len(PartDic[k])
        return PartDic
class MathCalculator:
    # equations like: p*z (-/+/*//) (a+bj) = (c+dj)
    #p must be (a+bj) form
    @staticmethod
    def linearEquationSolver(equation:str):
        separator = StrPreOperation.equationSeparator(equation)
        leftSide = separator['leftSide']
        rightSide = separator['rightSide']
        leftPartDic =  StrPreOperation.preSideFormular('left',leftSide)
        rightPartDic = StrPreOperation.preSideFormular('right',rightSide)
        leftPartDic['leftParaList'] = FormTranslation.list2strPro(leftPartDic['leftParaList'])
        leftPartDic['leftNumList'] = FormTranslation.list2strPro(leftPartDic['leftNumList'])
        rightPartDic['rightParaList'] = FormTranslation.list2strPro(rightPartDic['rightParaList'])
        rightPartDic['rightNumList'] = FormTranslation.list2strPro(rightPartDic['rightNumList'])
        leftPartDic = MathOperation.multipleMerge(leftPartDic)
        rightPartDic = MathOperation.multipleMerge(rightPartDic)
        leftPartDic = MathOperation.addMerge(leftPartDic)
        rightPartDic = MathOperation.addMerge(rightPartDic)
        if len(leftPartDic['leftNumList']):
            leftPartDic['leftNumList'][0] = list(leftPartDic['leftNumList'][0])
            leftPartDic['leftNumList'][0].insert(0,'-')
            rightPartDic['rightNumList'].append(FormTranslation.list2str(MathOperation.signFiliper(leftPartDic['leftNumList'][0])))
            del leftPartDic['leftNumList'][0]
            rightPartDic = MathOperation.addMerge(rightPartDic)
        if len(leftPartDic['leftNumList']) != 0 or len(rightPartDic['rightParaList']) != 0:
            print('merge not complete')
            print('leftNumList',leftPartDic['leftNumList'])
            print('rightParaList',rightPartDic['rightParaList'])
            return
        result = MathOperation.complexDivide(rightPartDic['rightNumList'][0],leftPartDic['leftParaList'][0],'general')
        return result

    # only support for formular has this format: (a+bi) (+/-/*/ /) (c+di)*n
    @staticmethod
    def combinedCal(equation:str):
        modules = []
        index = 0
        for i in range(0,len(equation)):
            if equation[i] == '(':
                modules.append([])
                if i-1>=0:
                    modules[index].append(equation[i-1])
                j=i
                while(equation[j] !=')'):
                    modules[index].append(equation[j])
                    j+=1
                index+=1
        length = len(modules)
        modules[0].remove('(')
        while(length !=1 ):
            if modules[1][0] == '(':
                modules[1].remove('(')
            elif modules[1][0] == '-':
                modules[1].remove('(')
                modules[1] = MathOperation.signFiliper(modules[1])
                if i != 0:
                    z1 = FormTranslation.list2str(modules[1])
                    z2 = FormTranslation.list2str(modules[0])
                    modules[1] = list(MathOperation.complexAdd(z1,z2,'general'))
                    modules.pop(0)
            elif modules[1][0] == '+':
                modules[1].remove('+')
                modules[1].remove('(')
                if i != 0:
                    z1 = FormTranslation.list2str(modules[1])
                    z2 = FormTranslation.list2str(modules[0])
                    modules[1] = list(MathOperation.complexAdd(z1,z2,'general'))
                    modules.pop(0)
            elif modules[1][0] == '*':
                modules[1].remove('*')
                modules[1].remove('(')
                if i != 0:
                    z1 = FormTranslation.list2str(modules[1])
                    z2 = FormTranslation.list2str(modules[0])
                    if z2[0] == '-' and z2[1] == '-':
                        z2 = FormTranslation.list2str (MathOperation.signFiliper(list(z2)))
                    modules[1] = list(MathOperation.complexMultiple(z1,z2,'general'))
                    modules.pop(0)
            elif modules[1][0] == '/':
                modules[1].remove('/')
                modules[1].remove('(')
                if i != 0:
                    z1 = FormTranslation.list2str(modules[1])
                    z2 = FormTranslation.list2str(modules[0])
                    modules[1] = list(MathOperation.complexDivide(z1,z2,'general'))
                    modules.pop(0)
            length = len(modules)
        return(FormTranslation.list2str(modules[0]))

class Graph():
    @staticmethod
    def plotAxis(axisLen):
        plt.xlabel('real')
        plt.ylabel('image')
        plt.grid(True)
        plt.xlim(min(-axisLen,axisLen),max(-axisLen,axisLen))
        plt.ylim(min(-axisLen,axisLen),max(-axisLen,axisLen))
        plt.quiver(-axisLen,0,axisLen,0,scale = 0.5,scale_units = 'xy', angles = 'xy')
        plt.quiver(0,-axisLen,0,axisLen,scale = 0.5,scale_units = 'xy', angles = 'xy')
    # (a+bj) +, -, *, / (c+dj)
    @staticmethod
    def plotForCombinedCal(equation:str):
        nums = StrPreOperation.extractEquation(equation)
        nums = FormTranslation.list2strPro(nums)
        nums.append(MathCalculator.combinedCal(equation))
        Graph.plotForNums(nums)
    # ['a + bj','c + dj']
    @staticmethod
    def plotForNums(nums:list):
        plt.figure(figsize=IMG_SIZE)
        maxLen = -9999999
        for num in nums:
            parts = StrPreOperation.extractParts(num)
            real = float(FormTranslation.list2str(parts['real']))
            img = float(FormTranslation.list2str(parts['img']))
            x = real
            y = img
            if max(abs(x),abs(y)) > maxLen:
                maxLen = max(abs(x),abs(y))
            plt.quiver(0,0,x,y,scale = 1,scale_units = 'xy', angles = 'xy')
            plt.text(x,y,str(real)+'+'+str(img)+'j')
        axisLen = maxLen*2
        Graph.plotAxis(axisLen)
        plt.savefig(IMAGE_ADDRESS)
    #|z-(a+bj)| = r, |z-(a+bj)| = |z-(c+dj)|, arg[z-(a+bj)] = a*pi, # equations like: p*z (-/+/*//) (a+bj) = (c+dj),p must be (a+bj) form
    @staticmethod
    def plotForEquation(equation:str):
        sides = StrPreOperation.equationSeparator(equation)
        leftSide = sides['leftSide']
        rightSide = sides['rightSide']
        if 'arg' in leftSide or '|' in leftSide:
            Graph.plotForAbsEquation(equation)
        else:
            ans = MathCalculator.linearEquationSolver(equation)
            Graph.plotForNums([ans])
    # |z-(a+bj)| = r, |z-(a+bj)| = |z-(c+dj)|, arg[z-(a+bj)] = a*pi
    @staticmethod
    def plotForAbsEquation(equation:str):
        sides = StrPreOperation.equationSeparator(equation)
        leftSide = sides['leftSide']
        rightSide = sides['rightSide']
        if '|' in rightSide:
            plt.figure(figsize=IMG_SIZE)
            leftPoint = StrPreOperation.extractEquation(leftSide)
            rightPoint = StrPreOperation.extractEquation(rightSide)
            leftParts = StrPreOperation.extractParts(FormTranslation.list2str(leftPoint[0]))
            rightParts = StrPreOperation.extractParts(FormTranslation.list2str(rightPoint[0]))
            x1 = FormTranslation.list2str(leftParts['real'])
            if '(' in x1:
                x1 = x1.replace('(','') 
            x1 = float(x1)
            y1 = FormTranslation.list2str(leftParts['img'])
            if ')' in y1:
                y1 = y1.replace(')','') 
            y1 = float(y1)
            x2 = FormTranslation.list2str(rightParts['real'])
            if '(' in x2:
                x2 = x2.replace('(','') 
            x2 = float(x2)
            y2 = FormTranslation.list2str(rightParts['img'])
            if ')' in y2:
                y2 = y2.replace(')','') 
            y2 = float(y2)
            axisLen = max((abs(x2-x1)),abs(y2-y1))*5
            gradient = (y2-y1)/(x2-x1)
            lineX = np.linspace(x1,x2)
            lineY = gradient*lineX + (y2-gradient*x2)
            verticalG = -1/gradient
            midX= (x1+x2)/2 
            midY= (y1+y2)/2 
            verticalX = np.linspace(-10000,10000)
            verticalY = verticalG*verticalX + midY - verticalG*midX
            Graph.plotAxis(axisLen)
            plt.plot(x1,y1,'.r')
            plt.text(x1,y1,FormTranslation.list2str(leftPoint[0]))
            plt.text(x2,y2,FormTranslation.list2str(rightPoint[0]))
            plt.plot(x2,y2,'.r')
            plt.plot(lineX,lineY,'g--')
            plt.plot(verticalX,verticalY)
            plt.savefig(IMAGE_ADDRESS)
        elif 'pi' in rightSide:
            plt.figure(figsize=IMG_SIZE)
            leftPoint = StrPreOperation.extractEquation(leftSide)
            leftParts = StrPreOperation.extractParts(FormTranslation.list2str(leftPoint[0]))
            rightParts = rightSide
            x = FormTranslation.list2str(leftParts['real'])
            if '(' in x:
                x = x.replace('(','')
            x = float(x)
            y = FormTranslation.list2str(leftParts['img'])
            if ')' in y:
                y = y.replace(')','') 
            y = float(y)
            axisLen = max((abs(x)),abs(y))*5
            paraX = np.linspace(x,10000)
            paraY = y + paraX*0
            i=0
            piPara = ''
            while rightParts[i] != '*':
                piPara += rightParts[i]
                i+=1
            piPara = float(piPara)
            gradient = tan(piPara*pi)
            angleX = np.linspace(x,10000)
            angleY = gradient*angleX + y - gradient*x
            Graph.plotAxis(axisLen)
            plt.plot(x,y,'.r')
            plt.plot(paraX,paraY,'g--')
            plt.plot(angleX,angleY)
            plt.text(x,y,str(piPara)+'*pi')
            plt.savefig(IMAGE_ADDRESS)
        else:
            leftPoint = StrPreOperation.extractEquation(leftSide)
            leftParts = StrPreOperation.extractParts(FormTranslation.list2str(leftPoint[0]))
            rightParts = float(rightSide)
            x = FormTranslation.list2str(leftParts['real'])
            if '(' in x:
                x = x.replace('(','')
            x = float(x)
            y = FormTranslation.list2str(leftParts['img'])
            if ')' in y:
                y = y.replace(')','') 
            y = float(y)
            radius = rightParts
            axisLen = abs(radius)+abs(y*1.25)
            CircleX = CircleY = np.arange(-radius,radius,0.1)
            CircleX, CircleY = np.meshgrid(CircleX, CircleY)
            figure, axes = plt.subplots(figsize = IMG_SIZE)
            paraX = np.linspace(x,x+radius)
            paraY = y + paraX*0
            Graph.plotAxis(axisLen)
            plt.plot(x,y,'.r')
            plt.text(x,y,FormTranslation.list2str(leftPoint[0]))
            c = plt.Circle((x,y),radius,fill = False)
            axes.add_artist(c)
            axes.set_aspect(1)
            plt.plot(paraX,paraY,'g--')
            plt.text(x+radius/2,y,str(radius))
            plt.savefig(IMAGE_ADDRESS)
#Graph.plotForEquation('|z-(2+3j)| = 5')
#Graph.plotForEquation('|z - (3e^0.2pij)| = |z-(3e^2pij)|')
#Graph.plotForEquation('arg[z-(3e^0.2pij)] = 0.3*pi')
#Graph.plotForEquation('- (1+2j) *z-(3+4j)=(3e^0.8pij))')
#Graph.plotForNums(['1+2j','3e^0.2pij'])
print(MathCalculator.linearEquationSolver('- (1+2j) *z-(3+4j)=(3e^0.6pij)'))
print(MathCalculator.combinedCal('(9+23j)*(-5+8j)'))
#Graph.plotForCombinedCal('(21-7j)/(-2e^3j)')
#print(StrPreOperation.extractEquation('(2+3j) + (2e^3j)'))
#print(FormTranslation.formTranslation('3e^0.2pij','polar'))
#print(FormTranslation.formTranslation('3e^0.2pij','general'))
#print(FormTranslation.formTranslation('3+2j','exp'))