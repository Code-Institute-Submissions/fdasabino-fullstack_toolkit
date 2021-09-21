from django.urls import path
from store.urls import app_name
from . import views


app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
]
