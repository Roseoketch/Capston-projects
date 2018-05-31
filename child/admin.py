from django.contrib import admin
from .models import categories, organization, vacancies

# Register your models here.
admin.site.register(categories)
admin.site.register(organization)
admin.site.register(vacancies)
