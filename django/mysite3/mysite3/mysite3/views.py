from django.shortcuts import render


# http://127.0.0.1:8000/
def index_view(request):
    return render(request, 'index.html')


def page1_view(request):
    return render(request, 'page1.html')


def page2_view(request):
    return render(request, 'page2.html')


def page3_view(request):
    return render(request, 'page3.html')
