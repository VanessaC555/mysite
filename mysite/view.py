#from django.http import HttpResponse
from django.shortcuts import render

def mysite(request):
    context={}
    context['mysite']='This is mysite new!'
    return render(request,'mysite.html',context)