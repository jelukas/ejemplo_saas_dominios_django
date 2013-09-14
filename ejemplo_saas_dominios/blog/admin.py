from django.contrib import admin
from .models import Pagina


class PaginaAdmin(admin.ModelAdmin):
	list_display = ['titulo', 'slug', 'owner',]
	prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(Pagina, PaginaAdmin)