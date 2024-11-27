from django.contrib import admin

from .models import Author, Book, Collection

# Register your models here.

admin.site.site_header = "Лаб2, Мошкович Демид, 3 курс, 11 группа, 2024"
admin.site.index_title = "Выберите таблицу для просмотра"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography', 'birth_date', 'rating')
    search_fields = ('name', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publication_date', 'pages', 'price', 'author')
    search_fields = ('title', 'author__name')


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_books')
    search_fields = ('title',)
    ordering = ('title',)
    filter_horizontal = ('books',)

    def display_books(self, obj):
        return ', '.join([book.title for book in obj.books.all()])

    display_books.short_description = 'Books'

