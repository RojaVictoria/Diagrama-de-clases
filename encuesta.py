from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas
from typing import List


class Encuesta():
    def __init__(self, nombre: str, preguntas: List[dict]) -> None:
        self.nombre = nombre
        self.__preguntas = [Pregunta(p['enunciado'], p['ayuda'], p['requerida'], p['alternativas']) for p in preguntas]
        self.__respuestas = []

    def mostrar_encuesta(self) -> None:
        print(self.nombre)

        for p in self.__preguntas:
            p.mostrar_pregunta()

    def agregar_respuestas(self, respuestas) -> None:
        self.__respuestas.append(respuestas)


class EncuestaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list, edad_min: int, edad_max: int) -> None:
        super().__init__(nombre, preguntas)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    @property
    def edad_min(self) -> int:
        return self.__edad_min

    @edad_min.setter
    def edad_min(self, edad_min) -> None:
        self.__edad_min = edad_min

    @property
    def edad_max(self) -> int:
        return self.__edad_max

    @edad_max.setter
    def edad_max(self, edad_max) -> None:
        self.__edad_max = edad_max

    def agregar_respuesta(self, respuestas: ListadoRespuestas):
        if self.__edad_min <= respuestas.usuario.edad <= self.__edad_max:
            super().agregar_respuestas(respuestas)


class EncuestaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list, regiones: List[int]) -> None:
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    @property
    def regiones(self) -> List[int]:
        return self.__regiones

    @regiones.setter
    def regiones(self, regiones) -> None:
        self.__regiones = regiones

    def agregar_respuesta(self, respuestas: ListadoRespuestas) -> None:
        if respuestas.usuario.region in self.__regiones:
            super().agregar_respuestas(respuestas)
