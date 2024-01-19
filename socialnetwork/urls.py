from django.urls import path
from . import views

urlpatterns = [
    path('',views.getPost),
    path('details/<int:id>',views.postDetails),
    path('comment/<int:id>',views.Commenting),
    path('newPost/',views.newPost),
]
