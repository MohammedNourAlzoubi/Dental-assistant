# Generated by Django 4.1.7 on 2023-03-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dentist_Assistant', '0002_alter_patient_age_alter_patient_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Married')], default='Single', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='progress',
            field=models.CharField(blank=True, choices=[('B', 'Beginning'), ('I', 'In Progress'), ('C', 'Completed')], default='Beginning', max_length=1, null=True),
        ),
    ]
