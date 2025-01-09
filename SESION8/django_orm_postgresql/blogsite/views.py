from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

def index(request):
    posts = Post.objects.all()  #.values() 

    context = {
        "posts" : posts
    }

    return render(request,"index.html",context)

def agregar(request):
    
    context = {
        
    }

    return render(request,"agregar.html",context)

def agregarregistro(request):
    titulo = request.POST['title'] 
    contenido = request.POST['content'] 
    autor = request.POST['author'] 
    post = Post(title=titulo, content=contenido, author=autor) 
    post.save() 
    return HttpResponseRedirect(reverse('index'))


def eliminar(request, id):
    post = Post.objects.get(id = id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

def actualizar(request, id):
    post = Post.objects.get(id = id)
    context = { "post": post }
    return render(request, "actualizar.html", context)

def actualizarregistro(request, id):
    titulo = request.POST['title'] 
    contenido = request.POST['content'] 
    autor = request.POST['author'] 
    post = Post.objects.get(id = id)

    post.title = titulo
    post.content = contenido
    post.author = autor
    post.save()
    return HttpResponseRedirect(reverse('index'))

