import os
import time
from SreddSys import *
print("Bem vindo ao Sreed!")
while True:
    print("O que você deseja?")
    print("Opções:\n1-Analisar Código\n2-Sair")
    sRespone = input("Resposta: ")
    if (sRespone == "1"):
        cSeg1 = input("digite a senha: ")
        if (cSeg1 == Senha_De_Segurança):
            cUsr1 = input("digite o código: ")
            usuario = open("{}.txt".format(cUsr1), "r")
            os.system("clear") or None
            print(usuario.read())
            nd = input("\ndigite enter para continuar...")
            os.system("clear") or None
        else:
            print("erro - senha incorreta")
            time.sleep(1)
            os.system("clear") or None
            print("deseja sair?\n1-Sim\n2-Tentar Novamente")
            rErr1 = input("Resposa: ")
            if (rErr1 == "1"):
                break
                exit()
            elif (rErr1 == "2"):
                os.system("clear") or None
                continue
            else:
                exit()
    elif (sRespone == "2"):
        exit()
    else:
        exit()


