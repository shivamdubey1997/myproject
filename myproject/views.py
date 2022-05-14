from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>This is My Home Page</h1> <a href='contact'> contact </a> || <a href='about'>About</a>")
def about(request):
    x=100
    html="<h1>This is My About Page</h1> <a href='home'> Home </a> || <a href='contact'>Contact</a>",x
    return HttpResponse(html)
def contact(request):
    return HttpResponse("<h1>This is My Contact Page</h1> <a href='home'> Home </a> || <a href='about'>About</a>")
def ssd(request):
    return HttpResponse("<h1>code with us</h1>")