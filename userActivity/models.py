from django.db import models
from django.utils import timezone
from django.conf import settings

class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_active = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.last_active}"


# how to determine which users are currently logged in in jdango
# how to determine which user made the last changes in django app