from django.urls  import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    path("",views.dashboard,name = 'user_dashboard'),
    path("register/",views.register,name = 'register'),
    path("add_message/",views.add_messages,name = 'add_message'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^oauth/",include("social_django.urls")),
]