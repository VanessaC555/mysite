# -*- coding:utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test

#数据库操作
def  testdb(request):
    test1 = Test(name='test1')
    test1.save()
    test2 = Test(name='test2')
    test2.save()
#   return HttpResponse("<p>数据添加成功！</p>")

    response = ""
    response1 = ""
#   list = Test.objects.all()
    list = Test.objects.order_by("name")

    for var in list:
        response1 += var.name +" "
    response = response1
    return HttpResponse("<p>" + response + "<p>")
