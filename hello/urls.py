from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("get_my_ip", views.get_my_ip, name="get_my_ip"),

    #cocktail_list
]