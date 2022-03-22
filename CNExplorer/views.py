from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from ComplexNumberExplorer.ComplexNumberAlgorithms import *
from CNExplorer.models import CandidateResult, PaperList, Question, Groups, QuestionDatabase, usersprofile
import random


def home(request):
    if request.method == 'POST':
        eq = request.POST.get('input')
        if '=' in eq:
            Graph.plotForEquation(eq)
        elif '*' in eq:
            Graph.plotForCombinedCal(eq)
        else:
            Graph.plotForNums([eq])
        picturePath = '/static/draw/img1.png'
        return render(request, 'home.html', {'picturePath': picturePath, 'input': eq})
    return render(request, 'home.html', {'picturePath': '/static/draw/home_origin.png'})


def loginSignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        U = usersprofile.objects.get(name=username)
        if password == U.password and U.usertype == 'Student':
            return redirect('/quizlist/')
        elif password == U.password and U.usertype == 'Teacher':
             return redirect('/teacherclasses/')
        elif username == 'studentAdmin' and password == '123':
            return redirect('/quizlist/')
        elif username == 'teacherAdmin' and password == '456':
            return redirect('/teacherclasses/')
    return render(request, 'loginSignUp.html')


def logout(request):
    return render(request, "home.html", {"msg":u"Logout Successfuly", })


def CreateQuiz(request):
    question=''
    answer=''
    quizID = request.GET.get('quizID')
    questionID = request.GET.get('id')
    print(questionID)
    if int(questionID) % 5 == 0:
        questionNumber = 5
    else:
        questionNumber = int(questionID) % 5
    Q = Question(id=questionID)
    Q.save()
    Q1 = Question.objects.get(id=questionID)
    nextQuestionID = Q1.id + 1
    print(Q1.id)
    G = Groups.objects.get(id=1)
    
    
    
    if int(questionID)%5 == 0:
        #if int(questionID) == 5:
        nextLink = '/teacherquizlist/?newQuizID=' + str(quizID)
        next = 'Finish'
        PL = PaperList()
        PL.id = quizID
        PL.groupNum = G
        PL.is_allow = 0
        PL.save()
    else:
        nextLink = '/newQuiz/?quizID='+ str(quizID) + '&id=' + str(nextQuestionID)
        next = 'Next'
        print(nextLink)
    
    if request.GET.get('auto_generate') == 'true':
        Q2 = QuestionDatabase.objects.get(id=random.randint(1,20))
        question = Q2.content + ': ' + Q2.equation
        answer = Q2.answer
    else: 
        Q3 = Question.objects.get(id=questionID)
        question = Q3.content + ': ' + Q3.equation
        answer = Q3.answer
        
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        #checking invalid
        if question == '' or answer == '' or (':' not in question):
            warning = 'Invalid input!'
        #create a question object and store in db
        description, equation = question.split(':')
        Q = Question.objects.get(id=questionID)
        Q.content = description
        Q.equation = equation
        Q.answer = answer
        Q.save()
    print(questionID)
 
    return render(request, 'CreateQuizv2.html', {'question': question, 'answer': answer, 'nextLink': nextLink, 'next': next, 'questionID': questionID, 'questionNumber': questionNumber, 'quizID': quizID, 'nextQuestionID': nextQuestionID})


def error404(request):
    return render(request, 'error404.html')


def error500(request):
    return render(request, 'error500.html')


