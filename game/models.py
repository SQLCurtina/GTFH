from django.conf import settings
from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
# Create your models here.

class Page (models.Model):
    page_title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.page_title



class Decision (models.Model):
    decision_title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    page = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    finance = models.IntegerField()
    health = models.IntegerField()
    sanity = models.IntegerField()
    respect = models.IntegerField()


