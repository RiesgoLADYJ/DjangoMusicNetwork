from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Grupo, Publicacion
# Create your views here.

def post_list_and_groups(request):
	publicacion = Publicacion.objects.order_by('fecha_publicacion')
	grupos = Grupo.objects.order_by('nombre_grupo')
	return render(request, 'home.html', {'publicacion': publicacion, 'grupos':grupos})

def groups(request,pk):
	grupo = get_object_or_404(Grupo.objects.order_by('nombre_grupo'), pk=pk)
	return render(request, 'fanpage.html', {'grupo': grupo})