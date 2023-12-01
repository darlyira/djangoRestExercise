from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.contrib import auth
from socialnetwork.models import User,Posts,Comment
from .serializer import UserSerializer,PostSerializer,CommentSerializer

@api_view(['POST'])
def newUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
    users= User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def new_post(request):
    if request.method ==  'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)   

@api_view(['GET'])
def get_post(request):
    poste= Posts.objects.all()
    serializer = PostSerializer(poste,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def new_comment(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def get_comment(request):
    commentaire=Comment.objects.all()
    serializer =  CommentSerializer(commentaire,many=True)
    return Response(serializer.data)       

@api_view(['POST','GET'])
def editUser(request,id):
    user= User.objects.get(id=id)
    serializer= UserSerializer(user)
    if request.method == 'POST':
        edit_serialiser = UserSerializer(data=request.data,instance=user)
        if edit_serialiser.is_valid():
            edit_serialiser.save()
        return Response(edit_serialiser.data)
    else:
        return Response(serializer.data)
    
@api_view(['POST','GET'])
def edit_post(request,id):
    post=Posts.objects.get(id=id)
    serialiser=PostSerializer(post)
    if request.method=='POST':
        edit_serialiser=PostSerializer(data=request.data,instance=post)
        if edit_serialiser.is_valid():
            edit_serialiser.save()
        return Response(edit_serialiser.data)
    
    else:
        return Response(serialiser.data)  
    
@api_view(['POST','GET'])
def edit_comment(request,id):
    comment=Comment.objects.get(id=id)
    serialiser=CommentSerializer(comment)
    if request.method=='POST':
        edit_serialiser=CommentSerializer(data=request.data,instance=comment)
        if edit_serialiser.is_valid():
            edit_serialiser.save()
        return Response(edit_serialiser.data)
    else:
        return Response(serialiser.data)    
          
@api_view(['GET','DELETE'])
def deleteUser(request,id):
    user= User.objects.get(id=id)
    if request.method== 'DELETE':
        serializer= UserSerializer(user)
        user.delete()
        return Response(serializer.data)
    else:
        serializer=UserSerializer(user)
        return Response(serializer.data,status=200)
    
@api_view(['GET','DELETE'])
def delete_post(request,id):
    post= Posts.objects.get(id=id)
    if request.method== 'DELETE':
        serializer= PostSerializer(post)
        post.delete()
        return Response(serializer.data)
    else:
        serializer=PostSerializer(post)
        return Response(serializer.data,status=200)
    
@api_view(['GET','DELETE'])
def delete_comment(request,id):
    comment=Comment.objects.get(id=id)
    if request.method == 'DELETE':
        serializer= CommentSerializer(comment)
        comment.delete()
        return Response(serializer.data)
    else:
        serializer=CommentSerializer(comment)
        return Response(serializer.data,status=200)    
         
class UserViewset(viewsets.ModelViewSet):
    if auth.user_logged_in:
        queryset= User.objects.all()
        serializer_class = UserSerializer
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer