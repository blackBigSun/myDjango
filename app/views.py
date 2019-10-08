from django.shortcuts import render

# Create your views here.

#引入HttpResponse响应类
from django.shortcuts import HttpResponse
#定义welcome函数
def welcome(request):
    #返回响应对象，参数为字符串‘hello django!’
    #参数会显示在网页中
    return HttpResponse('hello django!')

def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)