from django.contrib import admin
from django.urls import path , include
from rest import views

urlpatterns = [
    path('',views.ind,name='main'),
    path('log/',views.signed ,name='loge'),
    path('sign/',views.loginic,name='lo'),
    path('out/',views.getout,name='o'),
    path('cart/<str:pk>/' ,views.cart, name='cart' ),
    path('rem/<str:pk>/' ,views.remo, name='re' ),
    path('payment/<str:pk>/' ,views.pay, name='pay' ),
    path('off/<str:pk>/' ,views.offer, name='off' ),
    path('your_cart' ,views.your_cart, name='your_c' ),

]