from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import link
from rest_framework.response import Response

from .models import Klass
from .serializers import KlassSerializer
from students.serializers import StudentSerializer

class KlassViewSet(viewsets.ModelViewSet):
    model = Klass
    serializer_class = KlassSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @link(renderer_classes=[renderers.StaticHTMLRenderer])
    def students(self, request, pk):
    	klass = Klass.objects.get(pk=pk)
    	students = klass.students.all()
    	student_serializer = StudentSerializer(students, many=True)
    	return Response(student_serializer.data)