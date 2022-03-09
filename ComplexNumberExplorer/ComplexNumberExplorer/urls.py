from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),

    # homepage and login system
    path('homepage/', views.homepage),
    path('login/', views.login),

    # quiz
    path('quiz/', views.quiz),

    path('directRegister/', views.directRegister),
    path('register/',views.registerView),
]
