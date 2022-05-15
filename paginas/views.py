from django.views.generic import TemplateView


# Create your views here.
# ################# PÁGINAS ###################

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'


class Ranking(TemplateView):
    template_name = 'paginas/rank.html'


class Sobre(TemplateView):
    template_name = 'paginas/sobre.html'

