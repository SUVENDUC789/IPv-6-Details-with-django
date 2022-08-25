# import time
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def ipv6(request):
    return render(request, 'ipv6.html')

def ipv4(request):
    return render(request, 'ipv4.html')

def analyzedIpv4(request):
    return render(request, 'analyzedIpv4.html')

# def delayCreate(request):
#     time.sleep(5)
#     return render(request, 'delay.html')


def analyzedIpv6(request):
    var = request.POST.get('value', 'default')
    binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    # var=input("Enter Ipv-6 : ")
    var = var.lower()
    var2 = []

    try:
        for i in var:
            if i == ':':
                var2.append(i)
            else:
                var2.append(binary[i])

        binip6 = ""
        for item in var2:
            binip6 = binip6+item

        p = {'Ipv6': var, 'binipv6': binip6}
        return render(request, 'Analizingipv6.html', p)
    except:
        return HttpResponse("<h1 class='text-danger'>Please enter valid ipv6</h1>")


