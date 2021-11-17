from funcoesDeBusca import procurar_materia_por_horario_e_periodo, verificar_existencia_de_materia_em_periodo
from modelos.individuo import Individuo
from modelos.materia import Materia

peso_punicao_conflito_de_horario_de_professor = 5

peso_punicao_dependencias_desordenadas = 5

peso_punicao_aulas_sobrepostas = 1

def verificacao_da_geracao(geracao : Individuo):
    for individuo in range(len(geracao)):
        verificar_individuo(geracao[individuo])

def verificar_individuo(individuo : Individuo):
    limpar_punicoes_do_individuo(individuo) #Primeiro é limpo caso ele tenha punições armazenadas
    verificar_sobreposicao_de_todas_materias(individuo)
    verificar_conflitos_de_horarios_de_professor_de_todas_materias(individuo)
    #verificar_dependencias_de_todas_materias(individuo)

def verificar_sobreposicao_de_todas_materias(individuo : Individuo):
    #print("Individuo a ser verificado sobreposicao de todas materias: "+str(individuo.id))
    for materia in range(len(individuo.lista_de_materias)):
        #print("Materia: "+individuo.lista_de_materias[materia].nome+ " periodo: "+str(individuo.lista_de_materias[materia].periodo))
        #if verificar_sobreposicao_de_materia(individuo, individuo.lista_de_materias[materia]) == True:
        verificar_sobreposicao_de_materia(individuo, individuo.lista_de_materias[materia])
        #individuo.lista_de_materias[materia].punicao += peso_punicao_aulas_sobrepostas
            

#Função que verifica se os horários da "materia" se repetem em outras matérias da lista de matérias
def verificar_sobreposicao_de_materia(individuo : Individuo, materia : Materia):
    horarios_ocupados : int = []

    for materia_ in range(len(individuo.lista_de_materias)):
        if individuo.lista_de_materias[materia_].periodo == materia.periodo:
            #print("Comparacao de "+materia.nome+" periodo "+str(materia.periodo)+" horarios "+str(materia.horarios)+" \ "+lista_de_materias[materia_].nome+" periodo "+str(lista_de_materias[materia_].periodo)+" horarios "+str(lista_de_materias[materia_].horarios))
            for horario in range(len(individuo.lista_de_materias[materia_].horarios)):
                if individuo.lista_de_materias[materia_].horarios[horario] in horarios_ocupados: 
                    #print("Sobreposicao aconteceu")
                    individuo.sobreposicao_de_aulas += 1
                    individuo.lista_de_materias[materia_].punicao += peso_punicao_aulas_sobrepostas
                    #return True
                else:
                    horarios_ocupados.append(individuo.lista_de_materias[materia_].horarios[horario])
    #return False

def verificar_dependencias_de_todas_materias(individuo : Individuo):
    for materia in range(len(individuo.lista_de_materias)):
        if verificar_dependencias_de_materia(individuo.lista_de_materias ,individuo.lista_de_materias[materia]):
            individuo.lista_de_materias[materia].punicao += peso_punicao_dependencias_desordenadas
            individuo.dependencias_desordenadas += 1


def verificar_dependencias_de_materia(lista_de_materias, materia):
    dependencias_ordenadas : bool = False

    #print("Materia a ser verificado: "+materia.nome)
    #print(materia.dependencias)
    if materia.dependencias:
        for materiaRequisitante in range(0, len(materia.dependencias)):
            dependencias_ordenadas = False
            #print("Requisito a ser procurado:"+materia.dependencias[materiaRequisitante])
            for periodo in range(1, materia.periodo-1):
                if verificar_existencia_de_materia_em_periodo(lista_de_materias, materia, periodo) == True:
                    #print("Materia "+materia.dependencias[materiaRequisitante]+" encotrada no periodo "+str(periodo))
                    dependencias_ordenadas = True
    else:
        dependencias_ordenadas = True

    #print("Dependencias ordenadas "+str(dependencias_ordenadas))
    return dependencias_ordenadas

def verificar_conflitos_de_horarios_de_professor_de_todas_materias(individuo : Individuo):
    for materia in range(25):
        if verificar_conflitos_de_horarios_de_professor(individuo.lista_de_materias, individuo.lista_de_materias[materia]) == True:
            individuo.lista_de_materias[materia].punicao += peso_punicao_conflito_de_horario_de_professor
            individuo.conflito_de_horario_de_professor += 1

def verificar_conflitos_de_horarios_de_professor(lista_de_materias : Materia, materia : Materia):
    #print("Materia a ser verificado: "+materia.nome)
    #print("Professor da materia: "+materia.professor)
    #print(materia.horarios)
    for horarios in range(len(materia.horarios)):
        for periodo in range(1,5):
            materia2 : Materia = procurar_materia_por_horario_e_periodo(lista_de_materias, materia.horarios[horarios], periodo)
            if materia2 and materia2 != materia:
                #print(materia2.professor+" - horario :"+str(materia2.horarios)+" periodo "+str(materia2.periodo))
                if materia.professor == materia2.professor:
                    #print("Conflito encontrado")
                    return True
    return False

def limpar_punicoes_do_individuo(individuo : Individuo):
    individuo.sobreposicao_de_aulas = 0
    individuo.dependencias_desordenadas = 0
    individuo.conflito_de_horario_de_professor = 0

    for materia in range(len(individuo.lista_de_materias)):
        individuo.lista_de_materias[materia].punicao = 0