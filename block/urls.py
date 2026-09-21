"""
URL configuration for block project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path

from posts.views import hello_world, my_name, say_name, post_list, post_detail, delete_post
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("helllo/", hello_world),
    path("name/", my_name),
    path("name/<str:name>", say_name),
    path("", post_list, name ="post_list"),
    path("posts/<int:pk>/", post_detail, name ="post_detail"),
    path('posts/<int:pk>/delete', delete_post, name='post_delete'),
]
