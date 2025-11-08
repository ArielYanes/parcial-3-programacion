from django.shortcuts import render
from django.shortcuts import redirect
from .forms import LogEntryForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Count
from .models import LogEntry, Device

# Vista principal con gráfico
def log_table(request):
    logs = LogEntry.objects.select_related('device').order_by('-timestamp')
    devices = Device.objects.all()

    # Agrupar logs por dispositivo
    device_counts = (
        LogEntry.objects.values('device__name')
        .annotate(total=Count('id'))
        .order_by('device__name')
    )

    labels = [entry['device__name'] for entry in device_counts]
    data = [entry['total'] for entry in device_counts]

    return render(request, 'monitor/log_table.html', {
        'logs': logs,
        'devices': devices,
        'labels': labels,
        'data': data,
    })

# Vista parcial para HTMX (solo la tabla)
def log_table_partial(request):
    logs = LogEntry.objects.select_related('device').order_by('-timestamp')
    html = render_to_string('monitor/log_table_partial.html', {'logs': logs})
    return HttpResponse(html)

def create_log_entry(request):
    if request.method == 'POST':
        form = LogEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirige a la tabla principal
    else:
        form = LogEntryForm()
    return render(request, 'monitor/create_log_entry.html', {'form': form})
