#RobbScript Creator
import time
import os
import json
bvv = ("CaddusX (KhiWare) | Versão 2.0.1")
if os.path.isfile('UserPass.json'):
   os.system("clear")
   print(bvv)
   print("updated")
   NewUserJson = open('UserPass.json')
   data = json.load(NewUserJson)
   User = (data["user"])
   Password = (data["senha"])
   NewUserJson.close()
   UserSys = input("Usuário: ")
   PassUser = input("Senha: ")
   if (UserSys == User and PassUser == Password):
       os.system("clear") or None
   else:
      print("erro")
else:
    print(bvv)
    print("criar usuário")
    usuário = input("usuário: ")
    senha = input("senha: ")
    senhajson = {"senha": f"{senha}", "user": f"{usuário}"}
    verifypass = json.dumps(senhajson)
    print(verifypass)
    UserNPass = open("UserPass.json", "w")
    UserNPass.write(verifypass)
    exit()
print("O que você deseja acessar?")
print(
    " 1-Mikhail\n",
    "2-Sredd\n",
    "3-Neil\n",
    "4-Informações\n",
    "5-Caddus BNK\n",
    "6-Cesar\n",
    "7-Sair\n",
)
optioneA1Z = input("Opção: ")
if(optioneA1Z == "1"):
    #MIKHAIL SYSTEM
    os.system("clear")
    print("olá, bem vindo ao MikHail")
    print("sistema de salvar textos de cadernos/conteúdo de cadernos\n")
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
        exit()
    if (optone == "2"):
        print("Qual matéria?")
        print("1-Portugês\n2-Matemática\n3-Ciências\n4-Geografia\n5-História\n6-Educação Física\n7-Inglês\n8-Projeto de vida\n9-Eletivas")
        mat1 = input ("digite o número: ")
        Escarc = open(f"materiasmik/{mat1}.txt", "r")
        os.system("clear")
        print(Escarc.read())
        nothing2 = input("pressione Enter para sair...")
        exit()
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
                cUsr1 = input("digite o código: ")
                usuario = open("users/{}.txt".format(cUsr1), "r")
                os.system("clear") or None
                print(usuario.read())
                nd = input("\ndigite enter para continuar...")
                os.system("clear") or None
                exit()
        elif (sRespone == "2"):
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
                exit()
        else:
            exit()
if(optioneA1Z == "3"):
    #NEIL SYSTEM
    os.system("clear")
    print("olá, bem vindo ao Neil")
    print("sistema de salvar RESUMOS de\nconteúdo de aulas/matérias\n")
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
        exit()
    if (optone == "2"):
        print("Qual matéria?")
        print("1-Portugês\n2-Matemática\n3-Ciências\n4-Geografia\n5-História\n6-Educação Física\n7-Inglês\n8-Projeto de vida\n9-Eletivas")
        mat1 = input ("digite o número: ")
        Escarc = open(f"materiasneil/{mat1}.txt", "r")
        os.system("clear")
        print(Escarc.read())
        nothing2 = input("pressione Enter para sair...")
        exit()
    else:
        exit()
if(optioneA1Z == "4"):
    #INFOS
    print(
        "Mecanismos Presentes: Mikhail, Neil, Sredd, Cesar. (4)\n",
        "Versão do Sistema: 2.0.1\n",
        "Geração Caddus: Rebirth\n",
        "Gerenciador de Dados: Star Sirius\n",
        "Desenvolvimento Geral: 4.5 Horas\n",
        "Dev(s): RobbScript\n",
        "Lançamento oficial: 17/10/2022 7:00 Am\n",
        "Baseado no Kattsi Versão 1.0.0"
    )
    exit()
