
from dominio.materia import Materia
from estructuras.grafo import Grafo
from servicios.planificador import PlanificadorAcademico


class Consola:
    """Gestiona la interacción con el usuario desde la terminal."""

    def __init__(self):
        self._grafo = Grafo()
        self._planificador = PlanificadorAcademico(self._grafo)

    def ejecutar(self) -> None:
        """Muestra el menú principal hasta que el usuario salga."""
        while True:
            print("\n===== PLANIFICADOR ACADÉMICO =====")
            print("1. Registrar materia")
            print("2. Registrar prerrequisito")
            print("3. Mostrar materias registradas")
            print("4. Generar plan académico")
            print("5. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self._registrar_materia()
            elif opcion == "2":
                self._registrar_prerrequisito()
            elif opcion == "3":
                self._mostrar_materias()
            elif opcion == "4":
                self._generar_plan()
            elif opcion == "5":
                print("Saliendo del Planificador Académico.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def _registrar_materia(self) -> None:
        """Solicita y registra una materia."""
        codigo = input("Código de la materia: ").strip()
        nombre = input("Nombre de la materia: ").strip()

        try:
            materia = Materia(codigo, nombre)
            self._grafo.agregar_materia(materia)
            print(f"Materia registrada: {materia}")
        except (ValueError, TypeError) as error:
            print(f"No se pudo registrar la materia: {error}")

    def _registrar_prerrequisito(self) -> None:
        """Registra una relación de prerrequisito."""
        codigo_prerrequisito = input(
            "Código de la materia prerrequisito: "
        ).strip()

        codigo_materia = input(
            "Código de la materia que lo necesita: "
        ).strip()

        try:
            self._grafo.agregar_prerrequisito(
                codigo_prerrequisito,
                codigo_materia
            )
            print("Prerrequisito registrado correctamente.")
        except (ValueError, TypeError) as error:
            print(f"No se pudo registrar el prerrequisito: {error}")

    def _mostrar_materias(self) -> None:
        """Muestra las materias registradas."""
        materias = self._grafo.obtener_materias()

        if not materias:
            print("No hay materias registradas.")
            return

        print("\n===== MATERIAS REGISTRADAS =====")

        for materia in materias:
            print(f"- {materia.codigo}: {materia.nombre}")

    def _generar_plan(self) -> None:
        """Genera y muestra el plan académico."""
        try:
            print()
            print(self._planificador.obtener_plan_texto())
        except ValueError as error:
            print(f"No se pudo generar el plan: {error}")
