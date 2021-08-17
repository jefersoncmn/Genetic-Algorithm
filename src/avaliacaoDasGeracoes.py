from materia import Materia

peso_punicao_conflito_de_horario_de_professor = 70

def verificar_dependencias_da_materia(lista_de_materias):
    conflitante = False

    for materia in range(25):
        print("Materia a ser verificado: "+lista_de_materias[materia].nome)
        print(lista_de_materias[materia].dependencias)
        if lista_de_materias[materia].dependencias:
            for materiaRequisitante in range(len(lista_de_materias[materia].dependencias)):
                print("Requisito a ser procurado:"+lista_de_materias[materia].dependencias[materiaRequisitante])
                for periodo in range(1, lista_de_materias[materia].periodo):
                    if procurar_materia_por_id(lista_de_materias, lista_de_materias[materia].id):
                        print("Materia :"+lista_de_materias[materia]+" comparado com "+procurar_materia_por_horario_e_periodo(lista_de_materias[materia], lista_de_materias[materia].horario, periodo).nome)
                        conflitante = True
                    else:
                        print("Materia :"+lista_de_materias[materia]+" comparado com "+procurar_materia_por_horario_e_periodo(lista_de_materias[materia], lista_de_materias[materia].horario, periodo).nome)
    return conflitante

def verificar_conflitos_de_horarios_de_professor_de_todas_materias(lista_de_materias):
    for materia in range(25):
        if verificar_conflitos_de_horarios_de_professor(lista_de_materias, lista_de_materias[materia]) == True:
            lista_de_materias[materia].punicao = peso_punicao_conflito_de_horario_de_professor

def verificar_conflitos_de_horarios_de_professor(lista_de_materias, materia):
    conflitante = False
    #print("Materia a ser verificado: "+materia.nome)
    #print("Professor da materia: "+materia.professor)
    #print(materia.horarios)
    for horarios in range(len(materia.horarios)):
        for periodo in range(1,5):
            materia2 = procurar_materia_por_horario_e_periodo(lista_de_materias, materia.horarios[horarios], periodo)
            if materia2 and materia2 != materia:
                #print(materia2.professor+" - horario :"+str(materia2.horarios))
                if materia.professor == materia2.professor:
                    conflitante = True
                    #print("Conflito encontrado")
    return conflitante        

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