if (optioneA1Z == "5"):
        print("Olá, bem vindo ao Caddus Bank!")
        if (os.path.isfile("Cad_BNK/usersbank.json")):
            userbankusr = input("Conta: ")
            userbankpass = input("Senha: ")
            procuserjbnk = open("Cad_BNK/usersbank.json")
            userbankjson = json.load(procuserjbnk)
            usercorrectbnk = (userbankjson[f"{userbankusr}"])
            userattempbnk = (usercorrectbnk["user"])
            userattempbnk2 = (usercorrectbnk["pass"])
            if(userattempbnk == userbankusr and  userattempbnk2 == userbankpass):
                os.system("clear") or None
            else:
                exit()
            print("Opções:\n1-Transferir Crédito\n2-Receber Crédito")
            respmenubnkone = input("Opção: ")
            if(respmenubnkone == "1"):
                print("de qual conta?")
                contabnktr1 = input("Seu ID Sredd: ")
                contabnktr2 = input("ID Sredd (pessoa que irá receber): ")
                if (os.path.isfile(f"Cad_BNK/{contabnktr1}.json" and os.path.isfile(f"Cad_BNK/{contabnktr2}.json"))):
                    bankscanvalue = open(f"Cad_BNK/{contabnktr1}.json")
                    bankscanvalue2 = open(f"Cad_BNK/{contabnktr2}.json")
                    bankscanmotion = json.load(bankscanvalue)
                    bankscanmotion2 = json.load(bankscanvalue2)
                    rescanbnk = bankscanmotion["valor"]
                    rescanbnk2 = bankscanmotion2["valor"]
                    irescanbnk = int(rescanbnk)
                    irescanbnk2 = int(rescanbnk)
                    print("qual valor deseja transferir?")
                    valorrgsbnk = int(input("valor: "))
                    valorrgsp = (irescanbnk + valorrgsbnk)
                    jsonbnktr = {"valor": f"{valorrgsp}"}
                    jsonbnktrue = json.dumps(jsonbnktr)
                    banktransf1 = open(f"Cad_BNK/{contabnktr1}.json", "w")
                    banktransf1.truncate()
                    banktransf1.write(jsonbnktrue)
                    valorrgsp2 = (irescanbnk - valorrgsbnk)
                    jsonbnktr2 = {"valor": f"{valorrgsp}"}
                    banktransf2 = open(f"Cad_BNK/{contabnktr2}.json", "w")
                    banktransf2.truncate()
                    banktransf2.write(jsonbnktrue)
                else:
                    banktransf1 = open(f"Cad_BNK/{contabnktr1}.json", "w")
                    banktransf2 = open(f"Cad_BNK/{contabnktr2}.json", "w")
                    valorc = {"valor": "0"}
                    rvalorc = json.dumps(valorc)
                    banktransf1.write(rvalorc)
                    banktransf2.write(rvalorc)
                    exit()
                try:
                    bankscanmotion["valor"]
                except:
                    print("registro quebrado :/")
            elif(respmenubnkone == "2"):
                print("de qual conta?")
                contabnktr1 = input("ID Sredd (transferidor): ")
                contabnktr2 = input("Seu ID Sredd: ")
                if (os.path.isfile(f"Cad_BNK/{contabnktr1}.json" and os.path.isfile(f"Cad_BNK/{contabnktr2}.json"))):
                    bankscanvalue = open(f"Cad_BNK/{contabnktr1}.json")
                    bankscanvalue2 = open(f"Cad_BNK/{contabnktr2}.json")
                    bankscanmotion = json.load(bankscanvalue)
                    bankscanmotion2 = json.load(bankscanvalue2)
                    rescanbnk = bankscanmotion["valor"]
                    rescanbnk2 = bankscanmotion2["valor"]
                    irescanbnk = int(rescanbnk)
                    irescanbnk2 = int(rescanbnk)
                    print("qual valor deseja resgatar?")
                    valorrgsbnk = int(input("valor: "))
                    valorrgsp = (irescanbnk - valorrgsbnk)
                    jsonbnktr = {"valor": f"{valorrgsp}"}
                    jsonbnktrue = json.dumps(jsonbnktr)
                    banktransf1 = open(f"Cad_BNK/{contabnktr1}.json", "w")
                    banktransf1.truncate()
                    banktransf1.write(jsonbnktrue)
                    valorrgsp2 = (irescanbnk + valorrgsbnk)
                    jsonbnktr2 = {"valor": f"{valorrgsp}"}
                    banktransf2 = open(f"Cad_BNK/{contabnktr2}.json", "w")
                    banktransf2.truncate()
                    banktransf2.write(jsonbnktrue)
                else:
                    banktransf1 = open(f"Cad_BNK/{contabnktr1}.json", "w")
                    banktransf2 = open(f"Cad_BNK/{contabnktr2}.json", "w")
                    valorc = {"valor": "0"}
                    rvalorc = json.dumps(valorc)
                    banktransf1.write(rvalorc)
                    banktransf2.write(rvalorc)
                    exit()
                try:
                    bankscanmotion["valor"]
                except:
                    print("registro quebrado :/")
            exit()
        else:
            print("criar conta")
            userbankidcreate = input("ID: ")
            userbankusrcreate = input("Conta: ")
            userbankpasscreate = input("Senha: ")
            regisusert = open("usersbank.json", "w")
            nubj = {f"{userbankusrcreate}": {"ID": f"{userbankidcreate}", "user": f"{userbankusrcreate}", "pass": f"{userbankpasscreate}"}}
            jsonnubj = json.dumps(nubj)
            regisusert.write(jsonnubj)
if (optioneA1Z == "6"):
#CESAR SYSTEM
       print("olá, bem vindo ao Joseph")
       print("perfilador Caddus.\n")
       print("Opções:")
       print("1-adicionar pessoas")
       print("2-Ver uma pessoa")
       perfopt1 = input("opção: ")
       if (perfopt1 == "1"):
          os.system("clear") or None
          print("qual pessoa você deseja Salvar?")
          pessoaPerf = input("nome: ")
          pessoaSPerf = input("sobrenome: ")
          print("digite as características que você conhece")
          caracPerf = input("caracteristicas: ")
          PESSOAWPERF = open(f"/Perfis/{pessoaPerf}_{pessoaSPerf}.txt", "w")
          PESSOAWPERF.write(f"\nNome: {pessoaPerf}\nDados: {caracPerf}")
          exit()
       if (perfopt1 == "2"):   
          pessoaPerf = input("nome: ")
          pessoaSPerf = input("sobrenome: ")
          PESSOARPERF = open(f"/Perfis/{pessoaPerf}_{pessoaSPerf}.txt", "r")
          PESSOARPERF.read()
          nothing = input("Digite enter para sair")
          exit()
       else:
          print("Erro: Escolha um número correto")
          time.sleep(2)
          exit()
if(optioneA1Z == "7"):
    exit()
else:
    print("Falha, Alternativa não existente.")
    time.sleep(2)
    exit()
