from .models import * 
from .serializers import * 
from rest_framework import routers, serializers, viewsets

 # ViewSets define the view behavior.
class ICategoryViewSet(viewsets.ModelViewSet):
    queryset = ICategory.objects.all()
    serializer_class = ICategorySerializer
    
       
class IProgramViewSet(viewsets.ModelViewSet):
    queryset = IProgram.objects.all()
    serializer_class = IProgramSerializer
    
