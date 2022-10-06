from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# http://127.0.0.1:8000/news/index/
def index_view(request):
    # return HttpResponse('这是news应用的首页')
    return render(request, 'news/index.html')