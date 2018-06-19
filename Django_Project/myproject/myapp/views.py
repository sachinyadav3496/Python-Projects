from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("<h1 style='color:red'>Welcome to Django</h1>\
    #<h1 style='color:green'>This is the first page of mysite</h1>")
    return render(request,'myapp/home.html')