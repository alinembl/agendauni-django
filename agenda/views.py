from django.shortcuts import render,get_object_or_404,redirect
from .models import Semestre,Curso,Professor,Disciplina,AlunoDisc
from .forms import SemestreForm,CursoForm,ProfessorForm,DisciplinaForm,MatriculaForm
from django.contrib.auth.decorators import login_required

from datetime import timedelta,date
def inicio(request):
    return render(request, 'agenda/inicio.html', {})

#Semestres
@login_required
def semestre_list(request):
    semestres = Semestre.objects.all()
    return render(request, 'agenda/semestre_list.html',{'semestres':semestres})

@login_required
def semestre_detail(request,pk):
    semestre = get_object_or_404(Semestre, pk=pk)
    return render(request, 'agenda/semestre_detail.html', {'semestre': semestre})

@login_required
def semestre_edit(request,pk):
    semestre = get_object_or_404(Semestre,pk=pk)
    if request.method == "POST":
        form = SemestreForm(request.POST, instance=semestre)
        if form.is_valid():
            semestre = form.save(commit=False)
            semestre.save()
            form.save_m2m()
            return redirect('semestre_detail',pk=semestre.pk)
    else:
        form = SemestreForm(instance=semestre)
    return render(request,'agenda/semestre_edit.html',{'form':form})

@login_required
def semestre_novo(request):
   form = SemestreForm(request.POST)
   if request.method == "POST":
       if form.is_valid():
           semestre = form.save(commit=False)
           semestre.save()
           form.save_m2m()
           return redirect('semestre_detail',pk=semestre.pk)
   else:
       form = SemestreForm()

   return render(request,'agenda/semestre_edit.html',{'form':form})

@login_required
def semestre_remove(request,pk):
    semestre = get_object_or_404(Semestre,pk=pk)
    semestre.delete()
    return redirect('semestre_list')


#Cursos
@login_required
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'agenda/curso_list.html',{'cursos':cursos})

@login_required
def curso_detail(request,pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'agenda/curso_detail.html', {'curso': curso})

@login_required
def curso_edit(request,pk):
    curso = get_object_or_404(Curso,pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            form.save()
            return redirect('curso_detail',pk=curso.pk)
    else:
        form = CursoForm(instance=curso)
    return render(request,'agenda/curso_edit.html',{'form':form})

@login_required
def curso_novo(request):
   form = CursoForm(request.POST)
   if request.method == "POST":
       if form.is_valid():
           curso = form.save(commit=False)
           curso.save()
           return redirect('curso_detail',pk=curso.pk)
   else:
       form = CursoForm()

   return render(request,'agenda/curso_edit.html',{'form':form})

@login_required
def curso_remove(request,pk):
    curso = get_object_or_404(Curso,pk=pk)
    curso.delete()
    return redirect('curso_list')

#Professores
@login_required
def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'agenda/professor_list.html',{'professores':professores})

@login_required
def professor_detail(request,pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, 'agenda/professor_detail.html', {'professor': professor})

@login_required
def professor_edit(request,pk):
    professor = get_object_or_404(Professor,pk=pk)
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.save()
            form.save_m2m()
            form.save()
            return redirect('professor_detail',pk=professor.pk)
    else:
        form = ProfessorForm(instance=professor)
    return render(request,'agenda/professor_edit.html',{'form':form})

@login_required
def professor_novo(request):
   form = ProfessorForm(request.POST)
   if request.method == "POST":
       if form.is_valid():
           professor = form.save(commit=False)
           professor.save()
           form.save_m2m()
           return redirect('professor_detail',pk=professor.pk)
   else:
       form = ProfessorForm()

   return render(request,'agenda/professor_edit.html',{'form':form})

@login_required
def professor_remove(request,pk):
    professor = get_object_or_404(Professor,pk=pk)
    professor.delete()
    return redirect('professor_list')

#Disciplinas
@login_required
def disciplina_list(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'agenda/disciplina_list.html',{'disciplinas':disciplinas})


@login_required
def disciplina_detail(request,pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    return render(request, 'agenda/disciplina_detail.html', {'disciplina': disciplina})

@login_required
def disciplina_edit(request,pk):
    disciplina = get_object_or_404(Disciplina,pk=pk)
    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.save()
            form.save_m2m()
            form.save()
            return redirect('disciplina_detail',pk=disciplina.pk)
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request,'agenda/disciplina_edit.html',{'form':form})

@login_required
def disciplina_novo(request,pk):
   curso_disc = get_object_or_404(Curso,pk=pk)
   form = DisciplinaForm(request.POST)
   if request.method == "POST":
       if form.is_valid():
           disciplina = form.save(commit=False)
           disciplina.curso = curso_disc
           print (disciplina.curso)
           disciplina.save()
           form.save_m2m()
           return redirect('disciplina_detail',pk=disciplina.pk)
   else:
       form = DisciplinaForm()

   return render(request,'agenda/disciplina_edit.html',{'form':form})

@login_required
def disciplina_remove(request,pk):
    disciplina = get_object_or_404(Disciplina,pk=pk)
    disciplina.delete()
    return redirect('disciplina_list')

def plano_de_aula(request,pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    return render(request, 'agenda/plano_de_aula.html', {'disciplina': disciplina})

def escolherDisciplina(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'agenda/escolher_disciplina.html', {'disciplinas':disciplinas})

def matricular_aluno_curso(request):
    form = MatriculaForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            matricula = form.save(commit=False)
            matricula.save()
            form.save_m2m()
            return redirect('aluno_curso',pk=matricula.pk)
    else:
        form = ProfessorForm()

    return render(request,'agenda/professor_edit.html',{'form':form})
