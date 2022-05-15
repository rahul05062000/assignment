from django.contrib import admin
from  .import models

# Register your models here.
admin.site.register(models.item)
admin.site.register(models.bill)
admin.site.register(models.print)
