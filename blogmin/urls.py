from django.urls import path

from blogmin.views import PostMinCreate, PostMinUpdate, PostMinDelete, PostMinList, PostMinDetail, AnswerMinCreate, \
    AnswerMinList

app_name = 'blogmin'

urlpatterns = [

    path('insertmin/', PostMinCreate.as_view(), name='post-min'),
    path('answermin/<int:pk>/', AnswerMinCreate.as_view(), name='answer-min'),
    path('updatemin/<int:pk>/', PostMinUpdate.as_view(), name='update-min'),
    path('deletemin/<int:pk>/', PostMinDelete.as_view(), name='delete-min'),
    path('listmin/', PostMinList.as_view(), name='list-min'),
    path('listaswmin/', AnswerMinList.as_view(), name='listasw-min'),
    path('<slug:slug>', PostMinDetail.as_view(), name='detail-min'),

]
