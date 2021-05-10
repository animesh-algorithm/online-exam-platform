from django.contrib import admin
from . import models

# Register your models here.
class OptionInline(admin.TabularInline):
    model = models.Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(models.Exam)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Option)
admin.site.register(models.Subject)