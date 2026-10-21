
class Materia:
    """
    Representa una materia del plan de estudios.

    Atributos:
        codigo: Identificador único de la materia.
        nombre: Nombre descriptivo de la materia.
    """

    def __init__(self, codigo: str, nombre: str):
        self.codigo = self._validar_texto(codigo, "El código")
        self.nombre = self._validar_texto(nombre, "El nombre")

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        """
        Valida que el campo sea texto y no esté vacío.
        Elimina espacios al inicio y al final.
        """
        if not isinstance(valor, str):
            raise TypeError(
                f"{campo} debe ser una cadena de texto."
            )

        valor = valor.strip()

        if not valor:
            raise ValueError(
                f"{campo} no puede estar vacío."
            )

        return valor

    def __eq__(self, otra) -> bool:
        """
        Dos materias son iguales si tienen el mismo código,
        sin distinguir mayúsculas y minúsculas.
        """
        if not isinstance(otra, Materia):
            return NotImplemented

        return self.codigo.casefold() == otra.codigo.casefold()

    def __hash__(self) -> int:
        """Permite utilizar materias en conjuntos y diccionarios."""
        return hash(self.codigo.casefold())

    def __str__(self) -> str:
        """Devuelve una representación legible de la materia."""
        return f"{self.codigo} - {self.nombre}"

    def __repr__(self) -> str:
        """Devuelve una representación útil para depuración."""
        return (
            f"Materia(codigo={self.codigo!r}, "
            f"nombre={self.nombre!r})"
        )
