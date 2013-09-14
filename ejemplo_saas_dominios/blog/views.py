from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Pagina


def paginas(request):
	paginas = Pagina.objects.owned_by(request.usuario_subdominio)
	context = {'paginas': paginas}
	return render_to_response('blog/paginas.html', context, RequestContext(request))


def ver_pagina(request, slug):
	pagina = get_object_or_404(Pagina, slug=slug, owner=request.usuario_subdominio)
	context = {'pagina': pagina}
	return render_to_response('blog/ver_pagina.html', context, RequestContext(request))