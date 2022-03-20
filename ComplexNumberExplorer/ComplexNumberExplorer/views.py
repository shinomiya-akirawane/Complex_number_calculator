from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request):
    return render(request, 'home.html')


def loginSignUp(request):
    return render(request, 'loginSignUp.html')


def CreateQuiz(request):
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
