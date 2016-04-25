from django import forms
from .models import Grupo
from .models import Publicacion
from django.contrib.auth.models import User

class GrupoForm(forms.ModelForm):
	class Meta:
		model = Grupo
		fields = ('nombre_grupo','fecha_inicio') #, 'uploadfoto' ):


class RegistroForm(forms.ModelForm):
	"""docstring for RegistroForm"""
	class Meta:
		model = User
		fields = ('email','password')

class PublicacionForm(forms.ModelForm):
	"""docstring for PublicacionForm"""
	class Meta:
		model = Publicacion
		fields = ('titulo','texto','fecha_creacion','fecha_publicacion','grupo_publicacion')
		