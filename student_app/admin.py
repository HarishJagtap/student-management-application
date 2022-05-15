from django.contrib import admin

from student_app.models import Book, School, Student


admin.site.register(Book)
admin.site.register(School)
admin.site.register(Student)
