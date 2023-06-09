from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.index, name='index'),
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('detail/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
]
