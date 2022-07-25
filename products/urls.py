from django.urls import path
from .views import product_list,UserView

urlpatterns = [
    path('',product_list,name='product_list'),
    path('signup/',UserView,name ='signup'),
]