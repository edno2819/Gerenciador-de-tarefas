from django.urls import path, include
from utils.views import redirect_to_admin
from saq.views import *

urlpatterns = [
    path('mes/', FormSaq ,name="saq"),
]
