# Generated by Django 5.0.6 on 2024-07-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_rename_detail_patient_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Age',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Gender',
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]