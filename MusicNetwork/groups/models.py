from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Grupo(models.Model):
	"""docstring for Grupo"""
	nombre_grupo = models.CharField(max_length=30)
	uploadfoto = models.FileField(upload_to='uploads/')

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
			


	
		
						
				