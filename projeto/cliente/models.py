from tkinter import CASCADE
from django.db import models
# from conta_do_banco.models import ContaBanco

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    # banco = models.ForeignKey(ContaBanco, on_delete=CASCADE)

    def __str__(self):
        return self.nome