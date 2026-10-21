
import unittest

from estructuras.cola import Cola


class TestCola(unittest.TestCase):

    def test_cola_inicia_vacia(self):
        cola = Cola()

        self.assertTrue(cola.esta_vacia())
        self.assertEqual(cola.tamano(), 0)
        self.assertEqual(len(cola), 0)

    def test_encolar_elementos(self):
        cola = Cola()

        cola.encolar("MAT101")
        cola.encolar("MAT102")

        self.assertFalse(cola.esta_vacia())
        self.assertEqual(cola.tamano(), 2)

    def test_desencolar_respeta_orden_fifo(self):
        cola = Cola()

        cola.encolar("MAT101")
        cola.encolar("MAT102")
        cola.encolar("MAT103")

        self.assertEqual(cola.desencolar(), "MAT101")
        self.assertEqual(cola.desencolar(), "MAT102")
        self.assertEqual(cola.desencolar(), "MAT103")

        self.assertTrue(cola.esta_vacia())

    def test_frente_no_elimina_elemento(self):
        cola = Cola()

        cola.encolar("MAT101")
        cola.encolar("MAT102")

        self.assertEqual(cola.frente(), "MAT101")
        self.assertEqual(cola.tamano(), 2)
        self.assertEqual(cola.desencolar(), "MAT101")

    def test_desencolar_cola_vacia(self):
        cola = Cola()

        with self.assertRaises(IndexError):
            cola.desencolar()

    def test_consultar_frente_cola_vacia(self):
        cola = Cola()

        with self.assertRaises(IndexError):
            cola.frente()

    def test_tamano_se_actualiza_al_desencolar(self):
        cola = Cola()

        cola.encolar("MAT101")
        cola.encolar("MAT102")
        cola.desencolar()

        self.assertEqual(cola.tamano(), 1)
        self.assertEqual(len(cola), 1)


if __name__ == "__main__":
    unittest.main()
