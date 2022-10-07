from django.urls import path

from . import views
app_name='linkdl'
urlpatterns = [
    path('', views.IndexView.index, name='index'),
    path('<int:link_id>/', views.detail, name='detail'),
    path('submit/', views.submit, name='submit'),
    
]