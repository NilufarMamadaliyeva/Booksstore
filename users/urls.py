from django.urls import path
from .views import UserRegisterView, CustomUserLogin, LogoutView, homepage_view, profile_view, update_profile



app_name = 'users'
urlpatterns = [
  path('register/', UserRegisterView.as_view(), name='register'),
  path('', CustomUserLogin.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('home/',homepage_view,name='home'),
  path('profile/',profile_view,name='profile'),
  path('profile_update/',update_profile,name='update-profile')

]
