from django.contrib import admin
from .models import Material
# Register your models here.

class MaterialsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Material, MaterialsAdmin)