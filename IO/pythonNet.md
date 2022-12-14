IO网络编程
==========================

 

1. 定义

>IO指数据流的输入输出，从计算机应用层编程层面来说，在内存中存在数据交换的操作一般认为是IO操作,比如和终端交互 ,和磁盘交互，和网络交互等.

2. 程序分类

>* IO密集型程序：在程序执行中有大量IO操作，而cpu运算较少。消耗cpu较少，耗时长。

>* 计算密集型程序：程序运行中计算较多，IO操作相对较少。cpu消耗多，执行速度快，几乎没有阻塞。

## 文件

文件是保存在持久化存储设备(硬盘、U盘、光盘..)上的一段数据。从格式编码角度分为文本文件（打开后会自动解码为字符）、二进制文件(视频、音频等)。在Python里把文件视作一种类型的对象，类似之前学习过的其它数据类型。

### 字节串（bytes）

在python3中引入了字节串的概念，与str不同，字节串以字节序列值表达数据，更方便用来处理二进程数据。因此在python3中字节串是常见的二进制数据展现方式。

* 普通的ascii编码字符串可以在前面加b转换为字节串，例如：b'hello'
* 字符串转换为字节串方法 ：str.encode()
* 字节串转换为字符串方法 : bytes.decode() 


### 文件读写

对文件实现读写的基本操作步骤为：**打开**文件，读写文件，关闭文件

```python
"""
file_open.py
文件打开方式
"""
# 打开文件
"""
文本文件可以用文本或者二进制方式打开
二进制文件一定要用二进制方式打开
"""
f = open('file','r')  # 只读
f = open('file','w')  # 只写
f = open('file','a')  # 追加(add)
print(f)
# 读写
# 关闭文件
f.close()
```

```python
"""
file_read.py
读文件操作
"""
# 打开文件
f = open('./examples.txt','r')    # 默认r
# 读文件
"""
每次读取100字符  读主目录下 examples.desktop文件内容，并打印出来
"""
# while True:
#     s = f.read(100)
#     if not s:
#         # 当s为空则到了文件结尾
#         break
#     print(s,end='')
# s = f.read(100)
# s = f.read()
# print("读取内容:",s)
# 读取一行
data = f.readline()
print("一行内容：",data)
# 读取若干行
data = f.readlines(24)
print("多行内容：",data)
# 迭代特性
for i in f:
    print(i)  # 每次获取一行
f.close()
```

***代码实现：  day2/file_write.py***

```python
"""
file_write.py
文件写演示
"""
# f = open('file','wb')
f = open('file','a')
# 写操作
# f.write("hi,死鬼\n".encode())
# f.write("哎呀，干啥\n".encode())
f.writelines(['hahaha\n','呵呵呵\n','嘿嘿嘿'])
f.close()
```

函数三要素：功能、参数、返回值。

1. 打开文件

```python
file_object = open(file_name, access_mode='r', buffering=-1)
功能：打开一个文件，返回一个文件对象。
参数：file_name  文件名；
     access_mode  打开文件的方式,如果不写默认为‘r’ 
          文件模式                        操作
              r                    以读方式打开 文件必须存在
              w                    以写方式打开
                                   文件不存在则创建，存在清空原有内容 
              a                    以追加模式打开 
              r+                   以读写模式打开 文件必须存在
              w+                   以读写模式打开文件
                                   不存在则创建，存在清空原有内容
              a+                   以读写模式打开 追加模式
              rb                   以二进制读模式打开 同r
              wb                   以二进制写模式打开 同w
              ab                   以二进制追加模式打开 同a
              rb+                  以二进制读写模式打开 同r+
              wb+                  以二进制读写模式打开 同w+
              ab+                  以二进制读写模式打开 同a+
     buffering  1表示有行缓冲，默认则表示使用系统默认提供的缓冲机制。
返回值：成功返回文件操作对象。
```

   2.读取文件（3种方法）

>read([size])
>功能： 来直接读取文件中字符。
>参数： 如果没有给定size参数（默认值为-1）或者size值为负，文件将被读取直至末尾，给定size最多读取给定数目个字符（字节）。
>返回值： 返回读取到的内容
>
>* 注意：文件过大时候不建议直接读取到文件结尾，读到文件结尾会返回空字符串。

>readline([size])
>功能： 用来读取文件中一行
>参数： 如果没有给定size参数（默认值为-1）或者size值为负，表示读取一行，给定size表示最多读取制定的字符（字节）。
>返回值： 返回读取到的内容

>readlines([sizeint])
>功能： 读取文件中的每一行作为列表中的一项
>参数： 如果没有给定size参数（默认值为-1）或者size值为负，文件将被读取直至末尾，给定size表示读取到size字符所在行为止。
>返回值： 返回读取到的内容列表


>文件对象本身也是一个可迭代对象，在for循环中可以迭代文件的每一行。
```python
for line in f:
     print(line)
```

