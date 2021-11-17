from tkinter import *
from funcoesDeBusca import procurar_materia_por_horario_e_periodo

from modelos.individuo import Individuo

class Table:
    
    def __init__(self,root, individuo : Individuo):

        aulas : int = 0
        periodo : int = 1
        w : int = 0
        #Criando tabela
        for linha in range(28):
            if periodo == 5:
                break
            for coluna in range(5):
                self.e = Entry(root, width=40, fg='black', font=('Arial',10))
                self.e.grid(row=w, column=coluna)
                materia = procurar_materia_por_horario_e_periodo(individuo.lista_de_materias, aulas, periodo)
                
                if materia != None:
                    self.e.insert(END, materia.nome)
                else:
                    self.e.insert(END, "Vago")
                
                if aulas < 24:
                    aulas += 1
                else:
                    w+=1
                    for tracejado in range(5):
                        self.e = Entry(root, width=40, fg='black', font=('Arial',10))
                        self.e.grid(row=w, column=tracejado)
                        self.e.insert(END, "----------------------------------------------------------------------------------------")
                    
                    aulas = 0
                    periodo += 1
                    
            w+=1
                

        
                        
  
    
