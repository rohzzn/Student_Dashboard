from django.shortcuts import render
from .models import Student
# Create your views here.

def studentlist(request):
    get_students = Student.objects.all()

    data = {
        'get_students': get_students,
    }
    return render(request, 'studentlist.html', data)
