from django.shortcuts import render

# Create your views here.
def base (request):
    context={}
    return render(request,'ecn/base.html',context)

def home (request):
    context={}
    return render(request,'ecn/home.html',context)