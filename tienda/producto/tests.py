from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class ProductoTests(TestCase):

    def test_url_insertar_producto(self):
        """Verifica que la URL /producto/insertar/ devuelva un código de estatus 200."""
        response = self.client.get('/producto/insertar/')
        self.assertEqual(response.status_code, 200)

    def test_url_reversa_insertar_producto(self):
        """Prueba de validación de URL disponible por nombre del enlace reverso de: insertar-pro."""
        response = self.client.get(reverse('insertar-pro'))
        self.assertEqual(response.status_code, 200)

    def test_nombre_correcto_template_insertar(self):
        """Verifica si el nombre es correcto con relación a la plantilla de insertar y su nombre reverso."""
        response = self.client.get(reverse('insertar-pro'))
        self.assertTemplateUsed(response, 'insertar.html')

    def test_contenido_template_insertar(self):
        """Verifica si un contenido corresponde a la plantilla, por ejemplo: '<td>Nombre del Producto</td>'."""
        response = self.client.get(reverse('insertar-pro'))
        self.assertContains(response, '<td>Nombre del Producto</td>')
