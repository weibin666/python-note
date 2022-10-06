"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from . import views

# http://127.0.0.1:8000/music/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('page1/', views.page1_view),
    path('page2/', views.page2_view),
    path('page3/', views.page3_view),

    path('music/', include('music.urls')),
    path('sport/', include('sport.urls')),
    path('news/', include('news.urls')),
    path('book/', include('bookstore.urls')),
]
