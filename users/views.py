from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreateForm, UpdateProfileForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def homepage_view(request):
    return render(request,'home.html')
  
def profile_view(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request,'profile.html',context=context)
  
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request,'profile.html',{'form':form})
  

class UserRegisterView(View):
  def get(self, request):
    create_form = CustomUserCreateForm()
    context = {
      'form': create_form
    }
    return render(request, template_name='register.html', context=context)
  
  def post(self,request):
    create_form = CustomUserCreateForm(request.POST)
    if create_form.is_valid():
      create_form.save()
      return redirect('login')
    else:
      context = {
      'form': create_form
    }
    return render(request, template_name='register.html', context=context)
     
  
  # def post(self, request):
  #   username = request.POST['username']
  #   first_name = request.POST['first_name']
  #   last_name = request.POST['last_name']
  #   email = request.POST['email']
  #   password = request.POST['password']
    
  #   user = CustomUser.objects.create(
  #     username=username,
  #     first_name=first_name,
  #     last_name=last_name,
  #     email=email
  #   )
  #   user.set_password(password)
  #   user.save()

# class ProfilView(View):
#   def get(self,request):
#     return render(request, template_name='users/profile.html' context=context)
  
class CustomUserLogin(View):
    def get(self, request):
      login_form = AuthenticationForm()
      context = {
      'form': login_form
       }
      return render(request, template_name='login.html', context=context)
      
    def post(self, request):
      data = AuthenticationForm(data=request.POST)
      data.is_valid()
      user = data.get_user()
      login(request, user)
      return redirect('home')
    
class LogoutView(View):
  def get(self, request):
    logout(request)
    return render(redirect, 'login')
  