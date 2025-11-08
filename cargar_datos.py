import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_project.settings')
django.setup()

from monitor.models import Device, LogEntry

# Crear dispositivo
device = Device.objects.create(name="Sensor 1", status="Activo")

# Crear log
LogEntry.objects.create(device=device, message="Inicio de sesión correcto", timestamp=datetime.now())

print("Datos cargados correctamente.")
