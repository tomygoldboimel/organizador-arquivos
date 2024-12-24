import os
import shutil

def desorganizar_arquivos():
    caminho = input("\nInsira o path: ")
    for pasta in os.listdir(caminho):
        pasta_destino = os.path.join(caminho, pasta)
        
        if os.path.isdir(pasta_destino):
            for arquivo in os.listdir(pasta_destino):
                origem = os.path.join(pasta_destino, arquivo)
                destino = os.path.join(caminho, arquivo)

                contador = 1
                while os.path.exists(destino):
                    nome_arquivo, ext = os.path.splitext(arquivo)
                    novo_nome = f"{nome_arquivo}({contador}){ext}"
                    destino = os.path.join(caminho, novo_nome)
                    contador += 1

                shutil.move(origem, destino)

            os.rmdir(pasta_destino)

    print("\nDesorganização concluída!")
