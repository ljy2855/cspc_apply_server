# Generated by Django 4.1.5 on 2023-02-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0006_remove_recruitment_announce_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='announce_final_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='announce_middle_time',
            field=models.DateTimeField(),
        ),
    ]
