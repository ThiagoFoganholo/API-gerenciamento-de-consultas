from django.test import TestCase
from .models import Profissional

class ProfissionalModelTest(TestCase):
    def test_criar_profissional(self):
        profissional = Profissional.objects.create(
            nome_completo="João Silva",
            nome_social="Joana Silva",
            profissao="Médico",
            endereco="Rua A, 123",
            contato="123456789"
        )
        self.assertEqual(profissional.nome_completo, "João Silva")

