from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.comment, name='comment'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('accounts/profile/', views.profile, name='profile'),
    ]