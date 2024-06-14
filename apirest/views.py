from rest_framework import viewsets

from .serializer import SerializadorPersona

from .models import Persona

class PersonaViewSet(viewsets.ModelViewSet):
    
        queryset = Persona.objects.all()
        serializer_class = SerializadorPersona


