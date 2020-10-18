from django.contrib import admin
from .models import Client, Part, Nom
from django.contrib.auth.models import Group

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
     list_display = ("number", "description")
     search_fields = ('number', 'description')
     

admin.site.unregister(Group)


admin.site.register(Client)
# admin.site.register(Part)
admin.site.register(Nom)

