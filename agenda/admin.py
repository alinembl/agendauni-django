from django.contrib import admin

from .models import Semestre,Curso,Professor,Disciplina

admin.site.register(Semestre)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Disciplina)
