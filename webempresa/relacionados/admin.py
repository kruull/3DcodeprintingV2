from django.contrib import admin
from .models import Partners
# Register your models here.

class PartnersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Partners, PartnersAdmin)