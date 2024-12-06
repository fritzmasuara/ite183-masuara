from django.urls import path
from .views import (
    contact_list, contact_create, contact_edit, contact_delete,
    ContactListAPI, ContactDetailAPI
)

urlpatterns = [
    # Web Views
    path('', contact_list, name='contact_list'),
    path('new/', contact_create, name='contact_create'),
    path('<int:pk>/edit/', contact_edit, name='contact_edit'),
    path('<int:pk>/delete/', contact_delete, name='contact_delete'),

    # API Views
    path('api/contacts/', ContactListAPI.as_view(), name='contact_list_api'),
    path('api/contacts/<int:pk>/', ContactDetailAPI.as_view(), name='contact_detail_api'),
]
