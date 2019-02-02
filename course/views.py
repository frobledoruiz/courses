from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Course

# Hacer un listado de cursos
class CourseList(ListView):
    model = Course

# Mostrar el detalle de un curso
class CourseDetail(DetailView):
    model = Course

# Crear un curso
class CourseCreation(CreateView):
    model = Course
    success_url = reverse_lazy('course:list')
    fields = ['name', 'start_date', 'end_date', 'picture']

# Para editar un curso
class CourseUpdate(UpdateView):
    model = Course
    success_url = reverse_lazy('course:list')
    fields = ['name', 'start_date', 'end_date', 'picture']

# Para borrar
class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('course:list')