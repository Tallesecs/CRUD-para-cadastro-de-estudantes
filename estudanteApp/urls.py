from django.urls import path
from .views import estudanteList, estudanteCreate, estudanteUpdate, estudanteDelete


urlpatterns = [
    path('list/', estudanteList, name='estudanteList'),
    path('create/', estudanteCreate, name='estudanteCreate'),
    path('update/<int:id>/', estudanteUpdate, name='estudanteUpdate'),
    path('delete/<int:id>/', estudanteDelete, name='estudanteDelete'),



]