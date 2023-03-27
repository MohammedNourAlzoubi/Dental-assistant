# Generated by Django 4.1.7 on 2023-03-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('progress', models.CharField(choices=[('B', 'Beginning'), ('I', 'In Progress'), ('C', 'Completed')], max_length=1)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('work', models.CharField(max_length=255)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married')], max_length=1)),
            ],
        ),
    ]