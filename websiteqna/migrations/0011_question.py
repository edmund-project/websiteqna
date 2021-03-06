# Generated by Django 2.2.12 on 2020-12-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('websiteqna', '0010_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('question_title', models.CharField(max_length=100)),
                ('question_detail', models.TextField(max_length=10000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.TextField(max_length=20)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
    ]
