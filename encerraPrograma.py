def encerraPrograma():
    resposta = input("\nDeseja encerrar o programa? (S/N) ")
    match resposta:
        case "S" | "s":
            continuar = False
            print("\nEncerrando programa...")
        case "N" | "n":
            continuar = True
        case _:
            print("Opção Inválida. Responda com 'S' ou 'N' ")
            encerraPrograma()
    return continuar
            