from django.db import models

from filer.fields.image import FilerImageField


class Profile(models.Model):

    name = models.CharField(max_length=64)
    image = models.ImageField(null=True, blank=True)
    filer_image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
