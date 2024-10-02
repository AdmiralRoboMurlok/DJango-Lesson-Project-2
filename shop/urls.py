from django.urls import path
from .views import index, store

urlpatterns = [
   path('index', index),
   path('sklep', store)
]

