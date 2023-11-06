from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Base
# Create your views here.

class Cargar(View):
    def get(self,request, nombre):
        producto_nuevo = Base(nombre=nombre)
        producto_nuevo.save()
        return HttpResponse(True)
class Eliminar(View):
    def get(self,request, nombre):
        productos = Base.objects.all()
        for producto in productos:
            if producto.nombre == nombre:
                eliminar = Base.objects.get(id=producto.id)
                eliminar.delete()
        return HttpResponse(True)

class Visualizar(View):
    def get(self,request):
        productos = Base.objects.all()
        return render(request, r"visualizar.html", {"productos":productos})