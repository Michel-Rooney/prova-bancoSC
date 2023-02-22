from datetime import datetime
from django.db import models

class Deposito(models.Model):
    deposito = models.FloatField()
    data_hora = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return str(self.deposito)