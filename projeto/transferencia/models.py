from datetime import datetime
from django.db import models

class Transferencia(models.Model):
    transferencia = models.FloatField()
    data_hora = models.DateField(default=datetime.now)


    def __str__(self):
        return str(self.transferencia)