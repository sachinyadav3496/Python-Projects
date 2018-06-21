from django.shortcuts import render
from django.http    import HttpResponse
from .forms import login,signup
# Create your views here.

def index(request):
    form = login()
    return render(request,'myapp/index.html',{ 'form':form, })
def hello(request,id=None):
    return render(request,'myapp/hello.html',{ 'name':id, })
def Signup(request):
    form = signup()
    return render(request,'myapp/signup.html',{ 'form':form, })