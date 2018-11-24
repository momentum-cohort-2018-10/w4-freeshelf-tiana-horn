from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Book, BookAdmin)
