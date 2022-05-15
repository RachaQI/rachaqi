from django.urls import path

from blogga.views import PostGaCreate, PostGaUpdate, PostGaDelete, PostGaList, PostGaDetail

app_name = 'blogga'

urlpatterns = [

    path('insertga/', PostGaCreate.as_view(), name='post-ga'),
    path('updatega/<int:pk>/', PostGaUpdate.as_view(), name='update-ga'),
    path('deletega/<int:pk>/', PostGaDelete.as_view(), name='delete-ga'),
    path('listga/', PostGaList.as_view(), name='list-ga'),
    path('<slug:slug>', PostGaDetail.as_view(), name='detail-ga'),

]
