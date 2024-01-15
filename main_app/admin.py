from django.contrib import admin

# Register your models here.
from .models import Bird, Feeding, NestingMaterial

admin.site.register(Bird)
admin.site.register(Feeding)
admin.site.register(NestingMaterial)