from django.urls import path
from .views import *

app_name="empleado_app"

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('empleado/',EmpleadoListView.as_view(),name='lista_empleado'),
    path('empleado_search/',EmpleadoByCityListView.as_view(),name="lista_filter_empleado"),
    path('add/',EmpleadoCreateView.as_view(),name='agregar_empleado'),
    path('delete/<pk>',EmpleadoDeleteView.as_view(),name='delete_job'),
    path('detail/<pk>',EmpleadoDetailView.as_view(),name='detail_empleado'),
    path('update/<pk>',EmpleadoUpdateView.as_view(),name='update_empleado')
]