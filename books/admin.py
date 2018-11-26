from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'author', 'description', 'picture',)
    prepopulated_fields = {'slug': ('author',)}

# Register your models here.
admin.site.register(Book, BookAdmin)
# admin.site.register(Suggestion)
# admin.site.register(User)
