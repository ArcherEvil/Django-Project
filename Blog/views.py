from django.shortcuts import render
from .models import Post
from datetime import datetime
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    posts = Post.objects.all()
    quantidade = len(posts)
    try:
        if request.POST:
            ide = request.POST['id']
            instance = Post.objects.get(id=ide)
            instance.delete()
            return HttpResponseRedirect('')
            
    except Exception as e:
        print(e)

    return render(request, 'index.html', {'posts': posts, 'quantidade': quantidade})

def create(request):
    posts = Post.objects.all()
    mensagem = ''
    quantidade = len(posts)
    if request.POST:
        title = request.POST['Input']
        thepost = request.POST['Inputt']
        post = Post.create(title, thepost)
        mensagem = 'Post Created.'

    return render(request, 'create.html', {'posts': posts, 'mensagem': mensagem})

def edit(request, pk):
    mensagem = ''
    post = Post.objects.get(id=pk)
    if request.POST:
        title = request.POST['Input']
        thepost = request.POST['Inputt']
        Post.objects.filter(id=pk).update(title=title, post=thepost, edited=True)
        mensagem = 'Post Edited.'
    
    return render(request, 'edit.html', {'post': post, 'mensagem': mensagem})