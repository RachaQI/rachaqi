from django.urls import path

from .views import PostGaCreate, PostGaUpdate, PostGaDelete, PostGaList
from .views import PaginaInicial, Ranking

app_name = 'paginas'

urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('rank/', Ranking.as_view(), name='rank'),
    path('insert/', PostGaCreate.as_view(), name='post-ga'),
    path('update/<int:pk>/', PostGaUpdate.as_view(), name='update-ga'),
    path('delete/<int:pk>/', PostGaDelete.as_view(), name='delete-ga'),
    path('listar/ga/', PostGaList.as_view(), name='list-ga'),

]
