from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Grupo, Publicacion
from .forms import GrupoForm
from .forms import RegistroForm
from .forms import PublicacionForm
from .forms import LoginForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.

def post_list_and_groups(request):
	publicacion = Publicacion.objects.order_by('fecha_publicacion')
	grupos = Grupo.objects.order_by('nombre_grupo')
	return render(request, 'home.html', {'publicacion': publicacion, 'grupos':grupos})

def groups(request,pk):
	grupo = get_object_or_404(Grupo.objects.order_by('nombre_grupo'), pk=pk)
	return render(request, 'fanpage.html', {'grupo': grupo})

def nuevo_grupo(request):
	if request.method == "POST":
		form = GrupoForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('grupos', pk=post.pk)
	else:
		form = GrupoForm()
		return render(request, 'nuevo_grupo.html', {'form': form})

def registro(request):
	if request.method == "POST":
		form = RegistroForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('post_list_and_groups')
	else:
		form = RegistroForm()
		return render(request, 'registro.html', {'form': form})

def crearPost(request):
	if request.method == "POST":
		form = PublicacionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return HttpResponseRedirect("/")
	else:
		form = PublicacionForm()
		return render(request, 'posts.html', {'form': form})

def login(request):
	form = LoginForm(request.POST)
	try:
		username = (request.POST['username'])
		contrasenia = (request.POST['password'])
	except KeyError:
		username = ""
		contrasenia = ""
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect("/")
		else:
			form = LoginForm()
	return render(request, 'login.html', {'form' : form})