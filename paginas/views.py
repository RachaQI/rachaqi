from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import PostGa, PostIot, PostMin


# Create your views here.
# ################# PÁGINAS ###################

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'


class Ranking(TemplateView):
    template_name = 'paginas/rank.html'


# ################# CREATE VIEWS ###################

class PostGaCreate(CreateView):
    model = PostGa
    fields = ['author', 'title', 'slug', 'body']
    template_name = 'paginas/form-insert.html'
    success_url = reverse_lazy('paginas:inicio')


# ################# UPDATE VIEWS ###################

class PostGaUpdate(UpdateView):
    model = PostGa
    fields = ['author', 'title', 'slug', 'body']
    template_name = 'paginas/form-insert.html'
    success_url = reverse_lazy('paginas:inicio')


# ################# DELETE VIEWS ###################

class PostGaDelete(DeleteView):
    model = PostGa
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('paginas:inicio')


# ################# LIST VIEWS ###################

class PostGaList(ListView):
    model = PostGa
    template_name = 'paginas/listas/ga.html'
