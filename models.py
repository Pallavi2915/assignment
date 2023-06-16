from django.db import models
class Transaction(models.Model):
    invoice_id = models.CharField(max_length=100)
    product_line = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()