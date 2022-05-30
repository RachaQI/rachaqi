from django.urls import path

from blogga.views import PostGaCreate, PostGaUpdate, PostGaDelete, PostGaList, PostGaDetail, AnswerGaCreate, \
    AnswerGaList

app_name = 'blogga'

urlpatterns = [

    path('insertga/', PostGaCreate.as_view(), name='post-ga'),
    path('answerga/<int:pk>/', AnswerGaCreate.as_view(), name='answer-ga'),
    path('updatega/<int:pk>/', PostGaUpdate.as_view(), name='update-ga'),
    path('deletega/<int:pk>/', PostGaDelete.as_view(), name='delete-ga'),
    path('listga/', PostGaList.as_view(), name='list-ga'),
    path('listaswga/', AnswerGaList.as_view(), name='listasw-ga'),
    path('<slug:slug>/', PostGaDetail.as_view(), name='detail-ga'),

]
