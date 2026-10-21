
import unittest

from dominio.materia import Materia


class TestMateria(unittest.TestCase):

    def test_crear_materia(self):
        materia = Materia("MAT1", "Matemática I")

        self.assertEqual(materia.codigo, "MAT1")
        self.assertEqual(materia.nombre, "Matemática I")

    def test_eliminar_espacios_exteriores(self):
        materia = Materia(" MAT1 ", " Matemática I ")

        self.assertEqual(materia.codigo, "MAT1")
        self.assertEqual(materia.nombre, "Matemática I")

    def test_rechazar_codigo_vacio(self):
        with self.assertRaises(ValueError):
            Materia("   ", "Matemática I")

    def test_rechazar_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Materia("MAT1", "   ")

    def test_rechazar_codigo_no_textual(self):
        with self.assertRaises(TypeError):
            Materia(123, "Matemática I")

    def test_codigos_iguales_sin_distinguir_mayusculas(self):
        materia1 = Materia("MAT1", "Matemática I")
        materia2 = Materia("mat1", "Otra descripción")

        self.assertEqual(materia1, materia2)
        self.assertEqual(hash(materia1), hash(materia2))


if __name__ == "__main__":
    unittest.main()
