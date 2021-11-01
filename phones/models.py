from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = AutoSlugField(populate_from='name')
