from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from ComplexNumberExplorer.ComplexNumberAlgorithms import *
from CNExplorer.models import Question


def home(request):
    if request.method == 'POST':
        eq = request.POST.get('input')
        Graph.plotForEquation(eq)
        return redirect('/home/')
    return render(request, 'home.html')


def loginSignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'studentAdmin' and password == '123':
            return redirect('/quizlist/')
        elif username == 'teacherAdmin' and password == '456':
            return redirect('/teacherclasses/')
    return render(request, 'loginSignUp.html')


def logout(request):
    return render(request, "home.html", {"msg":u"Logout Successfuly", })


def CreateQuiz(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        if question == '' or answer == '' or (':' not in question):
            return render(request, 'CreateQuiz.html', {'warning': 'invalid input!'})
        description, equation = question.split(':')
        Q = Question()
        Q.content = description
        Q.equation = equation
        Q.answer = answer
        Q.save()
    return render(request, 'CreateQuiz.html')


def error404(request):
    return render(request, 'error404.html')


def error500(request):
    return render(request, 'error500.html')


def TakingQuizv2(request):
    return render(request, 'TakingQuizv2.html')


def TeacherClasses(request):
    return render(request, 'TeacherClasses.html')


def Quizhistory(request):
    return render(request, 'QuizHistory.html')


def Register(request):
    return render(request, 'register.html')


def QuizList(request):
    return render(request, 'QuizList.html')
   