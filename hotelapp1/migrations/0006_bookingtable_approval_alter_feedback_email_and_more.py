# Generated by Django 5.0.1 on 2024-02-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp1', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtable',
            name='approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='topic',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
