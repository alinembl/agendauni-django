# Generated by Django 2.0 on 2017-12-13 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_alunodisc'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunodisc',
            name='curso',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Curso'),
        ),
    ]
