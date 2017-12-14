from django import forms
from .models import Semestre,Curso,Professor,Disciplina,AlunoDisc

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('mat_prof','nome_prof','email_prof')

class SemestreForm(forms.ModelForm):

    data_inicial = forms.DateField(help_text='Insira a data de início do semestre no formato dd/mm/aaaa',
                                    widget=forms.DateInput(format = '%d/%m/%Y'),input_formats=('%d/%m/%Y',),required=True)
    data_final = forms.DateField(help_text='Insira a data final do semestre dd/mm/aaaa',
                                widget=forms.DateInput(format = '%d/%m/%Y'),input_formats=('%d/%m/%Y',),required=True)
    cursos = forms.ModelMultipleChoiceField(queryset= Curso.objects.all())


    class Meta:
        model = Semestre
        fields = ('ano','sem','data_inicial','data_final','cursos')



class CursoForm(forms.ModelForm):
    duracao = forms.DecimalField(min_value=1,max_value=10,help_text="Informe a duração do curso",widget=forms.NumberInput())

    class Meta:
        model = Curso
        fields = ('cod_curso','nome_curso','duracao','turno','coordenador')

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ('cod_disciplina','nome_disciplina','periodo','carga_horaria','bibliografia', 'professor')

class MatriculaForm(forms.Form):
    class Meta:
        model = AlunoDisc
        fields = ('curso')
