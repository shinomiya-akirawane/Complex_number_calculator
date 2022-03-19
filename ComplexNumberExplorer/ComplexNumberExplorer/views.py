from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
def home(request):
    return render(request,'home.html')

def loginSignUp(request):
    return render(request,'loginSignUp.html')

def CreateQuiz(request):
    return render(request,'CreateQuiz.html')

def error404(request):
    return render(request,'error404.html')

def error500(request):
    return render(request,'error500.html')

def TakingQuiz(request):
    return render(request,'TakingQuiz.html')

def TeacherClasses(request):
    return render(request,'TeacherClasses.html')

def Quizhistory(request):
    return render(request,'QuizHistory.html')

