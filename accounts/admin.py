from django.contrib import admin
from .models import Book, UserProfile, AddCourse, CreateCourse, Book

admin.site.register(Book)
class UserProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AddCourse)
admin.site.register(CreateCourse)