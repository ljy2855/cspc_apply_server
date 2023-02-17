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

#TODO 
@admin.action(description='면접 시간 자동 배치')
def set_interview_time(self, request, queryset):
    times = InterviewTime.objects.all()
    meta = self.model._meta


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'student_id', 'semester',
                    'phone', 'fixed_interview_time')
    actions=[get_all_resume]

    def get_ordering(self, request):
        return ['fixed_interview_time']




admin.site.register(Recruitment)
admin.site.register(InterviewTime)

# Register your models here.
