from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts':posts
    }
    return render(request, 'blog_index.html',context)

def blog_category(request,category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request,'blog_category.html',context)

def blog_detail(request,pk):
    post = Post.objects.get(pk= pk)

    form = CommentForm()
    if request.method == 'POST':
        form =  CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author =  form.cleaned_data["author"],
                body =  form.cleaned_data["body"],
                post = post
            )
            comment.save()


    comments = Comment.objects.filter(post=post)
    context = {
        'post' : post,
        'comments': comments,
        'form':form
    }
    return render(request,'blog_detail.html',context)

def staff_place(request):
    return HttpResponse("Employee must wash hands",content_type='text/plain')

def see_request(request):    
    pas
    # print("ankur")
    
    # text = f"""
    # Some atttributes of HttpRequest onject:
    # Scheme : {request.scheme}
    # Path : {request.path}
    # Method : {request.method}
    # GET : {request.get}
    # User :  {request.user}
    # """
    # print(text)
    # return HttpResponse("NEW PAge",content_type = 'text/plain')

def user_info(request):
    text = f"""
    Selected HttpRequest.user attributes:
    username : {request.username}
    is_anonymous : {request.is_anonymous}
    is_staff  : {request.is_staff}
    is_superuser :  {request.is_superuser}
    is_user : {request.is_active}

    """

    return HttpResponse(text,content_type= "text/plain")
