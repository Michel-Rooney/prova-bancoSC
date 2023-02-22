from django.shortcuts import render
from .models import ContaBanco
from deposito.models import Deposito
from transferencia.models import Transferencia

def index(request):
    conta_banco = ContaBanco.objects.all().first()
    deposito = Deposito.objects.all()
    transferencia = Transferencia.objects.all()

    gastos_sum = calcula_transferencia(transferencia)
    deposito_sum = calcula_deposito(deposito)
    saldo = calcula_saldo(conta_banco, gastos_sum, deposito_sum)


    dados = {
        'conta' : conta_banco,
        'deposito' : deposito,
        'transferencia' : transferencia,
        'deposito_sum' : deposito_sum,
        'gastos' : gastos_sum,
        'saldo' : saldo,

    }

    return render(request, 'index.html', dados)


def calcula_saldo(conta_banco, gastos_sum, deposito_sum):
    saldo = (conta_banco.saldo - gastos_sum) + deposito_sum
    return saldo

def calcula_deposito(deposito):
    valor = 0
    for depo in deposito:
        valor += depo.deposito

    return valor

def calcula_transferencia(transferencia):
    valor = 0
    for trans in transferencia:
        valor += trans.transferencia

    return valor


