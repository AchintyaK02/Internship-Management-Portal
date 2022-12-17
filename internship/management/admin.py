from django.contrib import admin
from .models import *


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    search_fields=("S_prn",)

admin.site.register(Login)
admin.site.register(CollegeSuper)
admin.site.register(Student,StudentAdmin)
admin.site.register(mideterm)
admin.site.register(Endterm)
# admin.site.register(Cmideterm)
# admin.site.register(CEndterm)
admin.site.register(company)
admin.site.register(compper)
admin.site.register(faccom)
admin.site.register(comeval)

