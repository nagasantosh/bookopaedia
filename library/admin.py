from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Book, BookRequest

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'category', 'age_group', 'is_available')
    search_fields = ('title', 'author', 'category', 'age_group')
    list_filter = ('category', 'age_group', 'is_available')
    actions = ['mark_available', 'mark_unavailable']

    @admin.action(description='Mark selected books available')
    def mark_available(self, request, queryset):
        queryset.update(is_available=True)

    @admin.action(description='Mark selected books unavailable')
    def mark_unavailable(self, request, queryset):
        queryset.update(is_available=False)

@admin.register(BookRequest)
class BookRequestAdmin(ImportExportModelAdmin):
    list_display = ('book', 'email', 'mobile', 'timestamp')
    search_fields = ('book__title', 'email', 'mobile')
    list_filter = ('timestamp',)

