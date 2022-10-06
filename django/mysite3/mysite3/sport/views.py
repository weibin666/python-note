from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# http://127.0.0.1:8000/sport/index
def index_view(request):
    # return HttpResponse('这是sport应用的首页')
    return render(request, 'sport/index.html')
