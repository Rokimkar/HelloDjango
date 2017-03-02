from django.contrib import admin
from .models import Publisher, Author, BooK

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'email')
	search_fields  = ('first_name','last_name', 'email')

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(BooK)
