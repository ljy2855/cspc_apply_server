from django.contrib import admin
from apply.models import *
import csv
from django.http import HttpResponse


@admin.action(description='csv 파일 다운로드')
def get_all_resume(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
        meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'student_id', 'semester', 'phone')
    actions=[get_all_resume]




admin.site.register(Recruitment)
admin.site.register(InterviewTime)

# Register your models here.
