from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('login/', views.loginSignUp),
    path('newQuiz/', views.AddNewQuiz),
]