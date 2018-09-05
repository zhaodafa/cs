from django.contrib import admin

# Register your models here.

from api.models import *


admin.site.register(Course)
admin.site.register(CourseDetail)
admin.site.register(Teacher)
admin.site.register(PricePolicy)
