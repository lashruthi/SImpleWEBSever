from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Name: Lashruthi</h1><h2>Register Number: 26019175</h2>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]