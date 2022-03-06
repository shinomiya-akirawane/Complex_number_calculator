from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homeView),
    path('directRegister/', views.directRegister),
    path('register/',views.registerView),
]
