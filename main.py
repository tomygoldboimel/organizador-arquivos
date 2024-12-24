from encerraPrograma import encerraPrograma
from organizador import organizar_arquivos
from desorganizador import desorganizar_arquivos
from tkinter import Tk
from tkinter.filedialog import askdirectory
from menu import menu

if __name__ == "__main__":
    while True:
        escolha = menu()
        
        match escolha:
            case "1":
                organizar_arquivos()
                continuar = encerraPrograma()
                if continuar == False:
                    break
                else:
                    True
            case "2":
                desorganizar_arquivos()
                continuar = encerraPrograma()
            case "3":
                print("\nEncerrando programa...")
                break
            case _:
                print("\nOpção Inválida.") 
        if continuar == False: break
        else: True
       



