# Generated by Django 4.2.9 on 2024-01-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_bird_nesting_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nestingmaterial',
            name='color',
            field=models.CharField(max_length=51),
        ),
    ]