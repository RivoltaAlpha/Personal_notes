from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import TaskForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('welcome/', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),

    # Acess Routes
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),

    # CRUD Actions Routes
    path('create/', views.create_task, name='create_task'),
    path('create-task/', views.create_list, name='create_list'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update-todo/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('delete-todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)