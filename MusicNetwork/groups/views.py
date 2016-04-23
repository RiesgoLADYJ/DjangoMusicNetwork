from django.shortcuts import render
from django.utils import timezone
from .models import Grupo, Publicacion
# Create your views here.

def post_list_and_groups(request):
	publicacion = Publicacion.objects.order_by('fecha_publicacion')
	return render(request, 'home.html', {'publicacion': publicacion})
