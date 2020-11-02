from django.urls import path
from . import views

urlpatterns = [
    path("",views.blog_index,name = 'blog_index'),
    path("<int:pk>/",views.blog_detail,name = "blog_detail"),
    path("<category>/",views.blog_category,name = "blog_category"),
    path("see_request/",views.see_request,name="see_request"),
    path("user_detail/",views.user_info,name='user_detail'),
    path("staff/",views.staff_place),
]