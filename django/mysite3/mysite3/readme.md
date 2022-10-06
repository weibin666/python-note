### 配置模板目录
```python
#settings.py 57行
'DIRS': [os.path.join(BASE_DIR,'templates')],
```
### 创建模板目录
```pythonstub
创建目录templates
index.html
page1.html
page2.html
page3.html
```
### 创建模板文件
```html
#index.html
<h1>项目首页</h1>
<a href="/page1">page1</a>
<a href="/page2">page2</a>
<a href="/page3">page3</a>
```
```html
#page1.html
<h1>page1</h1>
<a href="/">返回首页</a>
```
```html
#page2.html
<h1>page2</h1>
<a href="/">返回首页</a>
```
```html
#page3.html
<h1>page3</h1>
<a href="/">返回首页</a>
```
### 配置路由和视图函数
```python
#urls.py
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('page1', views.page1_view),
    path('page2', views.page2_view),
    path('page3', views.page3_view),
]
```
```python
#views.py
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
```