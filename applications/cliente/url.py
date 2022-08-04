from django.urls import path
from .views import ClienteListView,ClienteCreateView

app_name="cliente_app"

urlpatterns = [
    path('cliente/',ClienteListView.as_view(),name='list_cliente'),
    path('cliente-add/',ClienteCreateView.as_view(),name='add_cliente'),
]