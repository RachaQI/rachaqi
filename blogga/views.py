from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import PostGa


# Create your views here.
# ################# CREATE VIEWS ###################

class PostGaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    model = PostGa
    fields = ['title', 'body']
    template_name = 'blogga/templates/form-insert.html'
    success_url = reverse_lazy('blogga:list-ga')

    def form_valid(self, form):

        form.instance.author = self.request.user

        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Incluir Mensagem GA-AL"
        context['titulo_pg'] = "Incluir Post na Base de Dados: Geometria Analítica e Álgebra Linear"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


# ################# UPDATE VIEWS ###################

class PostGaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    model = PostGa
    fields = ['title', 'body']
    template_name = 'blogga/templates/form-insert.html'
    success_url = reverse_lazy('blogga:list-ga')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PostGa, pk=self.kwargs['pk'], author=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Mensagem GA-AL"
        context['titulo_pg'] = "Editar Post na Base de Dados: Geometria Analítica e Álgebra Linear"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


# ################# DELETE VIEWS ###################

class PostGaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    model = PostGa
    template_name = 'blogga/templates/form-excluir.html'
    success_url = reverse_lazy('blogga:list-ga')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PostGa, pk=self.kwargs['pk'], author=self.request.user)
        return self.object


# ################# LIST VIEWS ###################

class PostGaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = PostGa
    template_name = 'blogga/templates/list/list-ga.html'
    paginate_by = 15

    def get_queryset(self):

        txt_title = self.request.GET.get('title')

        if txt_title:
            title = PostGa.objects.filter(title__icontains=txt_title)
        else:
            title = PostGa.objects.all()

        return title


# ################# Detail VIEWS ###################

class PostGaDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('account_login')
    model = PostGa
    template_name = 'blogga/templates/detail/detail-ga.html'
