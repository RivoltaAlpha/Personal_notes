from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task,Todo,Subtask
from django.contrib.auth import logout as auth_logout
from django.urls import reverse

# Home page 
def home(request):
    return render(request, 'home.html')

#login function
login_view = LoginView.as_view(template_name='registration/login.html')

#register Function
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#Logout Function
def logout_user(request):
    logout(request)
    return redirect('home')

#Displays all tasks associated with the user
@login_required
def task_list(request):
    todos = Todo.objects.filter(user=request.user)
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'todos': todos, 'tasks': tasks})


#Notes operations
@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        attachment = request.FILES.get('attachment')
        
        # to debug the code
        # print("Title:", title)
        # print("Description:", description)
        # print("Attachment:", attachment)

        # The task is created, then the user is requested in the code below
        task = Task.objects.create(title=title, description=description, attachment=attachment, user=request.user)

        # tasks = Task.objects.filter(user=request.user)  # Fetch tasks for the user

        return redirect('task_list')   # Pass tasks to the template

    return render(request, 'Create.html')

@login_required
def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')

    return render(request, 'update.html', {'task': task})


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'delete.html', {'task': task})

            #############################################

# Todo list operations
@login_required
def create_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        completed = request.POST.get('completed', False) # Default to False if not present


        # The task is created, then the user is requested in the code below
        todo = Todo.objects.create(name=name, completed=completed,  user=request.user)

        #todos = Todo.objects.filter(user=request.user)  # Fetch tasks for the user
        
        # Redirect to the task_list view after creating a task
        return redirect('task_list')  
        
    return render(request, 'create_task.html')


@login_required
def create_subtask(request):
    if request.method == 'POST' and request.is_ajax():
        parent_todo_id = request.POST.get('parent_todo_id')
        name = request.POST.get('name')

        # Assuming you have a model for Subtask
        parent_todo = Todo.objects.get(id=parent_todo_id)
        subtask = Subtask.objects.create(name=name, parent_todo=parent_todo)

        return JsonResponse({'message': 'Subtask created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def update_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)

    if request.method == 'POST':
        if 'completed' in request.POST:
            todo.completed = request.POST.get('completed') == 'on'  # 'on' is sent when checkbox is checked
        todo.save()
        return redirect('task_list')

    return render(request, 'update_todo.html', {'todo': todo})


@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)

    if request.method == 'POST':
        todo.delete()

        return redirect('task_list')

    return render(request, 'delete_todo.html', {'todo': todo})