from rest_framework import viewsets
from rest_framework import permissions

from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    model = Note
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

