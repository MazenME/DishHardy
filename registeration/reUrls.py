from django.urls import path
from . import views


from django.urls import path
from . import views



urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),  
    path('homeuser',views.homeuser,name='homeuser'),
    path('homeadmin',views.homeadmin,name='homeadmin'),
 
]
