from django.db import models
from django.utils import timezone
# Create your models here.
import uuid


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=250, unique=True)
    # bus/train/plane
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vehicle'
