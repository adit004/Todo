from django.contrib import admin

from new_app import models

# Register your models here.
class Todoadmin(admin.ModelAdmin):
  list_display = ("event_name", "didcription","Date")
admin.site.register(models.Todo)