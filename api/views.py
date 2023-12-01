from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.contrib import auth
from socialnetwork.models import User,Posts,Comment
from .serializer import UserSerializer,PostSerializer,CommentSerializer
        
class UserViewset(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class=PostSerializer    
