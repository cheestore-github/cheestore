from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('name','family', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('name','family','national_code')}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','family','phone_number','national_code','email', 'password1', 'password2'),
        }),
    )
    search_fields = ('phone_number',)
    ordering = ('family',)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
