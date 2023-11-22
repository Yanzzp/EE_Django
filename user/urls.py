from django.urls import path
from . import views

app_name = 'users'   # 定义一个命名空间，用来区分不同应用之间的链接地址
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]
