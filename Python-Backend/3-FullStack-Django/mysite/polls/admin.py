from django.contrib import admin
from .models import Choice, Question

# Register your models here.

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass