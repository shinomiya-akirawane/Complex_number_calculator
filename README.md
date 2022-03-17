# Complex_number_calculator
A group repository for ENGF0002 

#### Project Strcuture

The structure of the project follows **MVT(Models,Views,templates)** structure
models.py contains the processor of data from database 
views.py contains main logic algorithms 
templates.py contains all html pages

For example:
To realize a log-in page:
 1. Client send log-in information to **View**
 2. **View** send the data to **Model**
 3. **Model** re-mat the data and send it to database to save
 4. Database return the result of saving data to **Model**
 5. **Model** send the result to **View**
 6. **View** request corresponding html page from **Template**
 7. **Template** send page to **View**
 8. **View** send page to Client

#### Variable and functions name Rules
The variable name should follow camel rules. Meaningless name is strictly banned, such as x,y,z
e.g. currentNum

The function name should follow camel rules,too. Aiming to be readable to others.
#### Frames used 
Bootstrap + Django

#### Tasks 

 - **Xinyu, Hou:** Templates genrated by Bootstrap
 - **TianXiang, Xiong:** Model + SQL
 - **Yuhang, Zhou:** urls
 - **Zhaoyan, Dong:** View

#### algorithm library APIs instruction

There are 5 classes:
- Graph: contains plotting functions 
- FormTranslation: contains form translating functions
- MathOperation: contains + - * / functions
- StrPreOperation: contains string pretreatment functions
- MathCalculator: equation solver and conbinedCalculation 
  
##### Graph Class
**plotAxis(axisLen):** float -> graph
 *plot empty graph with axis*

**plotForCombinedCal(equation):** str -> graph
====equation format: #03A9F4== #F44336== [ (a+bj) (+, -, *, /) (c+dj) ] *n
*plot graph with axis showing both the complex numbers in the formular and the answer*

**plotForNums(equation):** list[str] -> graph
====equation format: #03A9F4== #F44336== [ 'a+bj', 'c+dj'... ]
*plot graph with axis showing the complex numbers in the list*

**plotForEquation(equation):** str -> graph
====equation format: #03A9F4== #F44336== z-(a+bj)|=r, |z-(a+bj)| = |z-(c+dj)|. arg[z-(a+bj)] = a*pi, p*z (-, +, *, /) (a+bj) = (c+dj), p **must** be (e+fj) form
*plot graph with axis showing the answer to the equation*

**plotForAbsEquation(equation):** str -> graph
====equation format: #03A9F4== #F44336== z-(a+bj)|=r, |z-(a+bj)| = |z-(c+dj)|. arg[z-(a+bj)] = a*pi 
*plot graph with axis showing the answer to equations with **abs sign** and **arg sign***

##### Form Translation
**list2str(l):** list -> str
**list2strPro(complexList):** list[list] -> list[str]
**getForm(inputFormular):** str -> str
==inputFormular format: #03A9F4== 2e^3j, 3cos2pi+4sinn2pij, 2+3j
*return the form of input formular, the form can be: ''general, 'polar', 'exp'*
**formTranslation(inputFormular,targetForm):** str,str -> str  
==inputFormular format: #03A9F4== 2e^3j, 3cos2pi+4sinn2pij, 2+3j
*return a formular of targetForm*

##### StrPreOperation
**extractParts(inputFormular):** str-> dict
==inputFormular format: #03A9F4== 2e^3j, 3cos2pi+4sinn2pij, 2+3j
==output format: #03A9F4== {'real': , 'img': }

**equationSeparator:** str -> dict
==inputFormular format: #03A9F4== ... = ...
==output format: #03A9F4== {'leftSidel': , 'rightSide': }

**preSideFormular(sindKind, formular):** str,str -> dict
==inputFormular format: #03A9F4==  [ (a+bj) (+, -, *, /) (c+dj) ] *n
==output format: #03A9F4== {'left or right ParaList': , 'left or right NumList': }

**extractEquation(equation):** str-> list(list)
==equation format: #03A9F4==  [ (a+bj) (+, -, *, /) (c+dj) ] *n
==output format: #03A9F4== [ (a+bi), (c+di), ... ]

##### MathOperation
**complexAdd(z1,z2,targetForm):** str,str,str -> str
**complexSubtract(z1,z2,targetForm):** str,str,str -> str
**complexMultiple(z1,z2,targetForm):** str,str,str -> str
**complexDivide(z1,z2,targetForm):** str,str,str -> str
**signFiliper(temp):** list -> list
*return a formular that the sign has been filiper. for example: -(a+bj) -> -a-bj*
**multipleMerge(PartDic):** dict -> dict
*return a dictionary that all multiple terms are merged.(a+bj) * (c+dj) -> (e+hj)*
**addMerge(PartDic):** dict -> dict
*return a dictionary that all multiple terms are merged.(a+bj) + (c+dj) -> (e+hj)*

#### MathCalculator
**linearEquationSolver(equation):** str -> str
==equation format: #03A9F4== p*z (-, +, *, /) (a+bj) = (c+dj), p must be (a+bj) form
*return a answer to linear equation*

**combindCal(equation):** str -> str
==equation format: #03A9F4== (c+dj) (-, +, *, /) (a+bj)