from django.shortcuts import render

def index(request):
    return render(request, 'mysite/home.html')
def engineering(request):
    return render(request,'mysite/engineering.html')
def medical(request):
    return render(request,'mysite/medical.html')
def bpharm(request):
    return render(request,'mysite/bpharmacy.html')
def commerce2(request):
    return render(request,'mysite/commerce2.html')
def arts1(request):
    return render(request,'mysite/arts1.html')
def arts2(request):
    return render(request,'mysite/arts2.html')
