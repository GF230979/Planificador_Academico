
import unittest

from dominio.materia import Materia
from estructuras.grafo import Grafo
from servicios.planificador import PlanificadorAcademico


class TestPlanificadorAcademico(unittest.TestCase):

    def setUp(self):
        self.grafo = Grafo()

        self.matematica1 = Materia("MAT101", "Matemática I")
        self.matematica2 = Materia("MAT102", "Matemática II")
        self.fisica1 = Materia("FIS101", "Física I")
        self.programacion1 = Materia("PRG101", "Programación I")

    def test_planificar_grafo_vacio(self):
        planificador = PlanificadorAcademico(self.grafo)

        self.assertEqual(planificador.planificar(), [])
        self.assertEqual(
            planificador.obtener_plan_texto(),
            "No hay materias registradas en el plan académico."
        )

    def test_una_materia_sin_prerrequisitos(self):
        self.grafo.agregar_materia(self.matematica1)

        planificador = PlanificadorAcademico(self.grafo)
        niveles = planificador.planificar()

        self.assertEqual(len(niveles), 1)
        self.assertEqual(niveles[0], [self.matematica1])

    def test_respetar_orden_de_prerrequisitos(self):
        self.grafo.agregar_materia(self.matematica1)
        self.grafo.agregar_materia(self.matematica2)

        self.grafo.agregar_prerrequisito("MAT101", "MAT102")

        planificador = PlanificadorAcademico(self.grafo)
        niveles = planificador.planificar()

        self.assertEqual(len(niveles), 2)
        self.assertEqual(niveles[0], [self.matematica1])
        self.assertEqual(niveles[1], [self.matematica2])

    def test_materias_independientes_en_el_mismo_nivel(self):
        self.grafo.agregar_materia(self.matematica1)
        self.grafo.agregar_materia(self.fisica1)
        self.grafo.agregar_materia(self.programacion1)

        planificador = PlanificadorAcademico(self.grafo)
        niveles = planificador.planificar()

        self.assertEqual(len(niveles), 1)
        self.assertEqual(
            {materia.codigo for materia in niveles[0]},
            {"MAT101", "FIS101", "PRG101"}
        )


    def test_agrupar_materias_por_niveles(self):
        self.grafo.agregar_materia(self.matematica1)
        self.grafo.agregar_materia(self.matematica2)
        self.grafo.agregar_materia(self.fisica1)
        self.grafo.agregar_materia(self.programacion1)

        self.grafo.agregar_prerrequisito("MAT101", "MAT102")
        self.grafo.agregar_prerrequisito("MAT102", "FIS101")

        planificador = PlanificadorAcademico(self.grafo)
        niveles = planificador.planificar()

        self.assertEqual(len(niveles), 3)

        self.assertEqual(
            {materia.codigo for materia in niveles[0]},
            {"MAT101", "PRG101"}
        )

        self.assertEqual(
            {materia.codigo for materia in niveles[1]},
            {"MAT102"}
        )

        self.assertEqual(
            {materia.codigo for materia in niveles[2]},
            {"FIS101"}
        )

    def test_detectar_ciclo(self):
        self.grafo.agregar_materia(self.matematica1)
        self.grafo.agregar_materia(self.matematica2)

        self.grafo.agregar_prerrequisito("MAT101", "MAT102")
        self.grafo.agregar_prerrequisito("MAT102", "MAT101")

        planificador = PlanificadorAcademico(self.grafo)

        with self.assertRaisesRegex(ValueError, "contiene un ciclo"):
            planificador.planificar()

    def test_rechazar_objeto_que_no_es_grafo(self):
        with self.assertRaises(TypeError):
            PlanificadorAcademico("no es un grafo")

    def test_generar_plan_en_texto(self):
        self.grafo.agregar_materia(self.matematica1)
        self.grafo.agregar_materia(self.matematica2)

        self.grafo.agregar_prerrequisito("MAT101", "MAT102")

        planificador = PlanificadorAcademico(self.grafo)
        resultado = planificador.obtener_plan_texto()

        self.assertIn("PLAN ACADÉMICO POR NIVELES", resultado)
        self.assertIn("Nivel 1:", resultado)
        self.assertIn("MAT101: Matemática I", resultado)
        self.assertIn("Nivel 2:", resultado)
        self.assertIn("MAT102: Matemática II", resultado)


if __name__ == "__main__":
    unittest.main()
