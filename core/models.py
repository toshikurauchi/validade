from datetime import date
from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=512)
    validade = models.DateField(default=date.today)
    quantidade = models.IntegerField(default=1)
    removido_em = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

    @property
    def dias_restantes(self):
        if not hasattr(self, '_dias_restantes'):
            self._dias_restantes = (self.validade - date.today()).days
        return self._dias_restantes

    @property
    def dias_restantes_str(self):
        if self.dias_restantes == 0:
            return 'Vence hoje'
        elif self.dias_restantes == 1:
            return 'Vence amanhã'
        elif self.dias_restantes == -1:
            return 'Venceu ontem'
        elif self.dias_restantes < 1:
            s = 's' if abs(self.dias_restantes) > 1 else ''
            return f'Venceu há {abs(self.dias_restantes)} dia{s}'
        else:
            s = 's' if self.dias_restantes > 1 else ''
            return f'Vence em {self.dias_restantes} dia{s}'

    @property
    def dias_restantes_classe(self):
        if self.dias_restantes < 0:
            return 'vencido'
        elif self.dias_restantes == 0:
            return 'vence-hoje'
        elif self.dias_restantes <= 7:
            return 'vencendo'
        else:
            return 'ok'

    @property
    def vencido(self):
        return self.validade < date.today()

    @property
    def removido(self):
        return self.removido_em is not None

    @property
    def removido_ha(self):
        if not hasattr(self, '_removido_a'):
            self._removido_a = (date.today() - self.removido_em).days
        return self._removido_a

    @property
    def removido_ha_str(self):
        if self.removido_ha == 0:
            return 'Removido hoje'
        elif self.removido_ha == 1:
            return 'Removido ontem'
        elif self.removido_ha == -1:
            return 'Removido amanhã'
        elif self.removido_ha < 1:
            s = 's' if abs(self.removido_ha) > 1 else ''
            return f'Removido em {abs(self.removido_ha)} dia{s}'
        else:
            s = 's' if self.removido_ha > 1 else ''
            return f'Removido há {self.removido_ha} dia{s}'
