# Generated by Django 4.0.4 on 2022-06-01 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0002_freepost_freecomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freecomment',
            old_name='body',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='freecomment',
            name='title',
        ),
        migrations.AlterField(
            model_name='freecomment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snsapp.freepost'),
        ),
    ]
