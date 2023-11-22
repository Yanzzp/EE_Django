from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render

from user.models import Users


def login(request):
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        usm = request.POST.get('usm')
        pwd = request.POST.get('pwd')

        if Users.objects.filter(username=usm):
            if Users.objects.filter(username=usm)[0].password == pwd:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            HttpResponse('用户不存在')
    return render(request, 'users/login.html')


def register(request):
    if request.method == "POST":
        usm = request.POST.get('usm')
        pwd = request.POST.get('pwd')

        # 检查用户名是否已存在
        if Users.objects.filter(username=usm).exists():
            return HttpResponse('用户名已存在')

        # 创建新用户
        new_user = Users(username=usm, password=pwd)
        new_user.save()

        return HttpResponse('注册成功')

    return render(request, 'users/register.html')