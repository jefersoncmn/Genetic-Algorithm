def verificar_dependencias_da_materia(lista_de_materias):
    return

def verificar_conflitos_de_horarios_de_professor(lista_de_materias):
    conflitante = False

    for materia in range(25):
        print("Materia a ser verificado: "+lista_de_materias[materia].nome)
        print(lista_de_materias[materia].dependencias)
        if lista_de_materias[materia].dependencias:
            for materiaRequisitante in range(len(lista_de_materias[materia].dependencias)):
                print("Materia que tem requisitos:"+lista_de_materias[materia].nome)
                for periodo in range(1, lista_de_materias[materia].periodo):
                    if procurar_materia_por_horario_e_periodo(lista_de_materias, lista_de_materias[materia].horarios, periodo):
                        print("Materia :"+lista_de_materias[materia]+" comparado com "+procurar_materia_por_horario_e_periodo(lista_de_materias[materia], lista_de_materias[materia].horario, periodo).nome)
                        conflitante = True
                    else:
                        print("Materia :"+lista_de_materias[materia]+" comparado com "+procurar_materia_por_horario_e_periodo(lista_de_materias[materia], lista_de_materias[materia].horario, periodo).nome)
    return conflitante

def procurar_materia_por_horario_e_periodo(lista_de_materias, horario, periodo):
    for materia in range(25):
        
        if lista_de_materias[materia].periodo == periodo:
            for horarios in range(len(lista_de_materias[materia].horarios)):
                if lista_de_materias[materia].horarios[horarios] == horario:
                    return  lista_de_materias[materia]