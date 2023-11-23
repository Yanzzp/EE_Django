from django.urls import path
from . import views
# user/urls.py
app_name = 'users'  # 定义一个命名空间，用来区分不同应用之间的链接地址
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('logout/', views.logout, name='logout'),
]
