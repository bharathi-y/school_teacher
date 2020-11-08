from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students
from .serializer import StudentsSerializer
from django.views.generic import TemplateView
from django.http import HttpResponse
from .tasks import sleepy, send_email_task
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    )

from rest_framework.permissions import AllowAny



class GetStudent(TemplateView):
    template_name = "student/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj1 = Students.objects.filter(teacher=self.request.user)
        context["students"] = obj1
        return context

class StudentView(APIView):
    def get(self, request):
        student = Students.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = StudentsSerializer(student, many=True)
        return Response({"student": serializer.data})

    def post(self, request):
        student = request.data.get('article')

        # Create an article from the above data
        serializer = StudentsSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(student_saved.title)})

class StudentAddAPIView(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    #permission_classes = [IsAuthenticated]

    def perform_add(self, serializer):
        serializer.save(user=self.request.user)

class StudentListAPIView(ListAPIView):
    serializer_class = StudentsSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['teacher','student_name','student_email','class_number', 'section','roll_number', 'maths',
                                  'english','social','evs','hindi','total','exam_date']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Students.objects.all().filter(teacher=self.request.user)
        return queryset_list


def index(request):
    send_email_task.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')
