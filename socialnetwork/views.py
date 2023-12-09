from django.shortcuts import render
from api import views

# Create your views here.
def homepage(request):
    posts = views.postDetaills
    
    
    return render(request,'home.html',{'Data':posts})