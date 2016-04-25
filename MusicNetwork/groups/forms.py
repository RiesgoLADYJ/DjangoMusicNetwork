from django import forms
from .models import Grupo

class GrupoForm(forms.ModelForm):
	class Meta:
		model = Grupo
		fields = ('nombre_grupo','fecha_inicio') #, 'uploadfoto' ):