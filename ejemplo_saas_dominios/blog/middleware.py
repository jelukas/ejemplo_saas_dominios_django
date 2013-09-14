from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class SubdomainMiddleware:
    """ Make the subdomain publicly available to classes """

    def process_request(self, request):
        domain_parts = request.get_host().split('.')
        if (len(domain_parts) > 1):
            subdomain = domain_parts[0]
            if (subdomain.lower() == 'www'):
                subdomain = ''
            domain = '.'.join(domain_parts[1:])
        else:
            subdomain = ''
            domain = request.META['HTTP_HOST']

        request.subdomain = subdomain
        request.domain = domain

        if subdomain != 'www' and subdomain != '':
            # Buscamos el usuario del subdominio
            try:
                request.usuario_subdominio = User.objects.get(username=subdomain)
            except ObjectDoesNotExist:
                raise Http404