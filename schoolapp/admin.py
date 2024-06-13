from django.contrib import admin
from schoolapp.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')