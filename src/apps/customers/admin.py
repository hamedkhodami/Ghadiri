from django.contrib import admin
from .models import  Counseling


@admin.register(Counseling)
class CounselingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__phone_number',)
