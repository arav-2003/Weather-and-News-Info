from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='weather.html'),
    path('hello',views.hello,name='hello.html'),
    path('',views.news,name='news.html'),
    path('home',views.home,name='base.html'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
