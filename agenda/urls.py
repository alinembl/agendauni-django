from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    #semestres
    url(r'^semestres/$', views.semestre_list, name='semestre_list'),
    url(r'^semestre/(?P<pk>\d+)/edit/$', views.semestre_edit, name='semestre_edit'),
    url(r'^semestre/(?P<pk>\d+)/$', views.semestre_detail, name='semestre_detail'),
    url(r'^semestre_novo/$', views.semestre_novo, name='semestre_novo'),
    url(r'^semestre/(?P<pk>\d+)/remove/$', views.semestre_remove, name='semestre_remove'),
    #cursos
    url(r'^cursos/$', views.curso_list, name='curso_list'),
    url(r'^curso/(?P<pk>\d+)/edit/$', views.curso_edit, name='curso_edit'),
    url(r'^curso/(?P<pk>\d+)/$', views.curso_detail, name='curso_detail'),
    url(r'^curso_novo/$', views.curso_novo, name='curso_novo'),
    url(r'^curso/(?P<pk>\d+)/remove/$', views.curso_remove, name='curso_remove'),

    #professores
    url(r'^professores/$', views.professor_list, name='professor_list'),
    url(r'^professor/(?P<pk>\d+)/edit/$', views.professor_edit, name='professor_edit'),
    url(r'^professor/(?P<pk>\d+)/$', views.professor_detail, name='professor_detail'),
    url(r'^professor_novo/$', views.professor_novo, name='professor_novo'),
    url(r'^professor/(?P<pk>\d+)/remove/$', views.professor_remove, name='professor_remove'),

    #disciplinas
    url(r'^disciplinas/$', views.disciplina_list, name='disciplina_list'),
    url(r'^disciplina/(?P<pk>\d+)/edit/$', views.disciplina_edit, name='disciplina_edit'),
    url(r'^disciplina/(?P<pk>\d+)/$', views.disciplina_detail, name='disciplina_detail'),
    url(r'^curso/(?P<pk>\d+)/disciplina_novo/$', views.disciplina_novo, name='disciplina_novo'),
    url(r'^disciplina/(?P<pk>\d+)/remove/$', views.disciplina_remove, name='disciplina_remove')


]
