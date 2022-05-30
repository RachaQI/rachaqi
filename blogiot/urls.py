from django.urls import path

from blogiot.views import PostIotCreate, PostIotUpdate, PostIotDelete, PostIotList, PostIotDetail, AnswerIotCreate, \
    AnswerIotList

app_name = 'blogiot'

urlpatterns = [

    path('insertiot/', PostIotCreate.as_view(), name='post-iot'),
    path('answeriot/<int:pk>/', AnswerIotCreate.as_view(), name='answer-iot'),
    path('updateiot/<int:pk>/', PostIotUpdate.as_view(), name='update-iot'),
    path('deleteiot/<int:pk>/', PostIotDelete.as_view(), name='delete-iot'),
    path('listiot/', PostIotList.as_view(), name='list-iot'),
    path('listaswiot/', AnswerIotList.as_view(), name='listasw-iot'),
    path('<slug:slug>', PostIotDetail.as_view(), name='detail-iot'),

]
