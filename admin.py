from django.contrib import admin
from .models import Services_Data

class AdminService_Data(admin.ModelAdmin):
    list_display =['course_id',
                   'course_name',
                   'course_duration',
                   'course_start_date',
                   'course_start_time',
                   'course_trainer_name',
                   'course_trainer_exp']
admin.site.register(Services_Data, AdminService_Data)
