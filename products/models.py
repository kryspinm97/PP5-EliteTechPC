from django.db import models

# Create your models here.


class Category(models.Model):

    """ Model to represent categories of products """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class PrebuiltPC(models.Model):

    """ Model to represent prebuilt PCs """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    graphics_card = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
