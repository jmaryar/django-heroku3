from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('thoughts', views.ThoughtsView.as_view(), name='thoughtsText'),
    path('thoughts/list/', views.ThoughtsListView.as_view(), name='thoughtsList'),
    path('thoughts/submitThought/', views.submitThought, name='submitThought'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


