# Generated by Django 2.2.2 on 2019-06-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190621_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='package_name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='package_version_code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]