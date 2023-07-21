from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
     number={
         'num1':[1,2,3,4,5,6,7,8,9,10]
     }
     return render(request,'index.html',number)
def about(request):
    return render(request,'about.html')
def doctors(request):
    return render(request,'doctors.html')
def contact(request):
    return render(request,'contact.html')