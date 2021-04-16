from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.person_create_view, name='home'),
    path('list/', views.person_list, name='list'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]