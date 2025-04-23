from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.add_application, name='add_application'),
    path('edit/<int:pk>/', views.edit_application, name='edit_application'),
    path('delete/<int:pk>/', views.delete_application, name='delete_application'), 
    path('search/', views.search_application, name='search_application'),
]