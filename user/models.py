from django.db import models
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver

class Applicant(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class LabMaster(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# 랩짱 변경 시 기존 랩장 비활성화
@receiver(post_save, sender=LabMaster)
def create_master(sender, instance=None, created=False, **kwargs):
    if created:
        pre_masters = LabMaster.objects.exclude(id=instance.id)
        for master in pre_masters:
            master.is_active = False
            master.save()
