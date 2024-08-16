from django.db import models
import uuid

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey('ticket.Ticket', on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name='orders')
    qty = models.CharField(max_length=255)  # Assuming qty is stored as a string; adjust max_length if needed
    payment_date = models.DateField(null=True, blank=True)
    payment_status = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} for {self.ticket} by {self.user}"
