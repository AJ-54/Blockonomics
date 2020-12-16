from django.db import models

# Create your models here.
def product_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/actual/<filename>
    return 'actual/{0}'.format(filename)

def product_thumb_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/thumb/<filename>
    return 'thumb/{0}'.format(filename)


class Product(models.Model):
    product_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    product_image = models.FileField(upload_to=product_image_path, max_length=100)
    product_thumb = models.FileField(upload_to=product_thumb_path, max_length=100)

    def __str__(self):
        return self.title
    

class Invoice(models.Model):
    STATUS_CHOICES = ((-1,"Not Started"),(0,'Unconfirmed'), (1,"Partially Confirmed"), (2,"Confirmed"))

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=-1)
    order_id = models.CharField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)
    btcvalue = models.IntegerField(blank=True, null=True)
    received = models.IntegerField(blank=True, null=True)
    txid = models.CharField(max_length=250, blank=True, null=True)
    rbf = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.address
    