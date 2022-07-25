from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    #image = models.ImageField(upload_to='images/', blank=True)
    # slug = models.SlugField(max_length=255, unique=True)
    vendor = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.pk})
    def get_update_url(self):
        return reverse('products:product_update', kwargs={'pk': self.pk})
    def get_delete_url(self):
        return reverse('products:product_delete', kwargs={'pk': self.pk})
    def get_add_url(self):
        return reverse('products:product_add')
    def get_list_url(self):
        return reverse('products:product_list')
    def get_add_to_cart_url(self):
        return reverse('products:add_to_cart', kwargs={'pk': self.pk})
    def get_remove_from_cart_url(self):
        return reverse('products:remove_from_cart', kwargs={'pk': self.pk})
    def get_cart_url(self):
        return reverse('products:cart')
    def get_checkout_url(self):
        return reverse('products:checkout')
    def get_checkout_success_url(self):
        return reverse('products:checkout_success')
    def get_checkout_failure_url(self):
        return reverse('products:checkout_failure')
    def get_checkout_cancel_url(self):
        return reverse('products:checkout_cancel')
    def get_checkout_return_url(self):
        return reverse('products:checkout_return')