from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoCreateForm, TodoUpdateForm


def home(request):
    all_todo = Todo.objects.all()
    context = {
        'all_todo': all_todo,
    }
    return render(request, 'home.html', context=context)


def detail(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).last()
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context=context)


def delete(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).first()
    if todo is not None:
        todo.delete()
    messages.success(request, 'Todo Delete Successfully', 'success')
    return redirect('home')


def create(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            Todo.objects.create(
                **form.cleaned_data
            )
            messages.success(request, 'Todo Create Successfully', 'success')
            return redirect('home')

    else:
        form = TodoCreateForm()

    return render(request, 'create.html', context={'form': form})


def update(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).first()
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo Update Successfully', 'success')
            return redirect('detail', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)

    return render(request, 'update.html', context={'form': form})
