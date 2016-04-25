from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

class Grupo(models.Model):
	"""docstring for Grupo"""
	nombre_grupo = models.CharField(max_length=30)
	#uploadfoto = models.ImageField(upload_to='profile_images',blank=True, null=True) ): esta muy dificil eso de subir fotos
	fecha_inicio = models.DateField()
	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('grupos', args=[str(self.id)])

class Artista(models.Model):
	"""docstring for Artista"""
	grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
	nombre_artista = models.CharField(max_length=30)
	apellidoP = models.CharField(max_length=30)
	apellidoM = models.CharField(max_length=30, blank=True)	

class Album(models.Model):
		"""docstring for Album"""
		artista  = models.ForeignKey(Artista, on_delete=models.CASCADE)
		nombre_album = models.CharField(max_length=30)
		fecha_lanzamiento = models.DateField()


class Genero(models.Model):
		"""docstring for Genero"""
		nombre_genero = models.CharField(max_length=30)
			
class Publicacion(models.Model):
	"""docstring for Publicacion"""
	autor = models.ForeignKey('accounts.User', null = True, blank=True)
	texto = models.TextField(default='Nada que ver aqui. (empty)')
	titulo = models.CharField(max_length=30, default = 'Sin titulo')
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)
	grupo_publicacion = models.ForeignKey(Grupo, on_delete=models.CASCADE, default=01)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

