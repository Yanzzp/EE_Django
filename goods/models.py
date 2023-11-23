from django.db import models


class Goods(models.Model):
    # 定义字段
    number = models.CharField(max_length=100, unique=True, verbose_name='编号')
    name = models.CharField(max_length=200, verbose_name='名称')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    quantity = models.IntegerField(verbose_name='数量')
    image = models.ImageField(upload_to='goods_images/', blank=True, null=True, verbose_name='图片')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
