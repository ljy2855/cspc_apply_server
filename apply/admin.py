from django.contrib import admin
from apply.models import *
import csv
from django.http import HttpResponse
from django.db.models import Count


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
def set_interview_time(self, request, queryset): #self = resume model , queryset = 체크했던 object들
    times = [queryset.time for queryset in InterviewTime.objects.all()]
    meta = self.model._meta

    q = Resume.objects.annotate(c=Count('interview_time_choice')).order_by('c')
    for i in q:
        for j in i.interview_time_choice.all():
            if j.time in times :
                times.remove(j.time)
                i.fixed_interview_time = j
                i.save()
                j.is_fixed = True
                j.save()
                break


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'name', 'semester',
                    'phone', 'fixed_interview_time')
    actions=[get_all_resume,set_interview_time]


    def get_ordering(self, request):
        return ['fixed_interview_time']




admin.site.register(Recruitment)
admin.site.register(InterviewTime)

# Register your models here.
