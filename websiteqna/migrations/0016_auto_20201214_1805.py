# Generated by Django 2.2.12 on 2020-12-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteqna', '0015_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='lol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_detail', models.TextField(max_length=50000)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]