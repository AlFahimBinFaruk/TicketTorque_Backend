from django.db import models
from django.utils import timezone
import uuid
from vehicle.models import Vehicle
from category.models import Category


# Create your models here.

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=250, null=True)
    vehicle = models.ForeignKey(Vehicle,default=None, on_delete=models.DO_NOTHING, db_column='vehicle_id')
    ticket_category = models.ForeignKey(Category,default=None, on_delete=models.DO_NOTHING, db_column='ticket_category_id')
    price = models.CharField(max_length=7)
    qty = models.CharField(max_length=7)
    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField()
    boarding_point_name = models.CharField(max_length=250)
    dropping_point_name = models.CharField(max_length=250)
    starting_point_name = models.CharField(max_length=250)
    ending_point_name = models.CharField(max_length=250)
    delay = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'ticket'
