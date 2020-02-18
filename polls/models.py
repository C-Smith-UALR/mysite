from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Course(models.Model):
    DISCIPLINE_CHOICES=(
        ('PC', 'Programming - C+'),
        ('AI', 'Artificial Intelligence'),
        ('CS', 'Cybersecurity'),
        ('PP', 'Programming - Python'),
        ('PL', 'Programming Languages'),
        ('OS', 'Operating Systems'),
        ('', '--------'),
    )

    courseTitle=models.CharField(max_length=50)
    courseNo=models.CharField(max_length=15)
    discipline1 = models.CharField(
        max_length=2,
        choices=DISCIPLINE_CHOICES,
        default='',

    )
    discipline2 = models.CharField(
        max_length=2,
        choices=DISCIPLINE_CHOICES,
        default='',

    )
    def __str__(self):
        return self.courseTitle