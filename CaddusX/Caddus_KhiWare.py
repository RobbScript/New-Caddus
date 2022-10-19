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
    "5-Caddus BNK\n",
    "6-Sair\n",
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
        #MIKHAIL SYSTEM
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
    #SREDD SYSTEM
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
                if (rErr1 == "2"):
                    continue
        else:
            exit()
if(optioneA1Z == "3"):
    #NEIL SYSTEM
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
    #INFOS
    print(
        "Mecanismos Presentes: Mikhail, Neil, Sredd. (3)\n",
        "Versão do Sistema: 0.2.5 (Alpha)\n",
        "Geração Caddus: Rebirth\n",
        "Gerenciador de Dados: Supernova\n",
        "Desenvolvimento Geral: 4.5 Horas\n",
        "Dev(s): RobbScript\n",
        "Lançamento oficial: 17/10/2022 7:00 Am\n"
    )
if (optioneA1Z == "5"):
    #CADDUS BANK (BNK)
    while True:
        os.system("clear") or None
        print("olá, bem vindo ao CaddusBNK!")
        print("O gerenciador de Créditos Caddus.")
        print("O que você deseja?\n1-Fazer uma transação Administrador\n2-Fazer uma transação comum\n3-Ver Saldos")
        opt1SBNK = input("opção: ")
        if (opt1SBNK == "1"):
            os.system("clear") or None
            print("Escreva o ID do usuário Sredd")
            optSIDBNK1 = input("ID: ")
            os.system("clear") or None
            USERBANK = open("Cad_BNK/{}.txt".format(optSIDBNK1), "r")
            USREADABLE = USERBANK.read
            method = USREADABLE()
            print(method)
            valor = int(input("digite o saldo da conta: "))
            USERBANK.close
            os.system("clear") or None
            tipoSTBNK = input("Opções:\n+ > Adição\n- > Subtração\n\nOpção: ")
            if (tipoSTBNK == "+"):
                USERBANK = open(f"Cad_BNK/{optSIDBNK1}.txt", "w")
                valorMS = int(input("valor a adicionar: "))
                valorfinal = valor + valorMS
                USERBANK.truncate(10)
                str(valorfinal)
                USERBANK.write(f"{valorfinal}")
                exit()
            if (tipoSTBNK == "-"):
                USERBANK = open(f"Cad_BNK/{optSIDBNK1}.txt", "w")
                valorMS = int(input("valor a adicionar: "))
                valorfinal = valor - valorMS
                USERBANK.truncate(10)
                str(valorfinal)
                USERBANK.write(f"{valorfinal}")
                exit()
            else:
                print("Opção errada...")
                time.sleep(1)
                os.system("clear") or None
                continue
        if (opt1SBNK == "2"):
            print("De qual conta?")
            os.system("clear") or None
            print("Digite o ID Sreed do Usuário transferidor")
            cn1tc = input("ID: ")
            USERBANK = open(f"Cad_BNK/{cn1tc}.txt", "r")
            USREADABLE = USERBANK.read
            method = USREADABLE()
            os.system("clear") or None
            print(method)
            print("Digite o valor da conta: ")
            vl1Cm = int(input("Valor:"))
            os.system("clear") or None
            print("Digite o ID Sreed do Usuário a receber")
            cn2tc = input("segundo ID: ")
            USERBANK.close
            USERBANK2 = open(f"Cad_BNK/{cn2tc}.txt", "r")
            USREADABLE = USERBANK2.read
            method = USREADABLE()
            print(method)
            print("Digite o valor da segunda conta: ")
            vl2Cm = int(input("Valor:"))
            os.system("clear") or None
            tipoSTBNK = input("Opções:\n+ > Adição\n- > Subtração")
            if (tipoSTBNK == "+"):
                #primeira conta
                USERBANK = open(f"Cad_BNK/{cn1tc}.txt", "w")
                print("valor a adicionar na segunda conta: ")
                valorMS = int(input("valor: "))
                USERBANK.truncate(10)
                valorfinal1 = vl1Cm - valorMS
                str(valorfinal1)
                USERBANK.write(valorfinal1)
                #segunda conta
                USERBANK = open(f"Cad_BNK/{cn2tc}.txt", "w")
                USERBANK.truncate(10)
                valorfinal2 = vl2Cm + valorMS
                str(valorfinal2)
                USERBANK.write(valorfinal2)
                exit()
            if (tipoSTBNK == "-"):
                USERBANK = open(f"Cad_BNK/{cn1tc}.txt", "w")
                print("valor a receber da segunda conta: ")
                valorMS = int(input("valor: "))
                USERBANK.truncate(10)
                valorfinal1 = vl1Cm + valorMS
                str(valorfinal1)
                USERBANK.write(valorfinal1)
                #segunda conta
                USERBANK = open(f"Cad_BNK/{cn2tc}.txt", "w")
                USERBANK.truncate(10)
                valorfinal2 = vl2Cm - valorMS
                str(valorfinal2)
                USERBANK.write(valorfinal2)
                exit()
            else:
                print("Opção errada...")
                time.sleep(1)
                os.system("clear") or None
                continue
        if (opt1SBNK == "3"):
            print("digite o ID Sredd da conta que você quer olhar o saldo")
            eIDsc = input("ID: ")
            USEREYE = open(f"Cad_BNK/{eIDsc}.txt", "r")
            USREADABLE = USEREYE.read
            method = USREADABLE()
            os.system("clear") or None
            print("valor:")
            print(method)
            nothing = input("Digite Enter para continuar...")
        else:
            print("opção errada")
            time.sleep(1)
            continue
if(optioneA1Z == "6"):
    exit()
else:
    print("Falha, Alternativa não existente.")
    time.sleep(2)
    exit()
    