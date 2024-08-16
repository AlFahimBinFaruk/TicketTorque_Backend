from django.db import models
import uuid

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=models.CASCADE)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    price = models.CharField(max_length=255)
    qty = models.CharField(max_length=255)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    boarding_point_name = models.CharField(max_length=255)
    dropping_point_name = models.CharField(max_length=255)
    from_location = models.ForeignKey('location.Location', related_name='departure_tickets', on_delete=models.CASCADE)
    to_location = models.ForeignKey('location.Location', related_name='arrival_tickets', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
