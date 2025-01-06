from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
# Create your views here.

# Lista de tareas
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})


# Marcar tarea completada
def marcar_completada(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completado = not task.completado
    task.save()
    return redirect('task_list')


# Borrar tarea
def agregar_tarea(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        
    return render(request, 'task/agregar_tarea.html', {'form': form})

# Editar tarea
def editar_tarea(request, task_id):
    tarea = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=tarea)
        
    return render(request, 'task/editar_tarea.html', {'form': form, 'tarea': tarea})

# Borrar tarea
def borrar_tarea(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

