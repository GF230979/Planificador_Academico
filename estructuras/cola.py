
from collections import deque
from typing import Generic, TypeVar


T = TypeVar("T")


class Cola(Generic[T]):
    """Implementa una cola FIFO: primero en entrar, primero en salir."""

    def __init__(self):
        self._elementos = deque()

    def esta_vacia(self) -> bool:
        """Indica si la cola no contiene elementos."""
        return len(self._elementos) == 0

    def encolar(self, elemento: T) -> None:
        """Agrega un elemento al final de la cola."""
        self._elementos.append(elemento)

    def desencolar(self) -> T:
        """Retira y devuelve el primer elemento de la cola."""
        if self.esta_vacia():
            raise IndexError(
                "No se puede desencolar: la cola está vacía."
            )

        return self._elementos.popleft()

    def frente(self) -> T:
        """Devuelve el primer elemento sin retirarlo."""
        if self.esta_vacia():
            raise IndexError(
                "No se puede consultar el frente: la cola está vacía."
            )

        return self._elementos[0]

    def tamano(self) -> int:
        """Devuelve la cantidad de elementos de la cola."""
        return len(self._elementos)

    def __len__(self) -> int:
        """Permite consultar el tamaño mediante len()."""
        return len(self._elementos)
