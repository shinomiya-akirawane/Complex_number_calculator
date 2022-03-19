from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('login/', views.loginSignUp),
    path('newQuiz/', views.CreateQuiz),
    path('error404/', views.error404),
    path('error500/', views.error500),
    path('takingquiz/', views.TakingQuiz),
    path('teacherclasses/', views.TeacherClasses),
    path('quizhistory/', views.Quizhistory),


]
