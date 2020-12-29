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
        if self.image.path:
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        
        if self.Image1:
            img1 = Image.open(self.Image1.path)
            if img1.height > 480 or img1.width > 480:
                output_size = (480,480)
                img1.thumbnail(output_size)
                img1.save(self.Image1.path)

        if self.Image2:
            img2 = Image.open(self.Image2.path)
            if img2.height > 480 or img2.width > 480:
                output_size = (480,480)
                img2.thumbnail(output_size)
                img2.save(self.Image2.path)

        if self.Image3:
            img3 = Image.open(self.Image3.path)
            if img3.height > 480 or img3.width > 480:
                output_size = (480,480)
                img3.thumbnail(output_size)
                img3.save(self.Image3.path)

        if self.Image4:
            img4 = Image.open(self.Image4.path)
            if img4.height > 480 or img4.width > 480:
                output_size = (480,480)
                img4.thumbnail(output_size)
                img4.save(self.Image4.path)
        
        if self.Image5:
            img5 = Image.open(self.Image5.path)
            if img5.height > 480 or img5.width > 480:
                output_size = (480,480)
                img5.thumbnail(output_size)
                img5.save(self.Image5.path)
        
        if self.Image6:
            img6 = Image.open(self.Image6.path)
            if img6.height > 480 or img6.width > 480:
                output_size = (480,480)
                img6.thumbnail(output_size)
                img6.save(self.Image6.path)
        
        if self.Image7:
            img7 = Image.open(self.Image7.path)
            if img7.height > 480 or img7.width > 480:
                output_size = (480,480)
                img7.thumbnail(output_size)
                img7.save(self.Image7.path)

        if self.Image8:
            img8 = Image.open(self.Image8.path)
            if img8.height > 480 or img8.width > 480:
                output_size = (480,480)
                img8.thumbnail(output_size)
                img8.save(self.Image8.path)

        if self.Image9:
            img9 = Image.open(self.Image9.path)
            if img9.height > 480 or img9.width > 480:
                output_size = (480,480)
                img9.thumbnail(output_size)
                img9.save(self.Image9.path)

        if self.Image10:
            img10 = Image.open(self.Image10.path)
            if img10.height > 480 or img10.width > 480:
                output_size = (480,480)
                img10.thumbnail(output_size)
                img10.save(self.Image10.path)

class verification(models.Model):
    Status = (
        ('P','Pending'),
        ('V','Verified')
    )
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    status = models.CharField(max_length=50,choices = Status, default='P')

    def __str__(self):
        return f'{self.user.username,self.status}'



