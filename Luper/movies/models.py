from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    year = models.CharField(max_length=4)  # Assuming year is always in YYYY format
    duration = models.CharField(max_length=10)  # Example: '3h 1m'
    star_rating = models.DecimalField(max_digits=3, decimal_places=1)  # Example: 8.0
    rate_count = models.CharField(max_length=100, blank=True, null=True)  # Rate count can be optional
    product_url = models.URLField()

    def __str__(self):
        return self.title
