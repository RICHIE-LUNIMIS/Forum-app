# Generated by Django 4.1.2 on 2022-10-26 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFacePlant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hobbies',
        ),
        migrations.AddField(
            model_name='post',
            name='hobbie',
            field=models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='hobbie'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Richie', max_length=14, verbose_name='name'),
        ),
    ]