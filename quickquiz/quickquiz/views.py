from asyncore import read
from operator import mod
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    p={'n':'Suvendu', 't':'Chowdhury'}
    return render(request,'index.html',p)

def analyzed(request):
    djtext=request.POST.get('text','default')
    removespace=request.POST.get('removespace','of')
    convertlowercase=request.POST.get('convertlowercase','of')
    convertuppercase=request.POST.get('convertuppercase','of')
   
    if removespace == "on":
        modtext=""
        for i in djtext:
            if i != ' ':
                modtext=modtext+i

        p={'ana':' "Remove Space" ','modtext':modtext}
        # return render(request,'analyzed.html',p)

    elif convertlowercase == "on":
        djtext=djtext.lower()
        p={'ana':' "Convert into lower case " ','modtext':djtext}
        # return render(request,'analyzed.html',p)

    elif convertuppercase == "on":
        djtext=djtext.upper()
        p={'ana':' "Convert into upper case " ','modtext':djtext}
        
    else :
        return HttpResponse("Please check any one check box")

    return render(request,'analyzed.html',p)


