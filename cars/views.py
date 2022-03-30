from rest_framework.decorators import api_view  #Decorator assigns certain permissions to each function, define which HTTP request types each function is capable of handling
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def cars_list(request):

    return Response('ok!')
