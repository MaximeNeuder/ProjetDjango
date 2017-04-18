from django.contrib import admin
from inv.models import Item
from inv.models import Inventaire
from inv.models import Member
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'place_occupe',
        'inventaire'
    )

class InventaireAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'place_max',
        'proprietaire'
    )

class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'avatar'
    )

admin.site.register(Item, ItemAdmin)
admin.site.register(Inventaire, InventaireAdmin)
admin.site.register(Member, MemberAdmin)