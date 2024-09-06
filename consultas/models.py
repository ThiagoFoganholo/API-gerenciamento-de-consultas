from django.db import models

class Profissional(models.Model):
    nome_completo = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    profissao = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo

class Consulta(models.Model):
    data_consulta = models.DateTimeField()
    profissional = models.ForeignKey(Profissional, related_name='consultas', on_delete=models.CASCADE)

    def __str__(self):
        return f"Consulta com {self.profissional.nome_completo} em {self.data_consulta}"
