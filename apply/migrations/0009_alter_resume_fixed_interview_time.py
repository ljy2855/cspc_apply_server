# Generated by Django 4.1.5 on 2023-02-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0008_alter_resume_fixed_interview_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='fixed_interview_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]