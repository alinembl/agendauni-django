from django.db import models

# Create your models here.

class Professor(models.Model):
    mat_prof = models.CharField(verbose_name='matricula do professor',max_length=10)
    nome_prof = models.CharField(verbose_name='nome do professor',max_length=100)
    email_prof = models.EmailField(verbose_name='email do professor')

    def __str__(self):
        return self.mat_prof + "-" + self.nome_prof


class Curso(models.Model):
    cod_curso = models.CharField(verbose_name='código do curso',max_length=3)
    nome_curso = models.CharField(verbose_name='nome do curso',max_length=100)
    duracao = models.CharField(verbose_name='duração',max_length=2)
    turno = models.CharField(verbose_name='Turno',max_length=50)
    coordenador = models.OneToOneField('Professor',on_delete=models.CASCADE,default=None,blank=True,null=True)

    class Meta:
        unique_together = (('cod_curso','nome_curso'))


    def __str__(self):
        return self.cod_curso + "-" + self.nome_curso

class Disciplina(models.Model):
    cod_disciplina = models.CharField(verbose_name='código da disciplina',max_length=5)
    nome_disciplina = models.CharField(verbose_name='nome da disciplina',max_length=100)
    periodo = models.CharField(verbose_name='período',max_length=2)
    carga_horaria = models.CharField(verbose_name='carga horária',max_length=4)
    bibliografia = models.TextField(verbose_name='bibliografia',max_length=500)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE,default=None,blank=True,null=True)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE,default=None,blank=True,null=True)

    class Meta:
        unique_together = (('cod_disciplina','nome_disciplina'))

    def __str__(self):
        return self.cod_disciplina + "-" + self.nome_disciplina


class Semestre(models.Model):
    ano = models.CharField(verbose_name="Ano",max_length=5)
    sem = models.CharField(verbose_name="Semestre",max_length=2)
    data_inicial = models.DateField(null=True)
    data_final = models.DateField(null=True)
    cursos = models.ManyToManyField(Curso,blank=True,null=True)

    class Meta:
        unique_together = (('ano','sem'))

    def __str__(self):
        return self.ano + "." + self.sem
