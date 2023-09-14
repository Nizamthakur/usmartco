from django.contrib import admin
from home import models
# Register your models here.
class product_Admin(admin.ModelAdmin):
    list_display = [
        "title",
        "price",
    ]

class blog_Admin(admin.ModelAdmin):
    list_display = [
        "title",
    ]

admin.site.register(models.product,product_Admin)
admin.site.register(models.blog,blog_Admin)