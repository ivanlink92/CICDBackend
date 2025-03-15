from django.urls import path
from .views import RegisterView, LoginView, TaskView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task-detail'),
]