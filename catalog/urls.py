from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.item_list),
    path('<int:id>', views.item_detail),

]
