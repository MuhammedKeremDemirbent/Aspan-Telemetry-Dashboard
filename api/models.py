from django.db import models

class SensorData(models.Model):
   
    device_id = models.CharField(max_length=150, db_index=True) #ID  
    payload = models.JSONField(verbose_name="Ham TTN Verisi")
    
    # Ayıştırılmış Veriler
    nitrogen = models.FloatField(verbose_name="Azot", null=True, blank=True)
    potassium = models.FloatField(verbose_name="Potasyum", null=True, blank=True)
    phosphorus = models.FloatField(verbose_name="Fosfor", null=True, blank=True)
    soil_moisture = models.FloatField(verbose_name="Toprak Nemi", null=True, blank=True)
    soil_temperature = models.FloatField(verbose_name="Toprak Sıcaklığı", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.payload and isinstance(self.payload, dict):
            uplink_message = self.payload.get('uplink_message', {})
            decoded_payload = uplink_message.get('decoded_payload', {})
            
            if decoded_payload:
                self.nitrogen = decoded_payload.get('nitrogen')
                self.potassium = decoded_payload.get('potassium')
                self.phosphorus = decoded_payload.get('phosphorus')
                self.soil_moisture = decoded_payload.get('soil_moisture')
                self.soil_temperature = decoded_payload.get('soil_temperature_c')
        
        super().save(*args, **kwargs)
    
    def __str__(self):
         return f"{self.device_id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"