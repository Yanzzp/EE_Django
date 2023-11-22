from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return self.username