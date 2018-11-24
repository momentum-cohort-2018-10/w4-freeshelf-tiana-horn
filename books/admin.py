from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = (
        'title', 
        'author',
        'description',

    )
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Book, BookAdmin)
