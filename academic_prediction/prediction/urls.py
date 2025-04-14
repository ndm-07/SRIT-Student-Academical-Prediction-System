from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('attendance/', views.attendance_prediction, name='attendance'),
    path('marks/', views.marks_prediction, name='marks'),
    path('cgpa/', views.cgpa_prediction, name='cgpa'),
    path('sgpa/', views.sgpa_prediction, name='sgpa'),
]
