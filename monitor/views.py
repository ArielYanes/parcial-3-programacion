from django.shortcuts import render, redirect
from .forms import LogEntryForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Count
from .models import LogEntry, Device

# Vista principal con gráfico
def log_table(request):
    logs = LogEntry.objects.select_related('sender', 'receiver').order_by('-timestamp')
    devices = Device.objects.all()

    # Agrupar logs por sensor emisor
    sender_counts = (
        LogEntry.objects.values('sender__name')
        .annotate(total=Count('id'))
        .order_by('sender__name')
    )

    labels = [entry['sender__name'] for entry in sender_counts]
    data = [entry['total'] for entry in sender_counts]

    return render(request, 'monitor/log_table.html', {
        'logs': logs,
        'devices': devices,
        'labels': labels,
        'data': data,
    })

# Vista parcial para HTMX (solo la tabla)
def log_table_partial(request):
    logs = LogEntry.objects.select_related('sender', 'receiver').order_by('-timestamp')
    html = render_to_string('monitor/log_table_partial.html', {'logs': logs})
    return HttpResponse(html)

# Vista para crear un nuevo mensaje entre sensores
def create_log_entry(request):
    form = LogEntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('log_table')
    return render(request, 'monitor/create_log_entry.html', {'form': form})
