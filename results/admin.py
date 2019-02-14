from django.contrib import admin
from .models import Student, SubjectResult, SemesterResult



# Register your models here.


admin.site.register(Student)
admin.site.register(SubjectResult)
admin.site.register(SemesterResult)
