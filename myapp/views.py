from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from myapp.models import *
from myapp.serializers import *



# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

# Create your views here.
class StoreViewSet(viewsets.ModelViewSet):
    queryset = store.objects.all()
    serializer_class = StoreSerializer


# Create your views here.
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Create your views here.   
def home(request):
    return HttpResponse("Home page")
    
def hiname(request, username):
    return HttpResponse("Hi " + username)
    
def age(request, year):
    return HttpResponse("Age: " + str(year))
    
def hello_view(request):
    fourSeason = range(1, 5)
    p1={"name":"Amy","phone":"0912-345678","age":20}
    p2={"name":"Jack","phone":"0937-123456","age":25}
    p3={"name":"Nacy","phone":"0958-654321","age":17}
    persons=[p1,p2,p3]
    return render(request, 'hello_django.html', {
        'title':"樣板使用",
        'data':"Hello Django!",
        'seasons':fourSeason,
        'persons':persons,
        'now':datetime.now()
    } )


def home(request):
    
    return render(request,'home.html')

def about(request):
    
    return render(request,'about.vue')
def index(request):
    return HttpResponse("Home page")
# Create your views here.



