from django.shortcuts import render
from datetime import datetime
from myapp.models import Dreamreal
from myapp.forms import LoginForm

# Create your views here.

from django.http import HttpResponse

#def hello(request):
#   text = """<h1>welcome to my app !</h1>"""
#   return HttpResponse(text)


def hello(request):
   today = datetime.now().date()
#   return render(request, "hello.html", {"today" : today})
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticles(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)

def datamanipulation(request):
   res = ''
   
   #Filtering data:
   qs = Dreamreal.objects.filter(name = "paul")
   res += "Found : %s results<br>"%len(qs)
   
   #Ordering results
   qs = Dreamreal.objects.order_by("name")
   
   for elt in qs:
      res += elt.name + '<br>'
   
   return HttpResponse(res)

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'loggedin.html', {"username" : username})

