from django.db import models
# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="product_Images",blank=True,null=True)


class blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length= 300,blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_Image",blank=True,null=True)