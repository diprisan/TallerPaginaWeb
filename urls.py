from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('indice/', views.indice, name='indice'),
	# ex: /polls/5/results/
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
	path('indexRender/', views.indexRender, name='indexRender'),
	path('<int:question_id>/detalle/', views.detailsExcep, name='detailsExcep'),
    path('home/', views.home, name='home'),
    path('detailsLogin/<user_id>/<pass_id>/', views.detailsLogin,  name='detailsLogin'),
	path('detailsExcep/<int:question_id>', views.detailsExcep,  name='detailsExcep'),
    path('login2/', views.login2, name='login2'),
    path('reporte/<user_id>/', views.reporte, name='reporte'),
    path('no_sesion/', views.no_sesion, name='no_sesion'),
    path('no_login/', views.no_login, name='no_login'),
    path('Rootindex/', views.Rootindex, name='Rootindex'),
    path('verGaleria/<int:idGaleria>/', views.verGaleria,  name='verGaleria'),
    path('verVenta/<int:idHotel>/<int:idanio>/', views.verVenta, name='verVenta'),
    path('vernac/<int:idHotel>/<int:idanio>/', views.vernac, name='vernac'),
]