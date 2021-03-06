from django.contrib import admin
from .models import *


class BranchInline (admin.StackedInline):
    model = Branch
    extra = 0


class ContactInline (admin.StackedInline):
    model = Contact
    extra = 0


class CoursesAdmin (admin.ModelAdmin):
    inlines = [BranchInline, ContactInline]


admin.site.register(Category)
admin.site.register(Course, CoursesAdmin)



