from django.db import models


# Create your models here.
# 默认数据表名应用名_小写模型类名 bookstore_book
class Book(models.Model):
    # id
    title = models.CharField("书名", max_length=50, default='', unique=True)
    pub = models.CharField('出版社', max_length=60, blank=False, null=False, default='')
    price = models.DecimalField('定价', max_digits=6, decimal_places=2, default=0.0)
    market_price = models.DecimalField('零售价', max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.id}-{self.title}-{self.pub}-{self.price}-{self.market_price}'

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = '图书s'


class Author(models.Model):
    name = models.CharField('姓名', max_length=20)
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('邮箱', blank=True, null=True)
