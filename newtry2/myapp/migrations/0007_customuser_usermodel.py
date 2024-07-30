# Generated by Django 5.0.6 on 2024-07-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_customuser_usermodel_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='usermodel',
            field=models.PositiveSmallIntegerField(choices=[(1, 'manager'), (2, 'employee')], null=True),
        ),
    ]
