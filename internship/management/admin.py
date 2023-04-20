from django.contrib import admin
from . import models
from .models import * 
from import_export.admin import ImportExportModelAdmin
# class studentexport(ImportExportModelAdmin,admin.ModelAdmin):
#     ...

# Register your models here.

class StudentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=("S_prn",)

admin.site.register(Login)
admin.site.register(CollegeSuper)
admin.site.register(Student,StudentAdmin)
# admin.site.register(Student,studentexport)
admin.site.register(mideterm)
admin.site.register(Endterm)
# admin.site.register(Cmideterm)
# admin.site.register(CEndterm)
admin.site.register(company)
admin.site.register(compper)
# admin.site.register(faccom)
admin.site.register(comeval)
admin.site.register(progresseval)
admin.site.register(StudentFeedbackForm)
admin.site.register(CompanySupervisorFeedbackForm)

