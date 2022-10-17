#viva a Anarquia! (A)
#RobbScript Creator
import os
import time
from SreddSys import *
print("Caddus KhiWare (Alpha)")
User = ("Usuário: ")
Pswd =  ("Senha: ")
while False:
    if (User == "rob" and Pswd == "8642"):
     os.system("clear")
    else:
     exit()
print("O que você deseja acessar?")
print(
    " 1-Mikhail\n",
    "2-Sredd\n",
    "3-Neil\n",
    "4-Informações\n",
    "5-Sair\n",
)
optioneA1Z = input("Opção: ")
if(optioneA1Z == "1"):
    os.system("clear")
    print("olá, bem vindo ao MikHail")
    print("sistema de salvar TEXTOS de\ncadernos/conteúdo de cadernos\n")
    username = input("username: ")
    password = input("password: ")
    if (username == "rob" and password == "8642"):
        os.system("clear")
    else:
        exit()
    print("O que você deseja?\n1-Escrever\n2-Ler")
    optone = input("opção: ")
    os.system("clear")
    if (optone == "1"):
        print("Qual matéria?")
        print("1-Portugês\n2-Matemática\n3-Ciências\n4-Geografia\n5-História\n6-Educação Física\n7-Inglês\n8-Projeto de vida\n9-Eletivas")
        mat1 = input ("digite o número: ")
        Escarc = open(f"materiasmik/{mat1}.txt", "w")
        os.system("clear")
        print("escrevendo...")
        materia = input("matéria: ")
        data = input("data: ")
        conteúdo = input("conteúdo: ")
        Escarc.write(f"\nMatéria: {materia} | Data: {data}\nConteúdo: {conteúdo}\n")
        nothing1 = input("pressione Enter para sair...")
    if (optone == "2"):
        print("Qual matéria?")
        print("1-Portugês\n2-Matemática\n3-Ciências\n4-Geografia\n5-História\n6-Educação Física\n7-Inglês\n8-Projeto de vida\n9-Eletivas")
        mat1 = input ("digite o número: ")
        Escarc = open(f"materiasmik/{mat1}.txt", "r")
        os.system("clear")
        print(Escarc.read())
        nothing2 = input("pressione Enter para sair...")
    else:
        exit()
if(optioneA1Z == "2"):
    print("Bem vindo ao Sredd!")
    while True:
        print("O que você deseja?")
        print("Opções:\n1-Analisar Código\n2-Adicionar Código\n3-Sair")
        sRespone = input("Resposta: ")
        if (sRespone == "1"):
            cSeg1 = input("digite a senha: ")
            if (cSeg1 == Senha_De_Segurança):
                cUsr1 = input("digite o código: ")
                usuario = open("users/{}.txt".format(cUsr1), "r")
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
            cSeg1 = input("digite a senha: ")
            if (cSeg1 == Senha_De_Segurança):
                cUsr2 = input("ID usuário: ")
                nusuario = open("users/{}.txt".format(cUsr2), "w")
                os.system("clear") or None
                códigoSr = (f"{cUsr2}")
                NomeSr = input("nome: ")
                IdadeSr = input("idade: ")
                qiest = input("QI estimado: ")
                Status = input("Status geral: ")
                Status_Escolar = input("Status escolar: ")
                Amizades = input("Amizades gerais: ")
                ConteúdoEs = input("Conteúdo Escolar: ")
                Nota_Akeseb = input("Nota AkSeb: ")
                nusuario.write(f"\nCódigo: {códigoSr}\nNome: {NomeSr}\nIdade: {IdadeSr}\nQI: {qiest}\nStatus: {Status}\nStatus Escolar: {Status_Escolar}\nAmizades: {Amizades}\nConteúdo Escolar {ConteúdoEs}\nNota Akseb: {Nota_Akeseb}")
            else:
                print("erro - senha incorreta")
                time.sleep(1)
                os.system("clear") or None
                print("deseja sair?\n1-Sim\n2-Tentar Novamente")
                rErr1 = input("Resposa: ")
                if (rErr1 == "1"):
                    break
                    exit()
        else:
            exit()
if(optioneA1Z == "3"):
    os.system("clear")
    print("olá, bem vindo ao Neil")
    print("sistema de salvar RESUMOS de\nconteúdo de aulas/matérias\n")
    username = input("username: ")
    password = input("password: ")
    if (username == "rob" and password == "8642"):
        os.system("clear")
    else:
        exit()
    print("O que você deseja?\n1-Escrever\n2-Ler")
    optone = input("opção: ")
    os.system("clear")
    if (optone == "1"):
        print("Qual matéria?")
        print("1-Portugês\n2-Matemática\n3-Ciências\n4-Geografia\n5-História\n6-Educação Física\n7-Inglês\n8-Projeto de vida\n9-Eletivas")
        mat1 = input ("digite o número: ")
        Escarc = open(f"materiasneil/{mat1}.txt", "w")
        os.system("clear")
        print("escrevendo...")
        materia = input("matéria: ")
        data = input("data: ")
        resumo = input("resumo: ")
        Escarc.write(f"\nMatéria: {materia} | Data: {data}\nConteúdo: {resumo}\n")
        nothing1 = input("pressione Enter para sair...")
    if (optone == "2"):
        print("Qual matéria?")
        print("1-Portugês\n2-Matemática\n3-Ciências\n4-Geografia\n5-História\n6-Educação Física\n7-Inglês\n8-Projeto de vida\n9-Eletivas")
        mat1 = input ("digite o número: ")
        Escarc = open(f"materiasneil/{mat1}.txt", "r")
        os.system("clear")
        print(Escarc.read())
        nothing2 = input("pressione Enter para sair...")
    else:
        exit()
if(optioneA1Z == "4"):
    print(
        "Mecanismos Presentes: Mikhail, Neil, Sredd. (3)\n",
        "Versão do Sistema: 0.1.3 (Alpha)\n",
        "Geração Caddus: Rebirth\n",
        "Gerenciador de Dados: Supernova\n",
        "Desenvolvimento Geral: 4.5 Horas\n",
        "Dev(s): RobbScript\n",
        "Lançamento oficial: 17/10/2022 7:00 Am\n"
    )
if(optioneA1Z == "5"):
    exit()
else:
    print("Falha, Alternativa não existente.")
    time.sleep(2)
    exit()
    