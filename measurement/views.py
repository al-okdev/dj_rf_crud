# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


# Создание и просмотр датчиков
class SensorView(CreateAPIView, ListAPIView):
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()


# Обновление датчика
class UpdateSensorView(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_update(self, serializer):
        serializer.save()


# Добавить измерение
class AddMeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializer

    def perform_update(self, serializer):
        serializer.save()