# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from .serializers import SensorsSerializer, MeasurementSerializers, SensorDetailSerializer


class SensorCreateView(ListCreateAPIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorsSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        sensor = Sensor(name=request.data['name'], description=request.data['description'])
        sensor.save()
        return Response({'message': f'Датчик {request.data["name"]} успешно добавлен'})


class MeasurementAdd(ListCreateAPIView):
    def post(self, request):
        measurement = Measurement(id_sensor_id=request.data['sensor'], temperature=request.data['temperature'])
        measurement.save()
        sen = Sensor.objects.filter(id=request.data['sensor'])
        meas = SensorsSerializer(sen)
        return Response({'message': f'Измерение {request.data["temperature"]} для {meas} принято'})


class SensorSingleUpdateView(RetrieveUpdateAPIView):
    def patch(self, request, pk):
        sensor = Sensor.objects.filter(id=int(pk)).update(description=request.data['description'])
        return Response({'message': f'Добавление успешно'})

    def get(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        sensor = SensorDetailSerializer(sensor)
        return Response(sensor.data)

