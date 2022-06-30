from telnetlib import LOGOUT
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name='logout'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about')
]