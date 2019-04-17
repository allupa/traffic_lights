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
    path('password/', views.change_password, name='change_password'),
    path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),
    path('home/trafficdata/', views.api, name='trafficdata'),
    path('home/trafficdata/map', views.map, name='map'),
  #  path('home/trafficdata/data'), views.apidata, name='datadata'),
    url(r'^accounts/profile/delete/(?P<username>[\w|\W.-]+)/$', views.delete_profile, name='delete_profile'),
    ]


    #path('change-password/', auth_views.PasswordChangeView.as_view()),

    #

    #path('sensors/',  views.sensor_list, name='sensor_list'),
    #path('sensors/new', views.sensor_create, name='sensor_new'),
    #url(r'^edit/(?P<pk>\d+)$', views.sensor_update, name='sensor_edit'),
    #url(r'^delete/(?P<pk>\d+)$', views.sensor_delete, name='sensor_delete'), 
    #path('sensors/', views.SensorList.as_view(template_name='sensors/sensor_list.html')),
    #path('sensor/<int:pk>', views.SensorDetail.as_view(), name='sensor_detail'),
    #path('create/', views.SensorCreate.as_view(), name='sensor_create'),
    #path('update/<int:pk>', views.SensorUpdate.as_view(), name='sensor_update'),
    #path('delete/<int:pk>', views.SensorDelete.as_view(), name='sensor_delete'),