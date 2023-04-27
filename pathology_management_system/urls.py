"""pathology_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  django.contrib.auth.models  import  Group
from django.conf import settings
from django.conf.urls.static import static


admin.site.unregister(Group) #remove group model from django admin

admin.site.site_header = "Pathology Admin"   #change text of django admin
admin.site.index_title = "Welcome to Pathology Administration"
admin.site.site_title = "Pathology Administration"

urlpatterns = [            #adds different pages to the website
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    #path('profile/', include('home.urls')),
    path('userprofile/edit_profile/', include('home.urls')),
    path('edit_relatives/', include('home.urls')),


    path('relatives/', include('home.urls')), 

    #path('parivar/', include('home.urls')),
    path('plejwork/', include('home.urls')),
    path('userprofile/', include('home.urls')),
    path('orderhistory2/', include('home.urls')),
    path('appointment/', include('home.urls')),
    path('appointment_history/', include('home.urls')),


    path('cart/', include('home.urls')),
    path('register/', include('home.urls')),
    path('login/', include('home.urls')),
    #path('homepage/', include('home.urls')),
    path('forgetpassword/', include('home.urls')),
    path('about/', include('home.urls')),
    path('feedback/', include('home.urls')),
    path('register_a/', include('home.urls')),
    path('login_a/', include('home.urls')),

    path('test_page/', include('home.urls')),
    path('testpage/',include('home.urls')),
    path('packagepage/',include('home.urls')),

    path('', include('home.urls')),
    



] 

