from django.urls import path
from . import views

# http://127.0.0.1:8000/book/index/
urlpatterns = [
    path('index/', views.index_view),
    path('modify/', views.modify_view),
    path('delete/', views.delete_view),
]
