from django.contrib import admin
from .models import Departement, DepartementMember

# Register your models here.
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active')
    list_filter = ('created_at', 'updated_at', 'is_active')
    search_fields = ('name',)

admin.site.register(Departement, DepartementAdmin)