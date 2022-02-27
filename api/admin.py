from django.contrib import admin

from api.models import URL


@admin.register(URL)
class AuthorAdmin(admin.ModelAdmin):
    pass
