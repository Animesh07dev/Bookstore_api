from django.contrib import admin
from .models import Author,Book
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','bio']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','title','author','published_date','isbn','price','description']