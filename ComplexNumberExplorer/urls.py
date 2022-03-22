from django.urls import path
from CNExplorer import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('login/', views.loginSignUp),
    path('newQuiz/', views.CreateQuiz),
    path('error404/', views.error404),
    path('error500/', views.error500),
    path('takingquiz/', views.TakingQuizv2),
    path('teacherclasses/', views.TeacherClasses),
    path('quizhistory/', views.Quizhistory),
    path('register/', views.Register),
    path('quizlist/', views.QuizList),
    path('logout/', views.logout),
    path('teacherquizlist/', views.teacherQuizList),


]
