""" 
@leolopes7
https://www.facebook.com/groups/pythonmania/
"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('caixas.views',
    url(r'^adicionar/$', 'caixasAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'caixasEditar'),
    url(r'^salvar/$', 'caixasSalvar'),
    url(r'^pesquisar/$', 'caixasPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'caixasExcluir'),
    url(r'^$', 'caixasListar'),
)