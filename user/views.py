from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from user.models import Users


def user_profile(request, username):
    if 'username' not in request.session or request.session['username'] != username:
        return redirect('/user/login/')
    return render(request, 'users/profile.html', {'username': username})



def login(request):
    if 'username' in request.session:
        return redirect(f'/user/profile/{request.session["username"]}/')

    if request.method == "POST":
        usm = request.POST.get('usm')
        pwd = request.POST.get('pwd')

        if Users.objects.filter(username=usm).exists():
            user = Users.objects.filter(username=usm).first()
            if user.password == pwd:
                # 登录成功，设置会话
                request.session['username'] = user.username
                return HttpResponseRedirect(f'/user/profile/{usm}/')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')
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


def logout(request):
    # 删除会话中的用户信息
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect('/user/login/')  # 重定向到登录页面
