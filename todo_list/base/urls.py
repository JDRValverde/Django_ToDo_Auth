from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, TaskReorder
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='tasks_detail'),
    path('tasks_create', TaskCreate.as_view(), name='tasks_create'),
    path('tasks_update/<int:pk>/', TaskUpdate.as_view(), name='tasks_update'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='tasks_delete'),
    path('task_reorder/', TaskReorder.as_view(), name='tasks_reorder'),

]
