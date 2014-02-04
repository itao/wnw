from rest_framework import serializers as s

from .models import Note
from students.serializers import StudentSerializer

class NoteSerializer(s.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id','klass', 'students', 'detail')

