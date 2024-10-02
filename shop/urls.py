from django.urls import path
from .views import index, store

urlpatterns = [
   path('pracownicy/', index),
   path('sklep/<int:id>', store),
]

