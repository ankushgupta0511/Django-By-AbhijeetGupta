# Generated by Django 5.0.6 on 2024-07-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_reportcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='data_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'data_of_report_card_generation')},
        ),
    ]