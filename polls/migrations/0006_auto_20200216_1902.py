# Generated by Django 3.0.3 on 2020-02-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200216_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discipline1',
            field=models.CharField(choices=[('PC', 'Programming - C+'), ('AI', 'Artificial Intelligence'), ('CS', 'Cybersecurity'), ('PP', 'Programming - Python'), ('PL', 'Programming Languages'), ('OS', 'Operating Systems'), ('', '--------')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='discipline2',
            field=models.CharField(choices=[('PC', 'Programming - C+'), ('AI', 'Artificial Intelligence'), ('CS', 'Cybersecurity'), ('PP', 'Programming - Python'), ('PL', 'Programming Languages'), ('OS', 'Operating Systems'), ('', '--------')], default='', max_length=2),
        ),
    ]
