from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="index"),
    path("rating/",rating,name="rating"),
    path("student/<int:id>",student,name="student"),
    path("login/",loginF,name="login"),
    path("logout/", logoutF, name="logout"),
    path("rules/", rules, name="rules"),

]
