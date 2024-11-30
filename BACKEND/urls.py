from django.urls import path
from . import views

urlpatterns = [

    path('/home',views.home, name = 'home'),
     path('', views.login_view, name='login'),
    path('/register_maps', views.register_maps, name='register_maps'),
    path('register/owner/', views.register_owner, name='register_owner'),
    path('register/seller/', views.register_seller, name='register_seller'),
    path('register/deal/', views.register_deal, name='register_deal'),
    path('success/', views.success, name='success'),
]
