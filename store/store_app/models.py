from django.db import models

class Product(models.Model):
    product_title = models.CharField(max_length=200, blank=True, default='')
    product_price = models.IntegerField()
    product_discount = models.IntegerField(default=0, blank=True)
    product_total_cost = models.IntegerField(blank=True)
    product_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_description = models.TextField(max_length=500)
    product_specifications = models.TextField(max_length=500)
    product_delivery = models.TextField(max_length=200)
    product_seller = models.ForeignKey('Seller', on_delete=models.PROTECT, null=True)
    owner = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)
    product_category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['pk']

    def save(self, *args, **kwargs):
        product_price = self.product_price
        product_discount = self.product_discount
        self.product_total_cost = int(round(product_price * (1 - product_discount / 100)))
        super(Product, self).save(*args, **kwargs)


class Category(models.Model):
    category_title = models.CharField(max_length=50)

    class Meta:
        ordering = ['pk']


class Seller(models.Model):
    seller_title = models.CharField(max_length=150)

    class Meta:
        ordering = ['pk']
