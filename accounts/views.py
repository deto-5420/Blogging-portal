from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,UserUpdateForm
# Create your views here.
def logout(request):
  auth.logout(request)
  return redirect('/posts/')
def login(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('/posts/')
    else:
      messages.info(request,'invalid Credentials') 
      return redirect('/posts/accounts/login')  

  else:
    return render(request,'accounts/login.html')
def register(request):
  if request.method=='POST':

    print(10)
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    password1=request.POST['password1']
    
    if  password== password1:
      if User.objects.filter(username=username).exists():
        messages.info(request,'Username taken')
        return redirect('/posts/accounts/register')
      elif User.objects.filter(email=email).exists():
        messages.info(request,"Email taken") 
        return redirect('/posts/accounts/register')     
      else: 
        user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save(); 
        print('user created')
        
    
     
    else:
      print(" password not matching ")
      return redirect('/posts/account/register')

    return redirect('/posts/accounts/login')  

  else:
    
    return render(request,'accounts/register.html')
@login_required  
def profile(request):
  
  if request.method=='POST':
    user_f=UserUpdateForm(request.POST,instance=request.user)
    profile_f=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    if user_f.is_valid and profile_f.is_valid:
      user_f.save()
      profile_f.save()
      messages.success(request,f'account updated')
      return redirect('profile')
  else:
    user_f=UserUpdateForm()
    profile_f=ProfileUpdateForm(('POST' or None))
  context={
     'user_f': user_f,
     'profile_f': profile_f
  }
  return render(request,'accounts/profile.html',context)
