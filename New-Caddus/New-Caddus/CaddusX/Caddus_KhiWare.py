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
    "7-Valquíria\n",
    "8-Sair\n"
)
optioneA1Z = input("Opção: ")
if(optioneA1Z == "1"):
    #MIKHAIL SYSTEM
    rubymik = 'ruby Mikhail.rb'
    os.system(rubymik)
if(optioneA1Z == "2"):
    #SREDD SYSTEM
    rubysredd = 'ruby Sredd.rb'
    os.system(rubysredd)
if(optioneA1Z == "3"):
    #NEIL SYSTEM
    rubyneil = 'ruby Neil.rb'
    os.system(rubyneil)
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
    cesarruby = ('ruby Cesar.rb')
    os.system(cesarruby)
if(optioneA1Z == "7"):
    rubyvalquiria = "ruby Valquiria.rb"
    os.system(rubyvalquiria)
if(optioneA1Z == "8"):
    exit()
else:
    print("Falha, Alternativa não existente.")
    time.sleep(2)
    exit()