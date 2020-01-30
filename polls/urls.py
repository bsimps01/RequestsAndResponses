from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('specifics<int: question_id>/', views.detail, name='detail'),
    path('<int: question_id>/results/', views.results, name='results'),
    path('<int: question_id>/vote/', views.vote, name='vote'),
]

