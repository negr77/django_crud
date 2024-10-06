from django.db import models
from django.conf import settings
from django.utils import timezone

class Mypost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.create_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title