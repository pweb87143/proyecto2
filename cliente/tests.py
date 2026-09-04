from django.test import TestCase
from django.urls import reverse

from .models import Cliente


class ClienteCrudTests(TestCase):
    def test_lista_clientes_carga(self):
        response = self.client.get(reverse('cliente_listar'))
        self.assertEqual(response.status_code, 200)

    def test_crear_cliente(self):
        data = {
            'nombre': 'Ana López',
            'email': 'ana@example.com',
            'telefono': '555123456',
        }

        response = self.client.post(reverse('cliente_crear'), data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cliente.objects.filter(email='ana@example.com').exists())
