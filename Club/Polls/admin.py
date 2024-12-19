from django.contrib import admin

from Polls.models import Computer

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_vip', 'status', 'reserved_by')
    list_filter = ('is_vip', 'status')
    search_fields = ('name',)