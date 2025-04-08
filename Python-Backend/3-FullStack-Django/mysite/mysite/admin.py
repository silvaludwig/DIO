from django.contrib import admin
from polls.models import Choice, Question

class MyAdminSite(admin.AdminSite):
    site_header = "Curso de Python Admin"

admin_site = MyAdminSite()
admin_site.register(Choice)
admin_site.register(Question)