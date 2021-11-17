from modelos.materia import Materia

class Individuo:
    id : int
    lista_de_materias : Materia = []
    fitness : float

    #Restrições feridas
    sobreposicao_de_aulas : int = 0
    dependencias_desordenadas : int = 0
    conflito_de_horario_de_professor : int = 0

    def __init__(self, id : int , lista_de_materias : Materia):
        self.id = id
        self.lista_de_materias = lista_de_materias