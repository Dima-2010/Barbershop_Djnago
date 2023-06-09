from django.contrib import admin

from .models import servis, logo, barber, comment, work

admin.site.register(servis)
admin.site.register(logo)
admin.site.register(comment)


class PropertyImageInline(admin.TabularInline):
    model = work
    extra = 6


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, ]


admin.site.register(barber, PropertyAdmin)
