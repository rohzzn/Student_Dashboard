from django.urls import path
from . import views

urlpatterns=[
    path('', views.studentlist, name='student_list')
    ]