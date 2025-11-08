from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LogEntry(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.name} - {self.timestamp}"
