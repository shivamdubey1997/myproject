from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('getform',views.getform,name='getform'),
    path('getdata',views.getdata,name="getdata"),
    path("more",views.more,name="more"),
    path("moredata",views.moredata,name="moredata"),
    path("getupdate",views.getupdate,name="getupdate"),
    path('Home',views.Home,name="Home"),
    path("action",views.action,name="action"),
    path("action2", views.action2, name="action2"),
    path("checkk", views.checkk, name="checkk"),
    path("product", views.product, name="product"),
    path("getproduct", views.getproduct, name="getproduct"),
    path("usersignup",views.usersignup,name="usersignup"),
    path("userdata",views.userdata,name="userdata"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("usercheck",views.usercheck,name="usercheck"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("upload_form",views.upload_form,name="upload_form"),
    path("uploadimg",views.uploadimg,name="uploadimg"),
    path("sendmail",views.sendmail,name="sendmail"),
    path("form", views.form, name="form"),
    path("form2", views.form2, name="form2"),
    path("sendmail2",views.sendmail2,name="sendmail2"),
    path("verifyotp",views.verifyotp,name="verifyotp"),
    path("resetpass",views.resetpass,name="resetpass"),
    path("ajax",views.ajax,name="ajax"),
    path("create",views.create,name="create"),
    path("ajaxdisplay",views.ajaxdisplay,name="ajaxdisplay"),
    path("delete",views.delete,name="del")

]
