from django.urls import path, include
from saq.views import *

urlpatterns = [
    path('mes/', FormSaq ,name="saq"),
]
