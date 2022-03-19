from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def home(request):
    if request.method == 'POST':
        input = request.POST.get('input')
        print(input)
        return redirect('/home/')
    return render(request, 'home.html')


def loginSignUp(request):
    return render(request, 'loginSignUp.html')


def addNewQuiz(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        print(question)
        print(answer)
        return redirect('/addNewQuiz/')
    return render(request, 'addNewQuiz.html')


def studentQuiz(request):
    return render(request, 'studentQuiz.html')


def quiz(request):
    return render(request, 'quiz.html')