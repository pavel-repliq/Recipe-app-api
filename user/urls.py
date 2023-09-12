"""
   urls mapping for user app 
"""
from django.urls import path
from user.views import *

app_name = "user"
urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create"),
    path("token/", UserAuthTokenView.as_view(), name="token"),
]
