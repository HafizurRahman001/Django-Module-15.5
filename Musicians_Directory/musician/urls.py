from django.urls import path
from . import views

urlpatterns = [
    path('musician/', views.add_musician, name='add_musician'),
    path('musician/<int:id>/', views.edit_musician, name='edit_musician'),
]