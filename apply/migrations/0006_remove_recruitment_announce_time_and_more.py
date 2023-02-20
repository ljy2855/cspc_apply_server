# Generated by Django 4.1.5 on 2023-02-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0005_remove_recruitment_is_document_announe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruitment',
            name='announce_time',
        ),
        migrations.AddField(
            model_name='recruitment',
            name='announce_final_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='recruitment',
            name='announce_middle_time',
            field=models.DateTimeField(null=True),
        ),
    ]
