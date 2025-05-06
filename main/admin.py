from django.contrib import admin
from main.models import Job, Blog, ContactMessage, TeamMember, Driver

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')  # 'type' is a valid choice field
    search_fields = ('title',)
    list_filter = ('type',)
    ordering = ('title',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_submitted')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('date_submitted',)
    ordering = ('-date_submitted',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')
    ordering = ('name',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'zip_code', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('-created_at',)
    list_filter = ('created_at',)