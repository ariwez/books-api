from django.contrib import admin

from books.api.models import Book


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
        'updated_at',
    )