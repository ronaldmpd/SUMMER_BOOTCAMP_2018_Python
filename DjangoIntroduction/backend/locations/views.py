from django.shortcuts import render
from django.template import RequestContext
from datetime import datetime
from pygeocoder import Geocoder
from .models import Location

from rest_framework import viewsets
from .serializers import LocationSerializer
# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        direccion = request.POST.get("search")
        if not Location.objects.filter(nombre=direccion).exists():
            try:
                result = Geocoder.geocode(direccion)
                latitud, longitud = result.coordinates
                location = Location()
                location.nombre = direccion
                location.latitud = latitud
                location.longitud = longitud
                location.save()
                context["mensaje"] = "La busqueda se realizo exitosamente"
                context["cordenadas"] = result.coordinates
            except:
                context["mensaje"] = "La busqueda de " + direccion
                context["mensaje"] += " no fue realizada"
                context["mensaje"] += " adecuadamente intente de nuevo"
        else:
            context["mensaje"] = "Anteriormente la busqueda fue realizada"
    else:
        context["mensaje"] = "Bienvenido"
    return render(request,'index.html',context)






class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