```python
"""
练习 ： 编写一个程序，从终端使用input输入一个单词，打印出这个单词及其解释
       * 每个单词一行
       * 单词和解释之间有空格
       * 单词按照升序（从小到大）排列
"""
word = input("单词:")  # 要查找单词
f = open('dict.txt') # 文本方式打开
# 每次获取一行
for line in f:
    w = line.split(' ')[0]
    if w > word:            #不是字符串长度的比较
        print("没有该单词")
        break
    elif word == w:
        # 查到单词
        print(line)
        break
else:
    print("没有该单词")
f.close()
```

  3.写入文件

>write(string)
>功能: 把文本数据或二进制数据块的字符串写入到文件中去
>参数：要写入的内容
>返回值：写入的字符个数
>
>* 如果需要换行要自己在写入内容中添加\n

>writelines(str_list)
>功能：接受一个字符串列表作为参数，将它们写入文件。
>参数: 要写入的内容列表

4. 关闭文件

打开一个文件后我们就可以通过文件对象对文件进行操作了，当操作结束后使用close（）关闭这个对象可以防止一些误操作，也可以节省资源。

>file_object.close()

5. with操作

python中的with语句使用于对资源进行访问的场合，保证不管处理过程中是否发生错误或者异常都会执行规定的“清理”操作，释放被访问的资源，比如有文件读写后自动关闭、线程中锁的自动获取和释放等。

with语句的语法格式如下：

```python
with context_expression [as obj]:
    with-body
```

通过with方法可以不用close(),因为with生成的对象在语句块结束后会自动处理，所以也就不需要close了，但是这个文件对象只能在with语句块内使用。

```python
with open('file','r+') as f:
    f.read()
```

>注意
>> 1. 加b的打开方式读写要求必须都是字节串
>> 2. 无论什么文件都可以使用二进制方式打开，但是二进制文件使用文本方式打开读写会出错.



```python

```

#### 刷新缓冲区

缓冲:系统自动的在内存中为每一个正在使用的文件开辟一个缓冲区，从内存向磁盘输出数据必须先送到内存缓冲区，再由缓冲区送到磁盘中去。从磁盘中读数据，则一次从磁盘文件将一批数据读入到内存缓冲区中，然后再从缓冲区将数据送到程序的数据区。

刷新缓冲区条件：

1. 缓冲区被写满
2. 程序执行结束或者文件对象被关闭
3. 行缓冲遇到换行
4. 程序中调用flush()函数

```python
"""
buffer.py
缓冲区示例
"""
f = open('file','w',1) 					# buffering=1表示行缓冲
while True:
    data = input(">>")
    if not data:
        break
    f.write("abc\n")
    # f.flush() # 自己刷新缓冲
f.close()
```

>flush()
该函数调用后会进行一次磁盘交互，将缓冲区中的内容写入到磁盘。

#### 文件偏移量

```python
"""
seek.py 文件偏移量
注意： r  w 打开文件默认文件偏移量在开头
      a 打开文件偏移量在结尾
      读写使用的是同一个偏移量
"""
f = open('file','w+') # 读写
f.write('hello world')
f.flush()
print("文件偏移量:",f.tell())			 # 查看偏移量
# 移动一下偏移量
f.seek(5,0)												# 0代表从开头算起
# f.write('你好')
data = f.read()
print(data)
f.close()
```

1. 定义
>打开一个文件进行操作时系统会自动生成一个记录，记录中描述了我们对文件的一系列操作。其中包括每次操作到的文件位置。文件的读写操作都是从这个位置开始进行的。

2. 基本操作
   
>tell()
功能：获取文件偏移量大小

>seek(offset[,whence])
>功能:移动文件偏移量位置
>参数：offset  代表相对于某个位置移动的字节数。负数表示向前移动，正数表示向后移动。
>​     whence是基准位置的默认值为 0，代表从文件开头算起，1代表从当前位置算起，2 代表从文件末尾算起。
>
>* 必须以二进制方式打开文件时基准位置才能是1或者2

```python
"""
空洞文件：提前占地方然后再填充，类似于迅雷下载文件，就是提前先占好地方。
"""
f = open('file','wb')
f.write(b'START')
# 末尾向后移动了10M
f.seek(1024*1024*10,2)
f.write(b'END')
f.close()
```

#### 文件描述符

1. 定义
>系统中每一个IO操作都会分配一个整数作为编号，该整数即这个IO操作的文件描述符。

2. 获取文件描述符
   
>fileno()
通过IO对象获取对应的文件描述符


### 文件管理函数

1. 获取文件大小  
>os.path.getsize(file)

2. 查看文件列表  
>os.listdir(dir)

3. 查看文件是否存在
>os.path.exists(file)

4. 判断文件类型
>os.path.isfile(file)

5. 删除文件
>os.remove(file)

```python
#     文件描述符示例
import os
print("文件大小：",os.path.getsize('file'))
print("查看目录内容：",os.listdir('.'))  #.代表当前目录
print("文件存在吗：",os.path.exists('./file'))
print("是一个普通文件：",os.path.isfile('file'))
print("删除一个文件：",os.remove('file'))
```
