from django.urls import path
from .views import log_table, log_table_partial
from .views import log_table, log_table_partial, create_log_entry


    
urlpatterns = [
    path('', log_table),  # ← ahora responde en http://127.0.0.1:8000/
     path('tabla/actualizar/', log_table_partial),
     path('nuevo/', create_log_entry),

]

