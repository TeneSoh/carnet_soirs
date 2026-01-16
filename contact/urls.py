from django.urls import path

from .views import index , store, delete #, create
urlpatterns = [
    path('', index, name="contact"),
    # path('create/', create, name="create_contact"),
    path('store/', store, name="store_contact")
    path('delete/', delete, name="delete_contact")
]