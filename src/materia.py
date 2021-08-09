class Materia:
    horarios = []
    id = 0 
    nome = ""
    professor = ""
    cargahoraria = 0 
    dependencias = []
    periodo = 0

    def __init__(self, id, nome, professor, cargahoraria, dependencias):
        self.id = id
        self.nome = nome
        self.professor = professor
        self.cargahoraria = cargahoraria
        self.dependencias = dependencias
        