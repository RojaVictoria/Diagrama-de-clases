from usuario import Usuario


class ListadoRespuestas():
    def __init__(self, respuestas: list):
        self.__respuestas = respuestas
        self.__usuario = []

    @property
    def usuario(self) -> [Usuario]:
        return self.__usuario

    def agregar_usuario(self, correo: str, edad: int, region: int) -> None:
        self.__usuario.append(Usuario(correo, edad, region))

    @property
    def respuestas(self) -> list:
        return self.__respuestas

    @respuestas.setter
    def respuestas(self, respuestas: list) -> None:
        self.__respuestas = respuestas
