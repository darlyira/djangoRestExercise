from django.shortcuts import render,redirect
from django.http.response import HttpResponse
import requests
from .forms.commentform import CommentsForm,PostForm
# Create your views here.
from .models import Posts,Comment

def getPost(request):
    posts = Posts.objects.all()
    return render(request,"posts.html",{'Posts':posts})
def postDetails(request,id):
    poste = Comment.objects.filter(post=id)
    return render(request,"postdetails.html",{'details':poste})

def Commenting(request,id):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/socialnetwork/details/{id}')
    else:
        form= CommentsForm()
        return render(request,'newComment.html',{'Comment':form})
def newPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/socialnetwork/')
    else:
        form = PostForm()
        return render(request,'newpost.html',{'Post':form})
    