from django.db import models
from django.utils.text import slugify

 
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    question_detail = models.TextField(max_length=50000)
    question_title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.TextField(max_length=20)
    slug = models.SlugField(max_length=40)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.question_title)
        super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_detail = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.TextField(max_length=20)