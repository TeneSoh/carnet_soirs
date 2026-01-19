from django.urls import path

from .views import index , store , delete, show, edit #, create
urlpatterns = [
    path('', index, name="contact"),
    # path('create/', create, name="create_contact"),
    path('store/', store, name="store_contact"),
    path('delete-contact/<int:id>/', delete, name="delete_contact"),
    path('show-contact/<int:id>/', show, name="show_contact"),
    path('edit-contact/<int:id>/', edit, name="edit_contact")
]
