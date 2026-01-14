from django.urls import path
from .views import index, show

urlpatterns = [
    path('hello', index, name='index'),
    path('show/<int:id>', show, name='show' )
]
