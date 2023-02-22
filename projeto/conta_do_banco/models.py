from django.db import models
from cliente.models import Cliente
from deposito.models import Deposito

class ContaBanco(models.Model):
    num_conta = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo = models.FloatField()

    def __str__(self):
        return str(self.num_conta)


