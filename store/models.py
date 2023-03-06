from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.name


class Website(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    website = models.ForeignKey(Website, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.URLField()
    price = models.CharField(max_length=100)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    website = models.CharField(max_length=100, default='Website name', blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    price = models.CharField(max_length=100, default='$', blank=True)
    created = models.DateField(auto_now_add=True)


    class Meta:
        indexes = [
        models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



