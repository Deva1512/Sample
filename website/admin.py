from django.contrib import admin
from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','contact','subject','message')


admin.site.register(Contact,ContactAdmin)
