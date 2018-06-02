from django.contrib import admin
from .models import Contact, Organization, Program


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name', 'email', 'phone', 'address']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'site')
    search_fields = ['name', 'site']


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'description', 'site', 'date', 'time')
    search_fields = ('name', 'description', 'site', 'donations_link', 'topic',
                     'age_group', 'location')
