from django.contrib import admin
from .models import Product, Category, Website, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['title', 'slug', 'image', 'created']
 list_filter = ['created']


admin.site.register(Product)
admin.site.register(Website)
admin.site.register(Category)

