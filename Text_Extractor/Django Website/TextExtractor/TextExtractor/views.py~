from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import myData
import pytesseract
from PIL import  Image
from .textextract import handle_uploaded_file
import smtplib
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import signup_form
from django.contrib.auth.models import User
from django.contrib.auth    import authenticate
from .models import UserProfile

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def home(request):
    form = myData()
    return render(request,'home.html',{ 'form' : form })

def index(request):
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
            Name = form.cleaned_data['Name']
            FName=form.cleaned_data['FName']
            LName=form.cleaned_data['LName']
            Email=form.cleaned_data['Email']
            Password=form.cleaned_data['Password']



            try:
                    Name = User.objects.get(username=Name)
                    myerror = "User already Exist so Please Login.If not register then choose other username"
                    context = { 'error':myerror}
                    return render(request,'/',context )
            except:

                    u = User.objects.create_user(username=Name,password=Password)
                    u.email=Email
                    u.first_name=FName
                    u.last_name=LName


                    request.session['username']=Name
                    request.session['password']=Password

                    u.save()

                    return render(request,'/home')



            #return HttpResponse("Name = %s<br />Email = %s<br />password = %s<br />"%(name,email,password))
        else:
            error = "Form data is invalid  Please try again "
            return render(request,'myapp/login.html',{'error':error})

    else :
        error = "Invalid Entries in Form,Please Make sure all entries are correct"
        return render(request,'myapp/login.html',{'error':error})
