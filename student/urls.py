from django.urls import path
from .views import StudentView,StudentAddAPIView,StudentListAPIView,GetStudent,index


urlpatterns = [
    path('articles/', StudentView.as_view()),
    path('create/', StudentAddAPIView.as_view(), name='create'),
    path('allstudents/', StudentListAPIView.as_view(), name='detail'),
    path('home/',GetStudent.as_view(),name='studentslist'),
    path('sendmail/', index, name='sendmail')
    # url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
]