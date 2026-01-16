from django.urls import path

from .views import index , store , create
urlpatterns = [
    path('', index, name="contact"),
    path('create/', create, name="create_contact"),
    path('store/', store, name="store_contact")
]
