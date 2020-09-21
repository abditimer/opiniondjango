from django.urls import path

from . import views

app_name = 'opinions'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.vote, name='vote'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/agree/', views.agree, name='agree'),
    path('<int:question_id>/disagree/', views.disagree, name='disagree'),
]