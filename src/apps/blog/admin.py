from django.contrib import admin
from .models import Category, Author, Blog

@admin.register(Blog)
class BloigAdmin(admin.ModelAdmin):
	pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass