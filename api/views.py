from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework import permissions
from socialnetwork.models import User,Posts,Comment
from .serializer import UserSerializer,PostSerializer,CommentSerializer,UserdetaillsSerializer,CommentAdditionSerializer
        
class UserViewset(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserdetaillsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CommentViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentAdditionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CommentListViewset(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewset(viewsets.ModelViewSet):
    queryset =Posts.objects.all()
    serializer_class=PostSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def postDetaills(request, id):
        query = Comment.objects.filter(post= id)
        seriazer= CommentSerializer(query,many=True)
        post = Posts.objects.get(id=id)
        postserializer = PostSerializer(post)
        return Response({"Post":postserializer.data,"coments":seriazer.data})         
@api_view(['POST'])
def ajoutercommentaire(request):    
    if request.method == 'POST':
        serializer = CommentAdditionSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
