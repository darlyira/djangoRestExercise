from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins as drf_mixins
from rest_framework import permissions,viewsets
from rest_framework.decorators import api_view
from socialnetwork.models import User,Posts,Comment
from .serializer import UserSerializer,PostSerializer,CommentSerializer,PostSerializers,PostDetailSerialiser
        
class UserViewset(viewsets.GenericViewSet,drf_mixins.CreateModelMixin,drf_mixins.ListModelMixin,drf_mixins.RetrieveModelMixin):
    queryset= User.objects.all()
    serializer_class = UserSerializer

    
class CommentViewset(viewsets.GenericViewSet,drf_mixins.CreateModelMixin,drf_mixins.ListModelMixin,drf_mixins.RetrieveModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewset(viewsets.GenericViewSet,drf_mixins.CreateModelMixin,drf_mixins.ListModelMixin,drf_mixins.RetrieveModelMixin):
    queryset =Posts.objects.raw('select socialnetwork_posts.id,socialnetwork_posts.title,socialnetwork_posts.contexte,socialnetwork_user.name from socialnetwork_posts,socialnetwork_user where socialnetwork_posts.user_id=socialnetwork_user.id')
    serializer_class=PostSerializers

class PostDetails(viewsets.GenericViewSet,drf_mixins.ListModelMixin,drf_mixins.RetrieveModelMixin):
    queryset = Comment.objects.all()
    serializer_class = PostDetailSerialiser

@api_view(['GET'])
def allPost(request):
    post= Posts.objects.all()
    print(post.query)
    serializer= PostSerializers(post)
    
    return Response(serializer.data)
    