from django.db import models

# Create your models here.
class User(models.Model):
    name =models.CharField( max_length=255,null=False,blank=False)
    user_name= models.CharField( max_length=50,blank=False,null=False)
    email = models.EmailField(null=False,blank=False, max_length=254)
    password = models.CharField(null=False,blank=False, max_length=50)
    adress= models.CharField( max_length=50)
    tel= models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.name

class Posts(models.Model):
    
    title = models.CharField(null=False,blank=False, max_length=50)
    contexte = models.TextField(null=False,blank=False, max_length=50)
    user = models.ForeignKey(User,related_name='Posts',related_query_name='Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    
    content = models.TextField()
    post = models.ForeignKey(Posts,related_name='Coments',related_query_name='Comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='Commenters',related_query_name='commenter', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.post


   
