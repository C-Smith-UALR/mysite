from django.db import models

class Course(models.Model):
    DISCIPLINE_CHOICES=(
        ('PC', 'Programming - C++'),
        ('PP', 'Programming - Python'),
        ('GD', 'Game Development'),
        ('DA', 'Data Structures and Algorithms'),
        ('CO', 'Computer Organization'),
        ('OS', 'Operating Systems'),
        ('PL', 'Programming Languages'),
        ('CS', 'Cybersecurity'),
        ('MA', 'Mobile Applications'),
        ('AI', 'Artificial Intelligence'),
        ('NT', 'Networks'),
        ('TC', 'Theory of Computation'),
        ('PD', 'Parallel and Distributed Systems'),
        ('', '--------'),
    )

    DAYS_CHOICES=(
        ('MW', 'MW'),
        ('TR', 'TR'),
    )

    TIMES_CHOICES=(
        (1, '08:00 AM - 09:15 AM'),
        (2, '09:25 AM - 10:40 AM'),
        (3, '10:50 AM - 12:05 PM'),
        (4, '12:15 PM - 01:30 PM'),
        (5, '01:40 PM - 02:55 PM'),
        (6, '03:05 PM - 04:20 PM'),
        (7, '04:30 PM - 05:45 PM'),
    )

    courseNumber=models.CharField(max_length=15)
    courseTitle = models.CharField(max_length=50)
    courseDays = models.CharField(max_length=2, choices=DAYS_CHOICES, default='')
    courseTime = models.IntegerField(choices=TIMES_CHOICES, default=0)
    discipline1 = models.CharField(
        max_length=2,
        choices=DISCIPLINE_CHOICES,
        default='',
        blank=True,

    )
    discipline2 = models.CharField(
        max_length=2,
        choices=DISCIPLINE_CHOICES,
        default='',
        blank=True,

    )
    def __str__(self):
        return self.courseTitle

    def getClassInfo(self):
        return self.courseNumber + ' ' + self.courseTitle + ' ' + self.courseDays + ' ' \
               + str(self.courseTime) + ' ' + self.discipline1 + ' ' + self.discipline2
