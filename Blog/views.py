from django.shortcuts import render
from .models import Post
from datetime import datetime
# Create your views here.

def index(request):
    posts = Post.objects.all()
    quantidade = len(posts)

    return render(request, 'index.html', {'posts': posts, 'quantidade': quantidade})

def create(request):
    posts = Post.objects.all()
    mensagem = ''
    quantidade = len(posts)

    if request.POST:
        title = request.POST['Input']
        thepost = request.POST['Inputt']
        post = Post.create(title, thepost)
        mensagem = 'Post Criado com Sucesso'

    return render(request, 'create.html', {'posts': posts, 'mensagem': mensagem})
