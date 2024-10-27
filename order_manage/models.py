from django.db import models

class Inventory(models.Model):
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

class Order(models.Model):
    customer = models.CharField(max_length=255)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)
