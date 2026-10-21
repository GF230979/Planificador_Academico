
from estructuras.cola import Cola
from estructuras.grafo import Grafo


class PlanificadorAcademico:
    """Planifica materias según sus relaciones de prerrequisitos."""

    def __init__(self, grafo: Grafo):
        if not isinstance(grafo, Grafo):
            raise TypeError(
                "El planificador necesita un objeto de tipo Grafo."
            )

        self._grafo = grafo

    def planificar(self) -> list[list]:
        """
        Ordena las materias por niveles mediante el algoritmo de Kahn.

        Cada nivel contiene materias que pueden cursarse una vez
        completados los niveles anteriores.
        """
        materias = self._grafo.obtener_materias()
        adyacencias = {
            materia.codigo.casefold(): self._grafo.obtener_adyacentes(
                materia.codigo
            )
            for materia in materias
        }

        grados_entrada = self._grafo.obtener_grado_entrada()
        cola = Cola()

        for materia in materias:
            codigo = materia.codigo.casefold()

            if grados_entrada[codigo] == 0:
                cola.encolar(materia)

        niveles = []
        procesadas = 0

        while not cola.esta_vacia():
            cantidad_nivel = cola.tamano()
            nivel_actual = []

            for _ in range(cantidad_nivel):
                materia = cola.desencolar()
                nivel_actual.append(materia)
                procesadas += 1

                codigo = materia.codigo.casefold()

                for adyacente in adyacencias[codigo]:
                    codigo_adyacente = adyacente.codigo.casefold()
                    grados_entrada[codigo_adyacente] -= 1

                    if grados_entrada[codigo_adyacente] == 0:
                        cola.encolar(adyacente)

            niveles.append(nivel_actual)

        if procesadas != len(materias):
            raise ValueError(
                "No se puede generar el plan: "
                "el grafo contiene un ciclo de prerrequisitos."
            )

        return niveles

    def obtener_plan_texto(self) -> str:
        """Devuelve el plan académico en formato de texto."""
        niveles = self.planificar()

        if not niveles:
            return "No hay materias registradas en el plan académico."

        lineas = ["PLAN ACADÉMICO POR NIVELES", ""]

        for numero, nivel in enumerate(niveles, start=1):
            lineas.append(f"Nivel {numero}:")

            for materia in nivel:
                lineas.append(f"  - {materia.codigo}: {materia.nombre}")

            lineas.append("")

        return "\n".join(lineas).rstrip()
