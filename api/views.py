from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.
class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer