from encuesta import Encuesta


class Usuario():
    def __init__(self, correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, correo: str) -> None:
        self.__correo = correo

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, edad: int) -> None:
        self.__edad = edad

    @property
    def region(self) -> int:
        return self.__region

    @region.setter
    def region(self, region: int) -> None:
        self.__region = region

    @staticmethod
    def contestar_encuesta(encuesta: Encuesta):
        encuesta.mostrar_encuesta()
