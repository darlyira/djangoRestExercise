from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name= "socialnetwork"
route = DefaultRouter()
route.register('user',views.UserViewset)
route.register('comment',views.CommentViewset)
route.register('posts',views.PostViewset)

urlpatterns = [
    path('',include(route.urls)),

]
