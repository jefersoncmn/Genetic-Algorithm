class Materia:
    horarios = []
    nome = ""
    professor = ""
    cargahoraria = 0 
    dependencias = []
    punicao = 0

    def __init__(self, id, nome, professor, cargahoraria, dependencias, periodo):
        self.id = id
        self.nome = nome
        self.professor = professor
        self.cargahoraria = cargahoraria
        self.dependencias = dependencias
        self.periodo = periodo
        