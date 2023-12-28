from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def kategori(request):
    data = kategori.objects.all()
    layout = loader.get_template('index.html')
    context = {
        'test' : 'ini test variable',
        'datas' : data,
    }
    return HttpResponse(layout.render(context, request))

def weblog(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def coba2(request):
    return render(request, 'weblog/coba2.html')

def loo(request):
    return render(request, 'weblog/loo.html')

def coba(request):
    return render(request, 'weblog/coba.html')