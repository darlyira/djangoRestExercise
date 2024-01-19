from django.forms import ModelForm
from socialnetwork.models import Comment,Posts
class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        
class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'