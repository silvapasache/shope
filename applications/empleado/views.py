from django.shortcuts import render
from django.views.generic import *
from .models import *
from .form import EmpleadoForm
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.


class EmpleadoByCityListView(ListView):
    template_name = "empleado/list.html"
    context_object_name='Empleados'
    paginate_by=4
    ordering=('id',)

    def get_queryset(self):
        name=self.request.GET.get('kword','')
        print("===",name)
        queryset = Empleado.objects.filter(
            first_name__icontains=name
        ) 
        return queryset


class EmpleadoListView(ListView):
    template_name = "empleado/list.html"
    context_object_name='Empleados'
    ordering=("id",)
    paginate_by=4

    def get_queryset(self):
        palabra=self.request.GET.get('kword','')
        queryset = Empleado.objects.filter(
            Q(first_name__icontains=palabra) | Q(last_name__icontains=palabra)
        )
        return queryset

    

class HomeView(TemplateView):
    template_name = "inicio.html"


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url=reverse_lazy('empleado_app:lista_empleado')


class EmpleadoCreateView(CreateView):
    template_name = "empleado/add.html"
    model = Empleado
    form_class=EmpleadoForm
    success_url =reverse_lazy('empleado_app:lista_empleado')

class EmpleadoDetailView(DetailView):
    template_name = "empleado/detail.html"
    model = Empleado
    context_object_name='Empleado'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        empleado=self.model.objects.get(id=pk)
        name_area=Empleado.AREA_CHOICES.__getitem__(int(empleado.area))
        context["area_nombre"]=name_area[1]
        return context
    


class EmpleadoUpdateView(UpdateView):
    template_name = "empleado/update.html"
    model = Empleado
    form_class=EmpleadoForm
    success_url=reverse_lazy('empleado_app:lista_empleado')
