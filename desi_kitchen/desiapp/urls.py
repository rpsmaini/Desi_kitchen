from django.urls import path
from .views import contact_list, contact_create, contact_update, contact_delete

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('new/', contact_create, name='contact_create'),
    path('edit/<int:id>/', contact_update, name='contact_update'),
    path('delete/<int:id>/', contact_delete, name='contact_delete'),
]
