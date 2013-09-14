from django.db import models
from django_extras.contrib.auth.models import SingleOwnerMixin


# Un coche tiene un solo propietario
class Pagina(SingleOwnerMixin, models.Model):
	titulo = models.CharField(max_length=200)
	slug = models.SlugField()
	contenido = models.TextField()

	def __unicode__(self):
		return self.titulo