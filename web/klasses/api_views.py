from rest_framework import viewsets
from rest_framework import permissions

from .models import Klass
from .serializers import KlassSerializer

class KlassViewSet(viewsets.ModelViewSet):
    model = Klass
    serializer_class = KlassSerializer
    permission_classes = (permissions.IsAuthenticated,)

