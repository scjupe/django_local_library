from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    # removes empty rows if fewer than default 6 instances
    extra = 0

# admin.site.register(Book)
# Below does the same thing as above
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # note that here we use display_genre, defined in genre model, because specifying a value with
    # a ManyToMany relationship with Book is not allowed
    list_display = ('title', 'author', 'display_genre')
    # next line gives book instance details
    inlines = [BooksInstanceInline]
    # using display_genre not genre because could be a multiple and hence needs a function defined in the model

class BookInline(admin.TabularInline):
    model = Book

# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

# Define the admin class for AuthorAdmin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #next line determines the fields to display, their order and grouping
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    #next line lists the books for displayed author
    inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)
admin.site.register(Language)
