from django.urls import path
from . import views

app_name = 'helpers'

urlpatterns = [
    path('', views.home, name='home'),
    path('helpers/', views.helper_list, name='helper_list'),
    path('helpers/<int:pk>/', views.helper_detail, name='helper_detail'),
    path('get-districts/', views.get_districts, name='get_districts'),
    path('get-upazilas/', views.get_upazilas, name='get_upazilas'),
    path('ajax/districts/', views.ajax_districts, name='ajax_districts'),
    path('ajax/upazilas/', views.ajax_upazilas, name='ajax_upazilas'),
    path('api/nearby-helpers/', views.get_nearby_helpers, name='nearby_helpers'),
]
