from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect


# 网站主页
def homepage(request):
    if request.method == "POST":
        equation = request.POST.get()
        print(equation)
        return redirect('/')

    return render(request, 'homepage.html')


# 登录界面
def login(request):
    error_msg = ''

    if request.method == "POST":

        user = request.POST.get('user', None)  # 避免提交空，时异常

        user = user.strip()  # 用户输入末尾有空格是去空格

        pwd = request.POST.get('pwd', None)

        if user == "root" and pwd == "123":

            print('user=' + user, 'pwd=' + pwd)

            return redirect("/quiz_list/")

        else:

            error_msg = "账号或者密码不对"

            print('user=' + user, 'pwd=' + pwd)

    return render(request, 'login.html', {'error_msg': error_msg})


def register(request):
    if request.method == "POST":
        return redirect('/quiz_list/')
    return render(request, 'register.html')


######################################################################

# 题目列表
def quiz_list(request):
    quizzes = {'1': 'calculate 1+1', '2': 'calculate 8-2'}
    return render(request, 'quiz_list.html', {'quizzes': quizzes})


# 单个题目
def quiz(request):
    if request.method == "POST":
        answer = request.POST.get('answer')
        if answer == '2':
            return render(request, 'quiz.html', {'result': 'Correct!'})
        else:
            return render(request, 'quiz.html', {'result': 'Incorrect!'})
    else:
        return render(request, 'quiz.html')


def directRegister(request):
    print(request.GET.items)
    if request.method == "POST":
        return render(request, 'login.html')


def registerView(request):
    error_msg = ''

    if request.method == "POST":
        user = request.POST.get('user', None)  # 避免提交空，时异常

        user = user.strip()  # 用户输入末尾有空格是去空格

        pwd = request.POST.get('pwd', None)

        print('user=' + user, 'pwd=' + pwd)
    if user and pwd:
        return render(request, 'exampleHomePage.html', {'error_msg': "register successfully!Please log in."})
    elif user:
        return render(request, 'login.html', {'error_msg': "please enter password"})
    else:
        return render(request, 'login.html', {'error_msg': "please enter username"})
