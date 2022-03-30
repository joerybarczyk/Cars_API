from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list),
    path('<int:pk>', views.car_detail)  #<int:pk> in route indicates that the value passed into the path will be used as the pk argument in car_detail(request, pk) and must be an integer
]