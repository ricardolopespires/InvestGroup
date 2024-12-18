from django.db import models
from datetime import datetime, timedelta




class Subscriber(models.Model):    
    email = models.EmailField()   
    time = models.TimeField(default="00:00:00")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    subscribed = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.email} "
    
    class Meta:
        ordering = ['-created']
        verbose_name = "Assinante"
        verbose_name_plural = "Assinantes"

    def save(self, *args, **kwargs):
        if self.email and self.created and self.updated:
            time_difference = self.updated - self.created
            # Convert the time difference to hours, minutes, seconds
            hours, remainder = divmod(time_difference.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            # Format the time as HH:MM:SS
            self.time = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        
        super().save(*args, **kwargs)
