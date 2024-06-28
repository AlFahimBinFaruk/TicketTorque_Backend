from django.urls import path
from . import views

urlpatterns=[
    path("",views.GetAllUserData.as_view()),
    path("register",views.RegisterNewUser.as_view()),
    path("login",views.LoginUser.as_view())
]