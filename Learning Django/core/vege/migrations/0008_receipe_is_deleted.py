# Generated by Django 5.0.6 on 2024-07-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0007_alter_reportcard_data_of_report_card_generation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
