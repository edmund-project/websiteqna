# Generated by Django 2.2.12 on 2020-12-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteqna', '0012_remove_question_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='posted_by',
            field=models.TextField(max_length=50, null=True),
        ),
    ]