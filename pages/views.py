from django.shortcuts import render
from api.models import SensorData

# Create your views here.

def sales(request):
    return render(request, 'pages/sales/sales.html')

def info(request):
    return render(request, 'pages/info/info.html')

def settings(request):
    return render(request, 'pages/settings/settings.html')

import json
from django.core.serializers.json import DjangoJSONEncoder

def graphs(request):
    sensor_data = SensorData.objects.all().order_by('-created_at')[:30]
    # Grafik için verileri kronolojik sıraya sokalım (eskiden yeniye)
    chart_data = list(sensor_data)[::-1]
    
    # JavaScript için verileri JSON formatına çevirelim (Daha güvenli ve hatasız)
    chart_data_json = json.dumps([{
        'time': d.created_at.strftime('%H:%M'),
        'n': float(d.nitrogen or 0),
        'p': float(d.phosphorus or 0),
        'k': float(d.potassium or 0),
        'm': float(d.soil_moisture or 0),
        't': float(d.soil_temperature or 0),
    } for d in chart_data], cls=DjangoJSONEncoder)

    return render(request, 'pages/graphs/graphs.html', {
        'sensor_data': sensor_data,
        'chart_data_json': chart_data_json
    })
