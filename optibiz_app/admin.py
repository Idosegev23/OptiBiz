from django.contrib import admin
from .models import User, Organization, Project, Task, Report

admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Report)
