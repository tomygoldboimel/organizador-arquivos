import os
import shutil

def organizar_arquivos():
    caminho = input("\nInsira o path: ")
    arquivos = os.listdir(caminho)
    pastas = []
    for arquivo in arquivos:
        filename, extension = os.path.splitext(arquivo)
        extension = extension[1:].capitalize()

        if extension: 
            pasta_destino = os.path.join(caminho, extension)

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
                pastas.append(pasta_destino)
            origem = os.path.join(caminho, arquivo)
            destino = os.path.join(pasta_destino, arquivo)

            contador = 1
            while os.path.exists(destino):
                novo_nome = f"{filename}({contador}){os.path.splitext(arquivo)[1]}"
                destino = os.path.join(pasta_destino, novo_nome)
                contador += 1

            shutil.move(origem, destino)
    if pastas:
        print("\nOrganização concluída!")
        print("Arquivos incluidos nas pastas: ")
        for pasta in pastas:
            print(os.path.basename(pasta))
    else:
        print("Nenhum arquivo a ser organizado")
