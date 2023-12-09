from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name= "socialnetwork"
route = DefaultRouter()
route.register('user',views.UserViewset)
route.register('commentlist',views.CommentListViewset)
route.register('posts',views.PostViewset)


urlpatterns = [
    path('',include(route.urls)),
    path('user/list',views.UserViewset.list),
    path('commentadd/',views.ajoutercommentaire),
    path('postdetails/<int:id>',views.postDetaills),
    
    
]
