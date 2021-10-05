
# Create your views here.
from django.http import HttpResponse
 
def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)
 
 
def login(request):
   text = """<h1>Login</h1> User name: <input type="text" nam="user" /> <BR> Password: <input type="password" nam="password" /> """
   return HttpResponse(text)