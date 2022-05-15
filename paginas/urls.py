from django.urls import path

from .views import PaginaInicial, Ranking, Sobre

app_name = 'paginas'

urlpatterns = [

    path('', PaginaInicial.as_view(), name='inicio'),
    path('rank/', Ranking.as_view(), name='rank'),
    path('sobre/', Sobre.as_view(), name='sobre'),

]
