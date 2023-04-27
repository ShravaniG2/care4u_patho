from django.contrib import admin
from django.urls import path,include 
from home import views
from . import views
from .views import logout



urlpatterns = [
    path("", views.firstpage, name='home'),
    path("cart", views.cart , name='cart'),
    path("login", views.login_p , name='login'),
    path("logout", views.logout_p, name='logout'),
    path("register", views.register , name='register'),
    #path("homepage", views.homepage , name='login'),
    #path("profile", views.profile , name='profile'),
    #path("profile/relatives", views.relatives , name='relatives'),
    #path("parivar", views.parivar , name='parivar'),
    #path("plejwork", views.plejwork , name='plejwork'),
    path("userprofile", views.userprofile , name='userprofile'),
    path("userprofile/edit_profile", views.edit_profile , name='edit_profile'),
    path("userprofile/edit_relatives/<int:id>", views.edit_relatives , name='edit_relatives'),


    path("userprofile/relatives", views.relatives , name='relative'),
    path("userprofile/orderhistory", views.orderhistory , name='orderhistory1'),
    path("userprofile/appointment", views.appointment_p , name='appointment'),
    path("userprofile/appointment_history", views.appointment_history , name='appointment_history'),
    path("cart/payment_p", views.payment_p , name='payment_p'),





    path("forgetpassword", views.forgertpassword , name='forgertpassword'),
    path("about", views.about , name='about'),
    path("feedback", views.feedback_u , name='feedback'),
    path("register_a", views.register_a , name='register_a'),
    path("login_a", views.login_a , name='login'),

    path("testpage/<int:id>",views.testpage,name='testpage'),
    path("packagepage/<int:id>",views.packagepage,name='packagepage'),

    path("search",views.search,name='search'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),



]