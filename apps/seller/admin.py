from django.contrib import admin
from .models import (SellerUser,EccoInformation, Dress, Equipment, Machines, CategoryGender, CategoryWear,
                     CategoryTypes, FinalCategory, Nature, Color, Tag, Ticket, 
                     TickComment)

admin.site.register(SellerUser)
admin.site.register(EccoInformation)
admin.site.register(CategoryGender)
admin.site.register(CategoryWear)
admin.site.register(CategoryTypes)
admin.site.register(FinalCategory)
admin.site.register(Nature)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(Ticket)
admin.site.register(TickComment)
admin.site.register(Dress)
admin.site.register(Equipment)
admin.site.register(Machines)

