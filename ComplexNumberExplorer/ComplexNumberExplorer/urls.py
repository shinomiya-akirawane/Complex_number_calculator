from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('login/', views.loginSignUp),
    path('addNewQuiz/', views.addNewQuiz),
    path('studentQuiz/', views.studentQuiz),
    path('quiz/', views.quiz),
]