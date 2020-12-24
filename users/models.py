from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profilepics')
    Contact = models.DecimalField(decimal_places = 0 ,max_digits=10,default=0)
    Address = models.TextField(default="")
    governmentID = models.ImageField(default = 'default.jpg', upload_to = 'governmentids')
    Image1 = models.ImageField(upload_to = 'people_faces',null=True)
    Image2 = models.ImageField(upload_to = 'people_faces',null=True)
    Image3 = models.ImageField(upload_to = 'people_faces',null=True)
    Image4 = models.ImageField(upload_to = 'people_faces',null=True)
    Image5 = models.ImageField(upload_to = 'people_faces',null=True)
    Image6 = models.ImageField(upload_to = 'people_faces',null=True)
    Image7 = models.ImageField(upload_to = 'people_faces',null=True)
    Image8 = models.ImageField(upload_to = 'people_faces',null=True)
    Image9 = models.ImageField(upload_to = 'people_faces',null=True)
    Image10 = models.ImageField(upload_to = 'people_faces',null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class verification(models.Model):
    Status = (
        ('P','Pending'),
        ('V','Verified')
    )
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    status = models.CharField(max_length=50,choices = Status, default='P')

    def __str__(self):
        return f'{self.user.username,self.status}'



