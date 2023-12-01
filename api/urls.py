from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name= "socialnetwork"
route = DefaultRouter()
route.register('user',views.UserViewset)
route.register('comment',views.CommentViewset)

urlpatterns = [
    path('',include(route.urls)),
    # path('user/list',views.getUsers),
    # path('user/delete/<int:id>',views.deleteUser),
    # path('post/delete/<int:id>',views.delete_post),
    # path('comment/delete/<int:id>',views.delete_comment),
    # path('post/add',views.new_post),
    # path('user/edit/<int:id>',views.editUser),
    # path('post/edit/<int:id>',views.edit_post),
    # path('comment/edit/<int:id>',views.edit_comment),
    # path('post/list',views.get_post),
    # path('comment/add',views.new_comment),
    # path('comment/list',views.get_comment)

]
