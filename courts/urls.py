from django.urls import path
from . import views

urlpatterns = [
    path('court/', views.courts, name='court'),
    path('court/details/<int:id>', views.details, name='details'),
    # path('testing/', views.testing, name='testing'),
]