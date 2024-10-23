from django.contrib import admin
from .models import Blog, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('tags',)
    search_fields = ('title',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'created_at'), 
        }),
    )

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
