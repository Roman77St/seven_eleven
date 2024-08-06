from django.contrib import admin
from .models import Tsar



class TsarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}

admin.site.register(Tsar, TsarAdmin)
