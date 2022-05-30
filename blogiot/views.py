from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import PostIot, AnswerIot


# Create your views here.
class PostIotCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    model = PostIot
    fields = ['title', 'body']
    template_name = 'blogiot/templates/form-insert.html'
    success_url = reverse_lazy('blogiot:list-iot')

    def form_valid(self, form):
        form.instance.author = self.request.user

        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Incluir Mensagem PC-IOT"
        context['titulo_pg'] = "Incluir Post na Base de Dados: Protocolos de Comunicação IoT"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


class AnswerIotCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    model = AnswerIot
    fields = ['title', 'body']
    template_name = 'blogiot/templates/form-insert.html'
    success_url = reverse_lazy('blogiot:listasw-iot')

    def form_valid(self, form):
        form.instance.author = self.request.user

        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Incluir Resposta Prot-IoT"
        context['titulo_pg'] = "Incluir Resposta na Base de Dados: Protocolos de Comunicação IoT"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


# ################# UPDATE VIEWS ###################

class PostIotUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    model = PostIot
    fields = ['title', 'body']
    template_name = 'blogiot/templates/form-insert.html'
    success_url = reverse_lazy('blogiot:list-iot')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PostIot, pk=self.kwargs['pk'], author=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Mensagem PC-IOT"
        context['titulo_pg'] = "Editar Post na Base de Dados: Protocolos de Comunicação IoT"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


# ################# DELETE VIEWS ###################

class PostIotDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    model = PostIot
    template_name = 'blogiot/templates/form-excluir.html'
    success_url = reverse_lazy('blogiot:list-iot')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PostIot, pk=self.kwargs['pk'], author=self.request.user)
        return self.object


# ################# LIST VIEWS ###################

class PostIotList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = PostIot
    template_name = 'blogiot/templates/list/list-iot.html'
    paginate_by = 15

    def get_queryset(self):

        txt_title = self.request.GET.get('title')

        if txt_title:
            title = PostIot.objects.filter(title__icontains=txt_title)
        else:
            title = PostIot.objects.all()

        return title


class AnswerIotList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = AnswerIot
    template_name = 'blogiot/templates/list/list-answer-iot.html'
    paginate_by = 15

    def get_queryset(self):

        txt_body = self.request.GET.get('body')

        if txt_body:
            body = AnswerIot.objects.filter(body__icontains=txt_body)
        else:
            body = AnswerIot.objects.all()

        return body


# ################# DETAIL VIEWS ###################

class PostIotDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('account_login')
    model = PostIot
    template_name = 'blogiot/templates/detail/detail-iot.html'
