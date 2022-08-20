from asyncore import read
from operator import mod
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    p={'n':'Suvendu', 't':'Chowdhury'}
    return render(request,'index.html',p)

def analyzed(request):
    djtext=request.GET.get('text','default')
    removespace=request.GET.get('removespace','of')
    modtext=""
    for i in djtext:
        if i != ' ':
            modtext=modtext+i

    p={'ana':' "Remove Space" ','modtext':modtext}
    return render(request,'analyzed.html',p)



