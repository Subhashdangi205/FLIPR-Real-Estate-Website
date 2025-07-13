from django.contrib import admin
from .models import Project, Client, Contact, Subscriber

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile', 'city', 'created_at')
    search_fields = ('full_name', 'email', 'mobile', 'city')
    list_filter = ('created_at',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'created_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)
