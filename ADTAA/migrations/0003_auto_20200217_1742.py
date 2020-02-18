# Generated by Django 3.0.3 on 2020-02-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADTAA', '0002_auto_20200216_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discipline1',
            field=models.CharField(blank=True, choices=[('PC', 'Programming - C++'), ('PP', 'Programming - Python'), ('GD', 'Game Development'), ('DA', 'Data Structures and Algorithms'), ('CO', 'Computer Organization'), ('OS', 'Operating Systems'), ('PL', 'Programming Languages'), ('CS', 'Cybersecurity'), ('MA', 'Mobile Applications'), ('AI', 'Artificial Intelligence'), ('NT', 'Networks'), ('TC', 'Theory of Computation'), ('PD', 'Parallel and Distributed Systems'), ('', '--------')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='discipline2',
            field=models.CharField(blank=True, choices=[('PC', 'Programming - C++'), ('PP', 'Programming - Python'), ('GD', 'Game Development'), ('DA', 'Data Structures and Algorithms'), ('CO', 'Computer Organization'), ('OS', 'Operating Systems'), ('PL', 'Programming Languages'), ('CS', 'Cybersecurity'), ('MA', 'Mobile Applications'), ('AI', 'Artificial Intelligence'), ('NT', 'Networks'), ('TC', 'Theory of Computation'), ('PD', 'Parallel and Distributed Systems'), ('', '--------')], default='', max_length=2),
        ),
    ]
