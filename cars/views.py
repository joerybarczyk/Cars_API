from rest_framework.decorators import api_view  #Decorator assigns certain permissions to each function, define which HTTP request types each function is capable of handling
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == 'GET':
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    