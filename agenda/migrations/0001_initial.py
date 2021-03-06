# Generated by Django 2.0 on 2017-12-09 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_curso', models.CharField(max_length=3, verbose_name='código do curso')),
                ('nome_curso', models.CharField(max_length=100, verbose_name='nome do curso')),
                ('duracao', models.CharField(max_length=2, verbose_name='duração')),
                ('turno', models.CharField(max_length=50, verbose_name='Turno')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_prof', models.CharField(max_length=10, verbose_name='matricula do professor')),
                ('nome_prof', models.CharField(max_length=100, verbose_name='nome do professor')),
                ('email_prof', models.EmailField(max_length=254, verbose_name='email do professor')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=5, verbose_name='Ano')),
                ('sem', models.CharField(max_length=2, verbose_name='Semestre')),
                ('data_inicial', models.DateField(null=True)),
                ('data_final', models.DateField(null=True)),
                ('cursos', models.ManyToManyField(to='agenda.Curso')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='coordenador',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Professor'),
        ),
        migrations.AlterUniqueTogether(
            name='semestre',
            unique_together={('ano', 'sem')},
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together={('cod_curso', 'nome_curso')},
        ),
    ]
