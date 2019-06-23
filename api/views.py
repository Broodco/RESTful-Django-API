from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.
@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'applications':reverse('applications-list',request=request,format=format)
    })

class CreateListAppViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def upload_apk(request,serializer):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no file attached')
