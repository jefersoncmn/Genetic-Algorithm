def procurar_materia_por_horario_e_periodo(lista_de_materias, horario, periodo):
    for materia in range(25):
        
        if lista_de_materias[materia].periodo == periodo:
            for horarios in range(len(lista_de_materias[materia].horarios)):
                if lista_de_materias[materia].horarios[horarios] == horario:
                    return  lista_de_materias[materia]

def procurar_materia_por_id(lista_de_materias, id):
    for materia in range(25):
        if lista_de_materias[materia].id == id:
            return lista_de_materias[materia]