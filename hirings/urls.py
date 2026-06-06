from django.urls import path
from . import views

app_name = 'hirings'

urlpatterns = [
    path('hire/<int:helper_id>/', views.create_hiring, name='create_hiring'),
    path('my-hirings/', views.my_hirings, name='my_hirings'),
    path('hirings/<int:hiring_id>/review/', views.submit_review, name='submit_review'),
    path('hirings/<int:hiring_id>/cancel/', views.cancel_hiring, name='cancel_hiring'),
    path('hirings/<int:hiring_id>/accept/', views.accept_hiring, name='accept_hiring'),
    path('hirings/<int:hiring_id>/complete/', views.complete_hiring, name='complete_hiring'),
]