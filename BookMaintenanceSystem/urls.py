from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

import book.views as bviews
import account.views as aviews

urlpatterns = [
    
    path("admin/", admin.site.urls),
    
    path("", bviews.search,name="Book"),
    path("create/", bviews.create,name="create"),
    path("edit/<int:pk>/", bviews.edit,name="edit"),
    path("detail/<int:pk>/", bviews.detail,name="detail"),
    path("delete/<int:pk>/", bviews.delete,name="delete"),
    path("lend_record/<int:pk>/", bviews.lend_record,name="lend_record"),
    
    path("login/", aviews.sign_in,name="Login"),
    path("log_out/", aviews.log_out,name="Logout"),
    path("register/", aviews.register,name="Sign_up"),
    
]
