from rest_framework import serializers

# import model from models.py
from .models import Students


# Create a model serializer
class StudentsSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Students
        fields = ('teacher','student_name','student_email','class_number', 'section','roll_number', 'maths',
                                  'english','social','evs','hindi','exam_date')
