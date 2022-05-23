from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import PostMin


# Create your views here.
class PostMinCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    model = PostMin
    fields = ['title', 'body']
    template_name = 'blogmin/templates/form-insert.html'
    success_url = reverse_lazy('blogmin:list-min')

    def form_valid(self, form):

        form.instance.author = self.request.user

        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Incluir Mensagem MIN-DADOS"
        context['titulo_pg'] = "Incluir Post na Base de Dados: Mineração de Dados"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


# ################# UPDATE VIEWS ###################

class PostMinUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    model = PostMin
    fields = ['title', 'body']
    template_name = 'blogmin/templates/form-insert.html'
    success_url = reverse_lazy('blogmin:list-min')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PostMin, pk=self.kwargs['pk'], author=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Mensagem MIN-DADOS"
        context['titulo_pg'] = "Editar Post na Base de Dados: Mineração de Dados"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


# ################# DELETE VIEWS ###################

class PostMinDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    model = PostMin
    template_name = 'blogmin/templates/form-excluir.html'
    success_url = reverse_lazy('blogmin:list-min')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PostMin, pk=self.kwargs['pk'], author=self.request.user)
        return self.object


# ################# LIST VIEWS ###################

class PostMinList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = PostMin
    template_name = 'blogmin/templates/list/list-min.html'
    paginate_by = 15

    def get_queryset(self):

        txt_title = self.request.GET.get('title')

        if txt_title:
            title = PostMin.objects.filter(title__icontains=txt_title)
        else:
            title = PostMin.objects.all()

        return title


# ################# DETAIL VIEWS ###################

class PostMinDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('account_login')
    model = PostMin
    template_name = 'blogmin/templates/detail/detail-min.html'
