from django.contrib import admin
from django.urls import path
from webapp.views import views

urlpatterns = [
    path('correcao/',views.correcao,name=("correcao")),
]
