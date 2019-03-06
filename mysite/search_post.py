# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf

#接收post请求
def search_post(request):
    ctx = {}
    #由于一开始没有收到请求，所以ctx是空字典
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)