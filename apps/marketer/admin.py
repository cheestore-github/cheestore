from django.contrib import admin

from apps.marketer.models import ProfileMrketer



admin.site.register(ProfileMrketer)
class MarketerAdmin(admin.ModelAdmin):
    list_display = ('name ', 'family', 'phone_number','is_active')
    list_filter = ('is_active', 'name','family', 'phone_number')
    search_fields = ('name', 'family', 'phone_number')
    prepopulated_fields = {"slug": ("id_number",)}
    date_hierarchy = 'created_at'
    raw_id_fields = 'id_number'

