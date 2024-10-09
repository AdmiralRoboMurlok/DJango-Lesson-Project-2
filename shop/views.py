from django.shortcuts import render, HttpResponse
from .models import Employee, Store

# Create your views here.
def index(request):
    lista_employ = Employee.objects.all()

    return render(request, 'index.html', context={
        'elements': lista_employ
    })

def store(request, id):
    dane_z_id_store = Store.objects.get(id=id)

    return HttpResponse(str(dane_z_id_store.name) + ' | ' + str(dane_z_id_store.location))