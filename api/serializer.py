from rest_framework import serializers
from socialnetwork.models import User,Posts,Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','name']

class UserdetaillsSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Posts
        fields = ['id','title','contexte','created_at','user']
        
class CommentAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment 
        fields = '__all__'       

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user= UserSerializer()
    # post = PostSerializer()
    class Meta:
        model = Comment
        fields = ['content','created_at','updated_at','user']
