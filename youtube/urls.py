from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    # path('include', name.vids,)
    # path('result', views.result),
    path('', views.home, name='home'),
]