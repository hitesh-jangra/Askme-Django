from __future__ import unicode_literals
from django.shortcuts import render,redirect
from questions.models import Question
from .models import Blog
from .forms import BlogForm
from django.shortcuts import get_object_or_404 
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    queryset = Question.objects.all()[:6]
    context = {"queryset": queryset}
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html", {})

def blog(request):
    
    context={'blog':Blog.objects.all()}
    return render(request,'core/blog.html',context)

def visitblog(request,id=None):

    visit=get_object_or_404(Blog,id=id)
    context={
        'blog':visit
    }
    return render(request,'core/visitblog.html',context)

@login_required()
def addblog(request):
    form=BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog')

    context={'form':form}
    return render(request,'core/addblog.html',context)
