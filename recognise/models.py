from django.db import models
from PIL import Image

class Images(models.Model):
    name = models.CharField(max_length=50,default='')
    file = models.ImageField()

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.file.path)

        if img.height > 480 or img.width > 480:
            output_size = (480,480)
            img.thumbnail(output_size)
            img.save(self.file.path)