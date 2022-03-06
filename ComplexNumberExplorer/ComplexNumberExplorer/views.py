from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect

def homeView(request):

    error_msg = ''

    if request.method == "POST":

        user = request.POST.get('user', None) #避免提交空，时异常

        user = user.strip() #用户输入末尾有空格是去空格

        pwd = request.POST.get('pwd', None)
        
        if user == "root" and pwd == "123":

            print('user=' + user, 'pwd=' + pwd)

            return redirect("/home")

        else:

            error_msg = "账号或者密码不对"

            print('user='+user, 'pwd='+pwd)

    return render(request, 'exampleHomePage.html',{'error_msg': error_msg})

 

def directRegister(request):

    print (request.GET.items)
    if request.method == "POST":
        return render(request,'exampleRegisterPage.html')

def registerView(request):
    
    error_msg = ''

    if request.method == "POST":

        user = request.POST.get('user', None) #避免提交空，时异常

        user = user.strip() #用户输入末尾有空格是去空格

        pwd = request.POST.get('pwd', None)

        print('user=' + user, 'pwd=' + pwd)
    if user and pwd:
        return render(request, 'exampleHomePage.html',{'error_msg': "register successfully!Please log in."})
    elif user:
        return render(request,'exampleRegisterPage.html',{'error_msg': "please enter password"})
    else:
        return render(request,'exampleRegisterPage.html',{'error_msg': "please enter username"})