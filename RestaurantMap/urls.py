from django.urls import path
from . import views

app_name = 'RestaurantMap'

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
]