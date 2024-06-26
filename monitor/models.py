from django.db import models

class Site(models.Model):
    website_name = models.CharField(max_length=100)
    website_url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class Check(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    checked_at = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveIntegerField()
    response_time = models.FloatField()  # in seconds

    def __str__(self):
        return f"{self.site.name} - {self.checked_at}"