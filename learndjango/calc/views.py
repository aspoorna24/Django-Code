from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World</h1>")

# dynamic content 
def page(request):
    return render(request, 'home.html',{'name':'Poorna'})

def add(request):
    val1 = request.GET['num1'] # use single quote
    val2 = request.GET['num2']
    res = int(val1) + int(val2)
    return render(request,'result.html',{'res':res})


def adds(request):
    val1 = request.POST['num1'] # use single quote
    val2 = request.POST['num2']
    res = int(val1) + int(val2)
    return render(request,'result.html',{'res':res})

