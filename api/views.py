from rest_framework import viewsets, mixins
from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.
class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class CreateListAppViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
