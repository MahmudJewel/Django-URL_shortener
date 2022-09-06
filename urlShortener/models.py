from django.db import models
from .utils import create_shortened_url
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.

# short model 
class ShortURLS(models.Model):
    # guest = User.objects.get(id=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_day = models.IntegerField(default=1)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.long_url} ==> {self.short_url}'

    def save(self, *args, **kwargs):
        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)
        super().save(*args, **kwargs)
