from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Employee
from .models import Product,Product2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.conf import settings
from django.core.mail import send_mail
import random


def index(request):
    #return HttpResponse("<h1>This is Blog Home Page</h1>")
    return render(request,'blog/index.html')

def about(request):
    #return HttpResponse("<h1>This is Blog About Page</h1>")
    return render(request,'blog/about.html')
def Home(request):
    #return HttpResponse("<h1>This is Blog About Page</h1>")
    return render(request,'blog/Home.html')
def getform(request):
    return render(request,'blog/reg.html')
def getdata(request):
    btn=request.GET.get("sub")
    if btn=="Insert":
        e_name=request.GET.get("ename")
        eloc=request.GET.get("eloc")
        esal=request.GET.get("esal")
        data=Employee(ename=e_name,eloc=eloc,esal=esal)
        data.save()
        param={"msg":"Record Inserted Successfully..."}
        return render(request,'blog/reg.html',param)
    if btn=="Display":
        record=Employee.objects.all()
        param={'data':record}
        return render(request,'blog/reg.html',param)

def more(request):
    record = Employee.objects.all()

    param={'data1':record}
    return render(request,"blog/one.html",param)


def moredata(request):
    btn=request.GET.get("sub")
    ename=request.GET.get("ename")
    if(btn=="Display"):
        record=Employee.objects.get(ename=ename)
        record1=Employee.objects.all()

        param={'data':record,'data1':record1}
        return render(request,"blog/one.html",param)

    if(btn=="Delete"):
        record=Employee.objects.filter(ename=ename).delete()
        record1=Employee.objects.all()

        param={'msg':'Record Deleted Successfully...','data1':record1}
        return render(request,'blog/one.html',param)
    if(btn=="Edit"):
        record = Employee.objects.get(ename=ename)

        param = {'data': record}
        return render(request, "blog/edit.html", param)

def getupdate(request):
    e_name = request.GET.get("ename")
    eloc = request.GET.get("eloc")
    esal = request.GET.get("esal")
    record=Employee.objects.get(ename=e_name)
    record1 = Employee.objects.all()

    record.eloc=eloc
    record.esal=esal
    record.save()
    param={"msg":"Record Updated Successfully..",'data1':record1}
    return render(request,"blog/one.html",param)

def action(request):
    ename=request.GET.get("name")
    record = Employee.objects.filter(ename=ename).delete()

    param = {'msg': 'Record Deleted Successfully...'}
    return render(request, 'blog/reg.html', param)

def action2(request):
    ename=request.GET.get("name")
    record = Employee.objects.get(ename=ename)

    param = {'data': record}
    return render(request, "blog/edit.html", param)

def checkk(request):
    return render(request,'blog/check.html')

def product(request):
    return render(request,'blog/product.html')

def getproduct(request):
    btn=request.GET.get("Productname")
    pname=request.GET.get("pname")

    if btn=="Productname":
        record=Product.objects.get(pname=pname)

        param={'data':record}
        return render(request,'blog/product.html',param)

def usersignup(request):
    return render(request,"blog/usersignup.html")

def userdata(request):
    username=request.POST.get("uname")
    password=request.POST.get("pass")
    email=request.POST.get("email")
    myuser=User.objects.create_user(username,email,password)
    myuser.save()
    return render(request,"blog/userlogin.html")
def userlogin(request):
    return render(request,"blog/userlogin.html")

def usercheck(request):
    username = request.POST.get("uname")
    password = request.POST.get("pass")

    user=authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('Home')
    else:
        return redirect('userlogin')

def userlogout(request):
    logout(request)
    return redirect('userlogin')
def upload_form(request):
    return render(request,"blog/upload.html")

def uploadimg(request):
    btn=request.POST.get("sub")
    if(btn=="Upload"):
        prod=Product2()
        prod.product_name=request.POST.get("pname")
        prod.product_category=request.POST.get("pcat")
        prod.product_price=request.POST.get("price")
        prod.product_date=request.POST.get("date")

        if(len(request.FILES)!=0):
            prod.product_image=request.FILES['f']
        prod.save()
        pram={"msg":"Upload Successfujlly...."}
        return render(request,"blog/upload.html",pram)
    if btn=="Display":
        record = Product2.objects.all()
        param = {'data': record}
        return render(request, "blog/upload.html", param)

def form(request):
    return render(request,"blog/form.html")



def sendmail(request):
    subject = request.POST.get("subject")
    otp = random.randint(1000, 9999)
    message = request.POST.get("message")
    message=f'{message}{otp}'
    email_from = settings.EMAIL_HOST_USER

    recipient_list = [request.POST.get("recipient_list")]
    send_mail(subject, message, email_from, recipient_list)
    param = {"msg": "sent Successfujlly....","otp":otp}

    return render(request, "blog/otpverify.html", param)

def verifyotp(request):
    otp=request.GET.get("otp")
    userotp=request.GET.get("userotp")
    if(otp==userotp):
        param={"msg":"Suucessfully Verify OTP..."}
        return render(request,"blog/reset.html",param)
    else:
        param = {"msg": "Not Match  OTP...","otp":otp}
        return render(request, "blog/otpverify.html", param)



def form2(request):
    return render(request,"blog/form2.html")


def sendmail2(request):
    subject ="Reset Password"
    otp = random.randint(1000, 9999)
    message = "OTP :"
    message=f'{message}{otp}'
    email_from = settings.EMAIL_HOST_USER
    request.session['email']=request.POST.get("recipient_list")
    recipient_list = [request.POST.get("recipient_list")]
    send_mail(subject, message, email_from, recipient_list)
    param = {"msg": "sent Successfujlly....","otp":otp}

    return render(request, "blog/otpverify.html", param)

def resetpass(request):
    npass=request.POST.get("password")
    email=request.session['email']
    #print(email,request.user)
    record = User.objects.get(email=email)
    #print(record.password)
    record.set_password(npass)

    record.save()
    return render(request,"blog/usersignup.html")
def ajax(request):
    return render(request,"blog/ajax.html")
def create(request):
    e_name = request.POST.get("ename")
    eloc = request.POST.get("eloc")
    esal = request.POST.get("esal")
    data = Employee(ename=e_name, eloc=eloc, esal=esal)
    data.save()

    return redirect('ajax')
def ajaxdisplay(request):
    record=list(Employee.objects.all().values())
    data=dict()
    data['dt']=record
    #return render(request,"blog/ajax.html",param);
    print(record)
    return JsonResponse(data)

def delete(request):
    eid=request.GET.get("eid")
    Employee.objects.filter(id=eid).delete()
    return render(request,"blog/ajax.html")