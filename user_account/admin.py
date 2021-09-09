from django.contrib import admin
from .models import TemplateClass, Report

# admin.site.register(TemplateClass)
@admin.register(TemplateClass)
class TemplateClass(admin.ModelAdmin):
    list_display = ('template_name', 'template_file')

# admin.site.register(Report)

admin.site.site_header = 'Integrated Web Based Latex System'
