from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
def home(request):
    return render(request,'home.html')

def loginSignUp(request):
    return render(request,'loginSignUp.html')

def AddNewQuiz(request):
    return render(request,'AddNewQuize.html')