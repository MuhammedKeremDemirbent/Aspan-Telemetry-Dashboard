import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import SensorData

@csrf_exempt
@require_POST
def ttn_webhook(request):
    try:
        data = json.loads(request.body)
        
        # TTN payload'undan device_id'yi güvenlice çıkarıyoruz
        device_id = data.get('end_device_ids', {}).get('device_id', 'Bilinmeyen Cihaz')
        
        SensorData.objects.create(device_id=device_id, payload=data)

        return JsonResponse({"status": "Veri başarıyla kaydedildi"}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Geçersiz JSON formatı"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
