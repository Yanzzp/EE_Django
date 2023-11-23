from django.shortcuts import get_object_or_404, redirect
from .models import Goods


def update_good(request, good_id):
    if request.method == "POST":
        good = get_object_or_404(Goods, id=good_id)
        good.quantity = request.POST.get('quantity')
        good.price = request.POST.get('price')

        image = request.FILES.get('image')
        if image:
            good.image = image

        good.save()
        return redirect('/user/profile/admin')  # 重定向到管理员页面的 URL

    return redirect('/error-page/')  # 如果不是 POST 请求，重定向到错误页面或其他页面
