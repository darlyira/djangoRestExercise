from rest_framework import serializers
from socialnetwork.models import User,Posts,Comment

class UserSerializer(serializers.ModelSerializer):
    posts=serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['name','user_name','email','password','adress','tel','posts']

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
        fields = '__all__'



class PostSerializers(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Posts
        fields = ['title','contexte','user']
        
class PostDetailSerialiser(serializers.HyperlinkedModelSerializer):
    user =UserSerializer()
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = ['id','content','post','user','created_at']
