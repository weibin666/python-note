from django.shortcuts import render, redirect
from .models import Book, Author
from django.db import models
from django.http import HttpResponse


# Create your views here.
# 作业 当用户访问http://127.0.0.1:8000/book/index时 显示bookstore的首页index.html 在首页中以表格的方式显示所有数据库中的图书

# 1.创建bookstore/urls.py 在urls.py中导入path函数 导入views.py 添加urlpatterns列表
# 2.到mysite3/urls.py中配置分布式路由 如果用户访问book/开头的地址时 将请求转到bookstore.urls
# 3.bookstore/urls.py 匹配以index/开头的路由 编写视图函数 在视图函数中查询所有的图书 然后传给模板index.html
# from .models import Book
# books = Book.objects.all()
# for book in books:
#   print(f'id为{book.id}的书是{book.title}')
# 4.编写模板index.html 以表格的形式显示数据


def index_view(request):
    # all() values() values_list()
    # order_by()
    # filter() exclude() get()
    books = Book.objects.all()
    return render(request, 'bookstore/index.html', locals())


def modify_view(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        book = Book.objects.get(id=id)
        return render(request, 'bookstore/modify.html', locals())
    elif request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        book = Book.objects.get(id=id)
        book.title = title
        book.pub = pub
        book.price = price
        book.market_price = market_price
        book.save()
        return redirect('/book/index/')


def delete_view(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        book = Book.objects.get(id=id)
        return render(request, 'bookstore/delete.html', locals())
    elif request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return redirect('/book/index/')
        except:
            print('删除失败')
