from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Experience
from .serializers import ExperienceSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    model = Experience
    serializer_class = ExperienceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.experiences.all()
