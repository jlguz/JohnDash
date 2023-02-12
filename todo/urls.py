from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('list', views.crateTask, name='list'),
        path('update_task/<str:pk>/', views.updateTask, name='update_task'),
        path('delete/<str:pk>/', views.deleteTask, name='delete'),
]




