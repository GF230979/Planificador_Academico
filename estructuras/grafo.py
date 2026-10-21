
from dominio.materia import Materia


class Grafo:
    """
    Representa un grafo dirigido de materias y prerrequisitos.

    Cada materia es un vértice.
    Cada relación de prerrequisito es una arista dirigida
    desde la materia prerrequisito hacia la materia dependiente.
    """

    def __init__(self):
        self._materias = {}
        self._adyacencias = {}

    def agregar_materia(self, materia: Materia) -> None:
        """Agrega una materia al grafo."""
        if not isinstance(materia, Materia):
            raise TypeError(
                "Solo se pueden agregar objetos de tipo Materia."
            )

        codigo = materia.codigo.casefold()

        if codigo in self._materias:
            raise ValueError(
                f"Ya existe una materia con el código "
                f"'{materia.codigo}'."
            )

        self._materias[codigo] = materia
        self._adyacencias[codigo] = []

    def agregar_prerrequisito(
        self,
        codigo_prerrequisito: str,
        codigo_materia: str
    ) -> None:
        """
        Registra una relación dirigida:
        prerrequisito -> materia que lo necesita.
        """
        prerrequisito = self._normalizar_codigo(
            codigo_prerrequisito
        )
        materia = self._normalizar_codigo(codigo_materia)

        if prerrequisito not in self._materias:
            raise ValueError(
                f"No existe la materia prerrequisito "
                f"'{codigo_prerrequisito}'."
            )

        if materia not in self._materias:
            raise ValueError(
                f"No existe la materia '{codigo_materia}'."
            )

        if prerrequisito == materia:
            raise ValueError(
                "Una materia no puede ser prerrequisito de sí misma."
            )

        if materia in self._adyacencias[prerrequisito]:
            raise ValueError(
                "Esta relación de prerrequisito ya existe."
            )

        self._adyacencias[prerrequisito].append(materia)

    def obtener_materias(self) -> list[Materia]:
        """Devuelve las materias registradas en el grafo."""
        return list(self._materias.values())

    def obtener_adyacentes(
        self,
        codigo_materia: str
    ) -> list[Materia]:
        """Devuelve las materias que dependen de una materia dada."""
        codigo = self._normalizar_codigo(codigo_materia)

        if codigo not in self._materias:
            raise ValueError(
                f"No existe la materia '{codigo_materia}'."
            )

        return [
            self._materias[codigo_adyacente]
            for codigo_adyacente in self._adyacencias[codigo]
        ]

    def obtener_grado_entrada(self) -> dict[str, int]:
        """
        Calcula cuántos prerrequisitos tiene cada materia.
        Devuelve un diccionario con código y cantidad.
        """
        grados = {
            codigo: 0
            for codigo in self._materias
        }

        for adyacentes in self._adyacencias.values():
            for codigo_adyacente in adyacentes:
                grados[codigo_adyacente] += 1

        return grados

    def cantidad_materias(self) -> int:
        """Devuelve la cantidad de materias registradas."""
        return len(self._materias)

    def cantidad_relaciones(self) -> int:
        """Devuelve la cantidad de relaciones de prerrequisito."""
        return sum(
            len(adyacentes)
            for adyacentes in self._adyacencias.values()
        )

    @staticmethod
    def _normalizar_codigo(codigo: str) -> str:
        """Valida y normaliza un código de materia."""
        if not isinstance(codigo, str):
            raise TypeError(
                "El código de materia debe ser una cadena de texto."
            )

        codigo = codigo.strip()

        if not codigo:
            raise ValueError(
                "El código de materia no puede estar vacío."
            )

        return codigo.casefold()