def TakingQuizv2(request):
    result = ''
    answer=''
    quizID = request.GET.get('quizID')
    questionID = request.GET.get('id')
    Q = Question.objects.get(id=questionID)
    Qcontent = Q.content
    Qequation = Q.equation
    Qanswer = Q.answer
    nextQuestionID = Q.id + 1
    PL = PaperList.objects.get(id=quizID)
    
    if int(questionID) % 5 == 0:
        questionNumber = 5
    else:
        questionNumber = int(questionID) % 5
    
    if int(questionID)%5 == 0:
        nextLink = '/quizlist/'
        next = 'Finish'
        PL.is_allow = 1
        PL.save()
    else:
        nextLink = '/takingquiz/?quizID='+ str(quizID) + '&id=' + str(nextQuestionID)
        next = 'Next'
        print(nextLink)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        
        CR = CandidateResult()
        CR.id = questionID
        CR.answer = answer
        CR.paper = PL
        CR.question = Q
        CR.user=usersprofile.objects.get(id=1)
        CR.save()
        
        if answer == Qanswer:
            result = 'Correct!'
        else:
            result = 'Incorrect!'
    return render(request, 'TakingQuizv2.html', {'next': next, 'quizID': quizID, 'questionID': questionID, 'questionNumber': questionNumber, 'Qcontent': Qcontent, 'Qequation': Qequation, 'Qanswer': Qanswer, 'result': result, 'nextLink': nextLink, 'answer': answer })


def TeacherClasses(request):
    return render(request, 'TeacherClasses.html')


def Quizhistory(request):
    quizID = request.GET.get('quizID')
    questionID = request.GET.get('id')
    
    PL = PaperList.objects.get(id=quizID)
    
    CR = CandidateResult.objects.get(id=questionID)
    CRanswer = CR.answer
    
    if int(questionID) % 5 == 0:
        questionNumber = 5
    else:
        questionNumber = int(questionID) % 5
    
    Q = Question.objects.get(id=questionID)
    Qcontent = Q.content
    Qequation = Q.equation
    Qanswer = Q.answer
    nextQuestionID = Q.id + 1
    
    if int(questionID)%5 == 0:
        nextLink = '/quizlist/'
        next = 'Finish'
    else:
        nextLink = '/quizhistory/?quizID='+ str(quizID) + '&id=' + str(nextQuestionID)
        next = 'Next  Question ->'
    
    if '=' in Qequation:
        Graph.plotForEquation(Qequation)
    elif '*' in Qequation:
        Graph.plotForCombinedCal(Qequation)
    else:
        Graph.plotForNums([Qequation])
    picturePath='/static/draw/img1.png'
    return render(request, 'quizHistoryv1.html', {'questionNumber': questionNumber, 'next': next, 'nextLink': nextLink, 'Qcontent': Qcontent, 'Qequation': Qequation, 'Qanswer': Qanswer, 'CRanswer': CRanswer, 'quizID': quizID, 'questionID': questionID, 'nextQuestionID': nextQuestionID, 'picturePath': picturePath})


def Register(request):
    if request.method == 'POST':
        GP = Groups()
        GP.id = 1
        GP.groupName = 'CN1'
        GP.groupCode = 1
        GP.save()
        username = request.POST.get('username')
        password = request.POST.get('password')
        Cpassword = request.POST.get('cpassword')
        if password != Cpassword:
            return redirect('/register/')
        usertype = request.POST.get('userType')
        email = request.POST.get('email')
        groupNumber = request.POST.get('groupNumber')
        USER = usersprofile()
        USER.name = username
        USER.password = password
        USER.usertype = usertype
        USER.emailAddress = email
        USER.groupNum = GP
        USER.save()

        return redirect('/login/')
    return render(request, 'register.html')


def QuizList(request):
    
    isAttempt=[]
    statuses=[]
    for i in range(1, 5):
        PL = PaperList.objects.get(id=i)
        isAttempt.append(PL.is_allow)
    statusRel = {False: 'Not Answered', True: 'Answered'}
    for attempt in isAttempt:
        statuses.append(statusRel[attempt])
    status = ''

    return render(request, 'QuizList.html', {'quiz_1_status': statuses[0], 'quiz_2_status': statuses[1], 'quiz_3_status': statuses[2], 'quiz_4_status': statuses[3]})


def teacherQuizList(request):
    newQuizID = request.GET.get('newQuizID')
    if newQuizID != None:
        PaperList.objects.get(id=newQuizID).is_allow = 0
    return render(request, 'TeacherQuizList.html')