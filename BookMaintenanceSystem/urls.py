from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

import book.views as bviews
import account.views as aviews

urlpatterns = [
    
    path("admin/", admin.site.urls),
    
    path("", bviews.search),
    # path("create/", bviews.create),
    # path("edit/", bviews.edit),
    # path("details/", bviews.details),
    # path("lend_record/", bviews.lend_record),
    
    path("login/", aviews.sign_in),
    path("log_out/", aviews.log_out),
    path("register/", aviews.register),
    
]
