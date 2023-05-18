from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    blogs = models.Blog.objects.all()
    context = {
        'news': blogs
    }
    return render(request, 'index.html', context)
