from django.db import models

class Parametros(models.Model):
    alcalinidade = models.FloatField(max_length=30)
    ph = models.FloatField(max_length=30)
    cloro = models.FloatField(max_length=30)
    agua = models.FloatField(max_length=30)

    @property
    def trat_alcalinidade(self):
        if self.alcalinidade <= 40:
            return self.agua * 180
        if self.alcalinidade <= 60:
            return self.agua * 108
        if self.alcalinidade <= 80:
            return self.agua * 72
        if self.alcalinidade <= 120:
            return 'A Alcalinidade Total está boa.'
        elif self.alcalinidade > 120:
            return (self.alcalinidade - 120) * 10 * self.agua

    @property
    def trat_ph(self):
        if self.ph < 6.8:
            return self.agua * 10
        if self.ph < 7:
            return self.agua * 5
        if self.cloro < 7.4:
            return "O PH da água está bom"
        if self.ph <= 8:
            return self.agua * 13
        else:
            return self.agua * 25

    @property
    def trat_cloro(self):
        if self.cloro < 1:
            return self.agua * 5
        if self.cloro <= 3:
            return "A quantidade de cloro na piscina está adequada"
        else:
            return 'Aguarde 6h e repita o teste'

    def __str__(self):
        """String representando o objeto."""
        return f'{self.alcalinidade}, {self.ph}, {self.cloro}, {self.agua}'