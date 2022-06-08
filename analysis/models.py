from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    customer_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    invoice_date = models.DateTimeField(null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    stock_code = models.CharField(max_length=100,null=True, blank=True)
    Invoice_no = models.BigIntegerField(null=True, blank=True)
    country = models.CharField(max_length=400, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)



