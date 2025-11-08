from django.urls import path
from .views import log_table, log_table_partial, create_log_entry

urlpatterns = [
    path('', log_table, name='log_table'),  # Tabla principal
    path('tabla/actualizar/', log_table_partial, name='log_table_partial'),  # HTMX
    path('nuevo/', create_log_entry, name='create_log_entry'),  # Formulario de envío
]
