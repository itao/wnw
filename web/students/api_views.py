from rest_framework import viewsets
from rest_framework import permissions

from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)

