from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    lista_employ = Employee.objects.all()

    return render(request, 'index.html', context={
        'elements': lista_employ
    })