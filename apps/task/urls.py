from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('borrar/<int:task_id>', views.borrar_tarea, name='borrar_tarea'),
]