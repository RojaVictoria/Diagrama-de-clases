from alternativa import Alternativa


class Pregunta():
    def __init__(self, enunciado: str, ayuda: str, requerida: bool, alternativas: list) -> None:
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.__alternativas = [Alternativa(a['contenido'], a['ayuda']) for a in alternativas]

    @property
    def alternativas(self) -> list:
        return self.__alternativas

    @alternativas.setter
    def alternativas(self, alternativas: list) -> None:
        self.__alternativas = alternativas

    def mostrar_pregunta(self) -> None:
        print(self.enunciado)

        if self.ayuda:
            print(f"({self.ayuda})")

        for a in self.__alternativas:
            a.mostrar_alternativa()

