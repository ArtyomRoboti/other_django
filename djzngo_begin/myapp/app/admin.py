from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Student)
# admin.site.register(Course)
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'publication_date',)
#     # fields = [('title','author'), ('publication_date', 'genre')]
#     search_fields = ('title',)
#     list_filter = ('author',)
#     fieldsets = (
#         ('info', {
#             'fields':
#                 ('title', 'author', 'publication_date')
#         }),
#     )

admin.site.register(Post)
