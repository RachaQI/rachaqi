from django.urls import path

from blogiot.views import PostIotCreate, PostIotUpdate, PostIotDelete, PostIotList, PostIotDetail

app_name = 'blogiot'

urlpatterns = [

    path('insertiot/', PostIotCreate.as_view(), name='post-iot'),
    path('updateiot/<int:pk>/', PostIotUpdate.as_view(), name='update-iot'),
    path('deleteiot/<int:pk>/', PostIotDelete.as_view(), name='delete-iot'),
    path('listiot/', PostIotList.as_view(), name='list-iot'),
    path('<slug:slug>', PostIotDetail.as_view(), name='detail-iot'),

]
