from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Faculty,Services
from .forms import BookingForm,UpdationForm

# def dect(func):
#      def inner(request):
#           func(request)
#           return HttpResponse("You are loged in")
#      return inner 
# Create your views here.
#@login_required(login_url='login_user')
# @dect
def home(request):
     return render(request,"home.html")
#     if 'username' in request.session:
#          return render(request,"home.html")     
#     return redirect(login_user)
    



def register(request):
        if request.method == 'POST':
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            username=request.POST["username"]
            email=request.POST["email"]
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if password==confirm_password :
                 if User.objects.filter(username=username).exists():
                      messages.info(request,'Username not available!')
                      return redirect(register)
                 elif User.objects.filter(email=email).exists():
                      messages.info(request,'email entered has an existing account please login to acces!')
                      return redirect(register)
                 else:
                      user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                      user.set_password(password)
                      #user.is_staff=True
                      user.save()
                      messages.info(request,'Account Created')
                      return redirect('login_user')
            else:
               messages.info(request,'passwords does not match')
               return redirect(register)
            
        else:
             print("This is not post method")
             return render(request,"register.html")




@user_passes_test(lambda u:u.is_superuser,login_url='home')
def adminregister(request):
        if request.method == 'POST':
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            username=request.POST["username"]
            email=request.POST["email"]
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if password==confirm_password :
                 if User.objects.filter(username=username).exists():
                      messages.info(request,'Username not available!')
                      return redirect(adminregister)
                 elif User.objects.filter(email=email).exists():
                      messages.info(request,'email entered has an existing  superuser!')
                      return redirect(adminregister)
                 else:
                      user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                      user.set_password(password)
                      user.is_staff=True
                      user.is_superuser=True
                      user.save()
                      messages.info(request,'Account Created')
                      return redirect('adminpanel')
            else:
               messages.info(request,'passwords does not match')
               return redirect(adminregister)
            
        else:
             print("This is not post method")
             return render(request,"adminregister.html")


def login_user(request):
     if 'username' in request.session:
          return redirect(home)
     if request.method == 'POST': 
          username =request.POST['username'] 
          password = request.POST['password'] 
          user = auth.authenticate(username=username, password=password) 
          if user is not None:
               request.session['username']=username 
               auth.login(request, user) 
               return render(request,'home.html')
          else: 
               messages.info(request,'Invalid Username or Password') 
               return render(request, 'login.html') 
     else: 
          return render(request, 'login.html')
def logout_user(request):
     if 'username' in request.session:
          request.session.flush() 
     #auth.logout(request) 
     return redirect('login_user')
# def department(request):
#      dict_dep={'dep':Department.objects.all()}
#      return render(request,dict_dep)
@login_required(login_url='login_user')
def contact(request):
     return render(request,'contact.html')
     # if 'username' in request.session:
     #      return render(request,'contact.html')
     # return redirect(login_user)     

@login_required(login_url='login_user')
def faculty(request):
     dict_faculty={'facu':Faculty.objects.all()}
     return render(request,'faculty.html',dict_faculty)
     # if 'username' in request.session:
     #      return render(request,'faculty.html',dict_faculty)
     # return redirect(login_user)



@login_required(login_url='login_user')
def Our_services(request):
     dict_service={'service':Services.objects.all()}
     if 'username' in request.session:
          return render(request,'Our Services.html',dict_service)
     return redirect(login_user)

@login_required(login_url='login_user')
def Book(request):
     if request.method=='POST':
          form=BookingForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request,'confirmation.html')

     form=BookingForm()
     dict_form={'form':form}
     
     return render(request,'bookservice.html',dict_form)
     
@user_passes_test(lambda u:u.is_superuser,login_url='home')
def adminpanel(request):
     if 'username' in request.session:
          context= {'allusers': User.objects.all().order_by('id')}
          return render(request,'adminpanel.html',context)
     return redirect(login_user)

#@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@user_passes_test(lambda u:u.is_superuser,login_url='home')
def DeleteUser(request,id):
    if request.method =='POST':
        dele=User.objects.get(pk=id)
        dele.delete()
        messages.info(request,'Deleted Successfully')
    return redirect('adminpanel')


#@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@user_passes_test(lambda u:u.is_superuser,login_url='home')
def Useredit(request,id):
    if request.method =='POST':
        query1= User.objects.get(pk=id)
        query2= UpdationForm(request.POST,instance=query1)
        if query2.is_valid():
            query2.save()
            messages.info(request,'Edit successful')
            return redirect(adminpanel)
    else:
        query1 = User.objects.get(pk=id)
        query2 = UpdationForm(instance=query1)
    return render(request,'useredit.html',{'form':query2})

@login_required(login_url='login_user')
def SearchName(request): 
    searched=request.GET['search']
    searchnames=User.objects.filter(username__icontains=searched)
    return render(request,'adminpanel.html',{'allusers':searchnames})

@login_required(login_url='login_user')
def confirmation(request):
     return render(request,'confirmation.html')

