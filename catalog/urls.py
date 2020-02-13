

from django.urls import path
from  . import views

urlpatterns = [
    path(r'^$', views.product_list, name='product_list')
]