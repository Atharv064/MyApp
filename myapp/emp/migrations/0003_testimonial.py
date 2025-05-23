# Generated by Django 5.2 on 2025-05-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_rename_empi_id_emp_emp_id_alter_emp_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonials/')),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]
