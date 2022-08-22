from asyncore import read
from operator import mod
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    p={'n':'Suvendu', 't':'Chowdhury'}
    return render(request,'index.html',p)

def analyzed(request):
    djtext=request.POST.get('text','default')
    choice=request.POST.get('choice','default')
   
    if choice == "removespace":
        modtext=""
        for i in djtext:
            if i != ' ':
                modtext=modtext+i

        p={'ana':' "Remove Space" ','modtext':modtext}
        return render(request,'analyzed.html',p)

    elif choice == "convertlowercase":
        djtext=djtext.lower()
        p={'ana':' "Convert into lower case " ','modtext':djtext}
        return render(request,'analyzed.html',p)

    elif choice == "convertuppercase":
        djtext=djtext.upper()
        p={'ana':' "Convert into upper case " ','modtext':djtext}
        return render(request,'analyzed.html',p)
        
    elif choice == "None" :
        return HttpResponse("Please chose any one check box")