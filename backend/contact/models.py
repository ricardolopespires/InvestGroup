from django.db import models
from datetime import datetime, timedelta

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(default="")
    answers = models.BooleanField(default=False)
    time = models.TimeField(default="00:00:00")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['-created']
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def save(self, *args, **kwargs):
        if self.answers and self.created and self.updated:
            time_difference = self.updated - self.created
            # Convert the time difference to hours, minutes, seconds
            hours, remainder = divmod(time_difference.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            # Format the time as HH:MM:SS
            self.time = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        
        super().save(*args, **kwargs)
