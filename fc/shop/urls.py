from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path("",views.index,name ="Shophome"),
   path("Home/",views.Home,name = "Home"),
   path("Contact/",views.Contact,name ="Contact"),
   path("About/",views.About,name ="About"),
   path('post_list/', views.post_list, name='post_list'),
]


