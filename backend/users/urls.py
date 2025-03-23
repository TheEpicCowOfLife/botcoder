from django.urls import path
from knox.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', views.UserView.as_view(), name='user'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
] 