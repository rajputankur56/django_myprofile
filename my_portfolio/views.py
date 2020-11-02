from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required


def hello(request):
    return HttpResponse("HEllow there")