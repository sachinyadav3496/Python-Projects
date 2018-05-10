import smtplib
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import signup_form,login_form,reset_form,password,userprofile_form
from django.contrib.auth.models import User
from django.contrib.auth    import authenticate
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from .models import UserProfile

def base(request):

    return render(request,'myapp/base.html')


def about(requset):

    if 'username' in requset.session:

        f = 1
    else :

        f = 0
    context = { 'f':f }

    return render(requset,'myapp/about.html',context)

def main(request):

     if 'username' in request.session:

        f = 1
     else :

        f = 0
     context = { 'f':f }

     return render(request,'myapp/home.html',context)

def login(request):

    myerror = None
    if 'username' in request.session:

        f = 1
    else :

        f = 0


    context = {'error':myerror,'f':f}
    if 'username' in request.session:

        uname=request.session['username']
        passwd=request.session['password']
        res=authenticate(username=uname,password=passwd)

        if res is not None :

                name=request.session['username']
                data=User.objects.get(username=name)
                name=data.username
                email=data.email
                first_name=data.first_name
                last_name=data.last_name
                context = { 'name':name,'email':email,'first_name':first_name,'last_name':last_name, 'message':'You are Already Logged IN','f':1 }
                return render(request,'myapp/profile.html',context)
        else:
                error = "Either UserName Or Password is invalid Try Again"
                return  render(request,'myapp/login.html',{'error':error})

    else :

        return render(request,'myapp/login.html',context)



def logout(request):

    if request.method == 'POST':

        del request.session['username']
        del request.session['password']

        return render(request,'myapp/home.html')

    else:

        return render(request,'myapp/login.html',{ 'error':"Form Should be POST Type" })




def signup(request):

    if request.method == 'POST':


        form = signup_form(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']



            try:
                    user = User.objects.get(username=name)
                    myerror = "User already Exist so Please Login.If not register then choose other username"
                    context = { 'error':myerror}
                    return render(request,'myapp/login.html',context )
            except:

                    u = User.objects.create_user(username=name,password=password)
                    u.email=email
                    u.first_name=first_name
                    u.last_name=last_name


                    request.session['username']=name
                    request.session['password']=password

                    u.save()

                    context = { 'name':name,'email':email,'first_name':first_name,'last_name':last_name,'message':"You Have Created your Account Successfully",'f':1}
                    return render(request,'myapp/profile.html',context)



            #return HttpResponse("Name = %s<br />Email = %s<br />password = %s<br />"%(name,email,password))
        else:
            error = "Form data is invalid  Please try again "
            return render(request,'myapp/login.html',{'error':error})

    else :
        error = "Invalid Entries in Form,Please Make sure all entries are correct"
        return render(request,'myapp/login.html',{'error':error})



def profile(request):

    if 'username' in request.session:

        uname=request.session['username']
        passwd=request.session['password']
        res=authenticate(username=uname,password=passwd)

        if res is not None :

                name=request.session['username']
                data=User.objects.get(username=name)
                name=data.username
                email=data.email
                first_name=data.first_name
                last_name=data.last_name
                form = userprofile_form()
                context = { 'name':name,'email':email,'first_name':first_name,'last_name':last_name, 'message':'','f':1,'form':form }
                return render(request,'myapp/profile.html',context)
        else:
                error = "Either UserName Or Password is invalid Try Again"
                return  render(request,'myapp/login.html',{'error':error})

    else :

        context = {'error':"Please Login First"}
        return render(request,'myapp/login.html',context)


def adduser(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            #name=str(name).strip()
            password=form.cleaned_data['password']
            #password=str(password).strip()
            user = authenticate(username=name,password=password)
            if user is not None:
                data=User.objects.get(username=name)
                name=data.username
                email=data.email
                first_name=data.first_name
                last_name=data.last_name
                context = { 'name':name,'email':email,'first_name':first_name,'last_name':last_name, 'message':'Welcome Back to Your Profile','f':1 }
                request.session['username']=name
                request.session['password']=password
                return render(request,'myapp/profile.html',context)
            else:
                error = "Either UserName Or Password is invalid Try Again"
                return  render(request,'myapp/login.html',{'error':error})
        else :
            error = "Invalid Entries in Form,Please Make sure all entries are correct"
            return render(request,'myapp/login.html',{'error':error})



def contact(request):
    if 'username' in request.session:

        f = 1
    else :

        f = 0
    context = { 'f':f }

    return render(request,'myapp/contact.html',context)


def wedding(request):
    if 'username' in request.session:

        f = 1
    else :

        f = 0
    context = { 'f':f }

    return render(request,'myapp/wedding.html',context)




def reset_password(request):

    if request.method == 'POST':

        form = reset_form(request.POST)

        if form.is_valid():

            otp = []
            for var in range(4):

                otp.append(str(randint(0,9)))

            otp = ''.join(otp)

            message = "Hey Check this out \nYour OTP for reset password is %s "%(otp)

            subject = "Reset Password"
            from_email = "3496.grras@gmail.com"

            to_email = form.cleaned_data['email']
            send_mail(subject, message, from_email, (to_email,),auth_password = settings.EMAIL_HOST_PASSWORD,fail_silently=False)
            request.session['OTP']=int(otp)
            request.session['email']=to_email

            form = password()
            return render(request,'myapp/change_password.html',{ 'form':form })

        else:

            form = reset_form()

        return render(request,'myapp/reset_password.html',{'form':form})
    else:

        form = reset_form()
        return render(request,'myapp/reset_password.html',{'form':form})


def update_password(request):

    if request.session['OTP'] and request.session['email']:

        if request.method == 'POST':

            form = password(request.POST)

            if form.is_valid():

                otp = request.session['OTP']

                OTP = form.cleaned_data['OTP']

                if otp == OTP :

                    obj = User.objects.get(email=request.session['email'])

                    obj.set_password(form.cleaned_data['new_password'])
                    obj.save()

                    del request.session['email']
                    del request.session['OTP']
                    request.session['username'] = obj.username
                    request.session['password'] = form.cleaned_data['new_password']


                    name=obj.username
                    email=obj.email
                    first_name=obj.first_name
                    last_name=obj.last_name
                    context = { 'name':name,'email':email,'first_name':first_name,'last_name':last_name, 'message':'Welcome Back to Your Profile','f':1 }

                    return render(request,'myapp/profile.html',context)

                else:

                    error = "OTP Does Not Match Try Again"
                    return render(request,'myapp/change_password.html',{'error':error})

            else:

                error = "Form Details is invalid"
                return render(request,'myapp/login.html',{'error':error})

        else:

                error = "Form Details is invalid"
                return render(request,'myapp/login.html',{'error':error})

    else:

            error = "Form Details is invalid"
            return render(request,'myapp/login.html',{'error':error})


def upload_pic(request):

    if request.method == 'POST' :

        form = userprofile_form(request.POST,request.FILES)

        if form.is_valid():

            m = UserProfile.objects.get(pk=1)






