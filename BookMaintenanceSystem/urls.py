"""BookMaintenanceSystem URL Configuration

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
from django.urls import path

import book.views as bviews
import account.views as aviews

urlpatterns = [
    
    path("admin/", admin.site.urls),
    
    path("", bviews.search),
    path("create/", bviews.create),
    path("edit/", bviews.edit),
    path("details/", bviews.details),
    path("landRecord/", bviews.landRecord),
    
    path("login/", aviews.sign_in),
    path("log_out/", aviews.log_out),
    path("register/", aviews.register),
    
]
