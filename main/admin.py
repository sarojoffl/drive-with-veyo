from django.contrib import admin
from main.models import Job, Blog, ContactMessage, TeamMember, CustomUser as User

admin.site.register(Job)
admin.site.register(Blog)
admin.site.register(ContactMessage)
admin.site.register(TeamMember)
admin.site.register(User)