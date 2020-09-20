from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "POLLING APP ADMIN"
admin.site.site_title = "POLLS admin area"
admin.site.index_title = "Welcome the polling admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets =[(None, {'fields': ['question']}), 
                ('Date', {'fields': ['publish_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)

