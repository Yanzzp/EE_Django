from django.urls import path
from . import views

app_name = 'goods'  # 定义应用程序命名空间

urlpatterns = [
    # 在这里添加与 goods 相关的 URL 配置
    path('update/<int:good_id>/', views.update_good, name='update_good'),
    # 您可以在这里添加更多与 goods 相关的 URL
]