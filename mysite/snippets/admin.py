from django.contrib import admin

from .models import Snippet


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

#
# class SnippetAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

# admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Snippet)
