# Generated by Django 4.1.6 on 2023-03-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_grade_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='title',
            field=models.CharField(default='This title', max_length=50),
            preserve_default=False,
        ),
    ]
