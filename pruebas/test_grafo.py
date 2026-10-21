
import unittest

from dominio.materia import Materia
from estructuras.grafo import Grafo


class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.grafo = Grafo()

        self.materia1 = Materia("MAT101", "Matemática I")
        self.materia2 = Materia("MAT102", "Matemática II")
        self.materia3 = Materia("FIS101", "Física I")

    def test_grafo_inicia_vacio(self):
        self.assertEqual(self.grafo.cantidad_materias(), 0)
        self.assertEqual(self.grafo.cantidad_relaciones(), 0)
        self.assertEqual(self.grafo.obtener_materias(), [])

    def test_agregar_materia(self):
        self.grafo.agregar_materia(self.materia1)

        self.assertEqual(self.grafo.cantidad_materias(), 1)
        self.assertEqual(
            self.grafo.obtener_materias(),
            [self.materia1]
        )

    def test_rechazar_materia_duplicada(self):
        self.grafo.agregar_materia(self.materia1)

        with self.assertRaises(ValueError):
            self.grafo.agregar_materia(
                Materia("mat101", "Otra Matemática")
            )

    def test_rechazar_objeto_que_no_es_materia(self):
        with self.assertRaises(TypeError):
            self.grafo.agregar_materia("MAT101")

    def test_agregar_prerrequisito(self):
        self.grafo.agregar_materia(self.materia1)
        self.grafo.agregar_materia(self.materia2)

        self.grafo.agregar_prerrequisito("MAT101", "MAT102")

        self.assertEqual(self.grafo.cantidad_relaciones(), 1)
        self.assertEqual(
            self.grafo.obtener_adyacentes("MAT101"),
            [self.materia2]
        )

    def test_grado_entrada(self):
        self.grafo.agregar_materia(self.materia1)
        self.grafo.agregar_materia(self.materia2)
        self.grafo.agregar_materia(self.materia3)

        self.grafo.agregar_prerrequisito("MAT101", "MAT102")
        self.grafo.agregar_prerrequisito("FIS101", "MAT102")

        grados = self.grafo.obtener_grado_entrada()

        self.assertEqual(grados["mat101"], 0)
        self.assertEqual(grados["mat102"], 2)
        self.assertEqual(grados["fis101"], 0)

    def test_rechazar_prerrequisito_inexistente(self):
        self.grafo.agregar_materia(self.materia2)

        with self.assertRaises(ValueError):
            self.grafo.agregar_prerrequisito("MAT999", "MAT102")

    def test_rechazar_materia_dependiente_inexistente(self):
        self.grafo.agregar_materia(self.materia1)

        with self.assertRaises(ValueError):
            self.grafo.agregar_prerrequisito("MAT101", "MAT999")

    def test_rechazar_materia_como_su_propio_prerrequisito(self):
        self.grafo.agregar_materia(self.materia1)

        with self.assertRaises(ValueError):
            self.grafo.agregar_prerrequisito("MAT101", "MAT101")

    def test_rechazar_relacion_duplicada(self):
        self.grafo.agregar_materia(self.materia1)
        self.grafo.agregar_materia(self.materia2)

        self.grafo.agregar_prerrequisito("MAT101", "MAT102")

        with self.assertRaises(ValueError):
            self.grafo.agregar_prerrequisito("MAT101", "MAT102")

    def test_codigos_sin_distinguir_mayusculas(self):
        self.grafo.agregar_materia(self.materia1)
        self.grafo.agregar_materia(self.materia2)

        self.grafo.agregar_prerrequisito("mat101", "mat102")

        self.assertEqual(
            self.grafo.obtener_adyacentes("MAT101"),
            [self.materia2]
        )


if __name__ == "__main__":
    unittest.main()
