from django.urls import path

from measurement.views import SensorCreateView, MeasurementAdd, SensorSingleUpdateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateView.as_view()),
    path('measurements/', MeasurementAdd.as_view()),
    path('sensors/<pk>/', SensorSingleUpdateView.as_view())
]
