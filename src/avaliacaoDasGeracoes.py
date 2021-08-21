from funcoesDeBusca import procurar_materia_por_horario_e_periodo, verificar_existencia_de_materia_em_periodo
from materia import Materia

peso_punicao_conflito_de_horario_de_professor = 70

peso_punicao_dependencias_ordenadas = 50


def verificar_dependencias_de_todas_materias(lista_de_materias):
    for materia in range(len(lista_de_materias)):
        if verificar_dependencias_de_materia(lista_de_materias ,lista_de_materias[materia]):
            lista_de_materias[materia].punicao += peso_punicao_dependencias_ordenadas 


def verificar_dependencias_de_materia(lista_de_materias, materia):
    dependencias_ordenadas : bool = False

    print("Materia a ser verificado: "+materia.nome)
    print(materia.dependencias)
    if materia.dependencias:
        for materiaRequisitante in range(0, len(materia.dependencias)):
            dependencias_ordenadas = False
            print("Requisito a ser procurado:"+materia.dependencias[materiaRequisitante])
            for periodo in range(1, materia.periodo-1):
                if verificar_existencia_de_materia_em_periodo(lista_de_materias, materia, periodo) == True:
                    print("Materia "+materia.dependencias[materiaRequisitante]+" encotrada no periodo "+str(periodo))
                    dependencias_ordenadas = True
    else:
        dependencias_ordenadas = True

    print("Dependencias ordenadas "+str(dependencias_ordenadas))
    return dependencias_ordenadas

def verificar_conflitos_de_horarios_de_professor_de_todas_materias(lista_de_materias):
    for materia in range(25):
        if verificar_conflitos_de_horarios_de_professor(lista_de_materias, lista_de_materias[materia]) == True:
            lista_de_materias[materia].punicao += peso_punicao_conflito_de_horario_de_professor

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