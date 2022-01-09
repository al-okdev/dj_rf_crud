from django.urls import path

from measurement.views import SensorView, UpdateSensorView, AddMeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', UpdateSensorView.as_view()),

    path('measurements/', AddMeasurementView.as_view())
]
