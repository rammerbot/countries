from django.contrib import admin
from .models import Countries,  Languages, Floor, Museum

# Register your models here.

admin.site.register(Countries)
admin.site.register(Languages)
admin.site.register(Floor)
admin.site.register(Museum)