from django.shortcuts import render,redirect
from django.http    import HttpResponse
from .forms import login,signup,reset_form
from .models import Users
from django.core.mail import send_mail
from ..myproject import settings
def index(request):
    if request.session.get('user') and request.session.get('password') :
        msg = "Welcome Back User {}".format(request.session['user'])
        return render(request,'myapp/index.html',{'msg':msg})
    else :
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
                request.session['user'] = name
                request.session['password'] = password
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
        'First_Name' : form.cleaned_data['First_Name'],
        'Last_Name' : form.cleaned_data['Last_Name'],
        'Email'  : form.cleaned_data['Email'],
        }
        obj = Users.objects.create(**data)
        obj.save()
        return render(request,'myapp/mksignup.html',{ 'data':data })

    else :
        return HttpResponse("<h1>Form is not valid</h1>")

def logout(request):
    del request.session['user']
    del request.session['password']
    form = login()
    return render(request,'myapp/index.html',{'form':form,})

def forgot(request):
    form = reset_form()
    return render(request,'myapp/forgot.html',{ 'form':form,})

def change_password(request):
    form = reset_form(request.POST)
    if form.is_valid() :
        try :
            obj = Users.objects.get(Email=form.cleaned_data['Email'])
            from random import choice
            l = [ 1,2,3,4,5,6,7,8,9,0]
            s = str(choice(l))+str(choice(l))+str(choice(l))+str(choice(l))
            request.session['otp'] = s
            message = "Hey Check this out \nYour OTP for reset password is %s "%(s)

            subject = "Reset Password"
            from_email = "3496.grras@gmail.com"
            to_email = form.cleaned_data['email']
            send_mail(subject, message, from_email, (to_email,),auth_password = settings.EMAIL_HOST_PASSWORD,fail_silently=False)
            return render(request,'myapp/reset_password.html')

        except Exception as e :
            form = login()
            error = "This Email Address does not Exist in Our System Try Again"
            return render(request,'myapp/index.html',{'form':form,'error':error})
    else :
        form = login()
        error = "Invalid Form for Password Reset Try Again"
        return render(request,'myapp/index.html',{'form':form,'error':error})