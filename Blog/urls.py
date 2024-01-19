"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
<<<<<<< HEAD
                                                                                                                                                                                                                                                
=======
from api import views
from socialnetwork import views as social_views

>>>>>>> 279890548c8620a20153fa1887315a9e2b07fbaf
urlpatterns = [
    path('socialnetwork/',include('socialnetwork.urls')),
    path('admin/', admin.site.urls),
    path('social/',include('api.urls')),
<<<<<<< HEAD
    
#     path('authentication/',include('dj_rest_auth.urls'))
=======
    path('',social_views.homepage),
    path('authentication/',include('dj_rest_auth.urls'))
>>>>>>> 279890548c8620a20153fa1887315a9e2b07fbaf
]
