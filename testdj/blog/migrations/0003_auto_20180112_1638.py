# Generated by Django 2.0 on 2018-01-12 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Employee'),
        ),
    ]
