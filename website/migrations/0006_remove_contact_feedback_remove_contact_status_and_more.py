# Generated by Django 4.2.7 on 2023-12-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='status',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact',
        ),
    ]
