from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from .forms import myData
import pytesseract
from PIL import  Image
from .textextract import handle_uploaded_file
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import signup_form,login_form,reset_form,password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from random import randint
from django.conf import settings
import urllib.parse
import requests
import json


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def home(request):
     if 'username' in request.session:
        form = myData()
        return render(request,'home.html',{ 'form' : form })
     else :
         error = "Please Login First To Access"
         return render(request,'index.html',{'error':error})

def index(request):

     if 'username' in request.session:

        return redirect('http://localhost/home')
     else :

        return render(request,'index.html')


def new(request):
    form = myData()
    return render(request,'new.html',{'form':form})

def extract(request):
    if request.method == 'POST':
        form = myData(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['image'])
            if  form.cleaned_data['english'] and form.cleaned_data['hindi']  :
                f = myData()
                return render(request,'home.html',{'form':f,'error':'Choose Only One Language '})
            elif not(form.cleaned_data['english']) and not(form.cleaned_data['hindi']) :
                 f = myData()
                 return render(request,'home.html',{'form':f,'error':'Choose Atleast One Language '})

            elif form.cleaned_data['english'] :
                result = pytesseract.image_to_string(Image.open("static/new.png"),lang='eng')
            elif form.cleaned_data['hindi'] :
                result = pytesseract.image_to_string(Image.open("static/new.png"),lang='hin')

            main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
            address = result
            url = main_api + urllib.parse.urlencode({'address':address})
            json_data = requests.get(url).json()
            try :
                addr = json_data["results"][0]["formatted_address"]
                try :

                    ln = json_data["results"][0]["geometry"]["bounds"]["northeast"]["lng"]
                    lt  = json_data["results"][0]["geometry"]["bounds"]["northeast"]["lat"]
                    result += '\n\n\nAddress = %s\nLongitude = %s \n Latitude = %s '%(addr,ln,lt)
                except :
                    try :
                        address = addr.split()[-1]
                        url = main_api + urllib.parse.urlencode({'address':address})
                        json_data = requests.get(url).json()

                        ln = json_data["results"][0]["geometry"]["bounds"]["northeast"]["lng"]
                        lt  = json_data["results"][0]["geometry"]["bounds"]["northeast"]["lat"]
                        result = result+'\n\n\nAddress = %s\nLongitude = %s \n Latitude = %s '%(addr,ln,lt)
                    except :
                        result = result+'\n\nAddress = %s'%(addr)
            except:
                result = result+'\n\nNo Location Found'



            f = open('static/result.txt','wb')
            f.write(result.encode('utf-8'))
            f.close()
            result = result.split('\n')
            return render(request,'success.html',{'result':result})
    else:
        form = myData()
    return render(request, 'home.html', {'form': form})

def success(request):
    return HttpResponse('success')






def signup(request):

    if request.method == 'POST':


        form = signup_form(request.POST)

        if form.is_valid():
            Name = form.cleaned_data['username']
            FName=form.cleaned_data['first_name']
            LName=form.cleaned_data['last_name']
            Email=form.cleaned_data['email']
            Password=form.cleaned_data['password']



            try:
                    Name = User.objects.get(username=Name)
                    myerror = "User already Exist so Please Login.If not register then choose other username"
                    context = { 'error':myerror}
                    return render(request,'index.html',context)
            except:

                    u = User.objects.create_user(username=Name,password=Password)
                    u.email=Email
                    u.first_name=FName
                    u.last_name=LName


                    request.session['username']=Name
                    request.session['password']=Password

                    u.save()

                    return redirect('http://localhost/home')



            #return HttpResponse("Name = %s<br />Email = %s<br />password = %s<br />"%(name,email,password))
        else:
            error = "Form data is invalid  Please try again "
            return render(request,'index.html',{'error':error})

    else :
        error = "Invalid Entries in Form,Please Make sure all entries are correct"
        return render(request,'index.html',{'error':error})

def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect('http://localhost')




def login(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            #name=str(name).strip()
            password=form.cleaned_data['password']
            #password=str(password).strip()
            user = authenticate(username=name,password=password)
            if user is not None:
                error =  'Welcome Back %s.'%(name)
                request.session['username']=name
                request.session['password']=password
                return redirect('http://localhost/home',{'error':error})
            else:
                error = "Either UserName Or Password is invalid Try Again"
                return  render(request,'index.html',{'error':error})
        else :
            error = "Invalid Entries in Form,Please Make sure all entries are correct"
            return render(request,'index.html',{'error':error})



def forgot(request):

    form = reset_form()
    return render(request,'reset.html',{'form':form})

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

            try :
                obj = User.objects.get(email=to_email)
                send_mail(subject, message, from_email, (to_email,),auth_password = settings.EMAIL_HOST_PASSWORD,fail_silently=False)
                request.session['OTP']=int(otp)
                request.session['email']=to_email
                form = password()
                error = "Check Your Mail For OTP"
                return render(request,'reset_password.html',{ 'form':form,'error':error})
            except :

                error = "Email Does not Exist in Our Database Try Again"
                form = reset_form()
                return redirect('http://localhost/forgot',{'form':form,'error':error})

        else:
            error = "Email Does not Exist in Our Database Try Again"
            form = reset_form()

        return render(request,'reset.html',{'form':form,'error':error})
    else:
        error = "Email Does not Exist in Our Database Try Again"
        form = reset_form()
        return render(request,'reset.html',{'form':form,'error':error})


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


                    error = "Welcome Back mr %s."%(obj.username)
                    return redirect('http://localhost/home')

                else:

                    error = "OTP Does Not Match Try Again"
                    return render(request,'reset_password.html',{'error':error})

            else:

                error = "Form Details is invalid"
                return render(request,'reset_password.html',{'error':error})

        else:

                error = "Form Details is invalid"
                return render(request,'myapp/login.html',{'error':error})

    else:

            error = "Form Details is invalid"
            return render(request,'myapp/login.html',{'error':error})
