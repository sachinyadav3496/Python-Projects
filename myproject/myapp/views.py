from django.shortcuts import render,redirect
from django.http    import HttpResponse
from .forms import login,signup
from .models import Users

def index(request):
    form = login()
    return render(request,'myapp/index.html',{ 'form':form, })
def hello(request,id=None):
    data = [ "{}  Hello World".format(var+1) for var in range(50) ]
    return render(request,'myapp/hello.html',{ 'name':id,'data':data })
def Signup(request):
    form = signup()
    return render(request,'myapp/signup.html',{ 'form':form, })
def mklogin(request):
    form = login(request.POST)
    if form.is_valid():
        name = form.cleaned_data['Name']
        password = form.cleaned_data['Password']
        try :
            user = Users.objects.get(Name=name)
            if password == user.Password :
                return render(request,'myapp/mklogin.html',{'name':name,'password':password})
            else :
                form = login()
                error = "Invalid Password Try Again"
                return render(request,'myapp/index.html',{'form':form,'error':error})

        except Exception as e :
            form = signup()
            return render(request,'myapp/signup.html',{'form':form,'error':"No such user Exist \n Please Signup"})


    else :
        return HttpResponse("<h1>Form is not valid</h1>")
def mksignup(request):
    form = signup(request.POST)
    if form.is_valid():
        data = {
        'Name' : form.cleaned_data['Name'],
        'Password' : form.cleaned_data['Password'],
        'Fisrt_Name' : form.cleaned_data['First_Name'],
        'Last_Name' : form.cleaned_data['Last_Name'],
        'Email'  : form.cleaned_data['Email'],
        }
        print(data)
        return render(request,'myapp/mksignup.html',{ 'data':data })

    else :
        return HttpResponse("<h1>Form is not valid</h1>")
