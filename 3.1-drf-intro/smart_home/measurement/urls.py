from django.urls import path

from .views import SensorView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
