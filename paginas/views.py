from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
# ################# PÁGINAS ###################

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'


class Ranking(TemplateView):
    template_name = 'paginas/rank.html'


class Sobre(TemplateView):
    template_name = 'paginas/sobre.html'


def handler404(request, *args, **kwargs):
    return render(request, 'paginas/404.html')


def handler500(request, *args, **kwargs):
    return render(request, 'paginas/404.html')
