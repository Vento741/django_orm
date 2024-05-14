from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерируем slug только если он еще не установлен
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)