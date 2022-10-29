import os
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

