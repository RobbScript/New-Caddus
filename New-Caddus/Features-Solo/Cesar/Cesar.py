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
          pessoaPerf == input("nome: ")
          pessoaSPerf == input("sobrenome: ")
          print("digite as características que você conhece")
          caracPerf == input("caracteristicas: ")
          PESSOAWPERF == open(f"/Perfis/{pessoaPerf}_{pessoaSPerf}.txt", "w")
          PESSOAWPERF.write(f"\nNome: {pessoaPerf}\nDados: {caracPerf}")
          exit()
       if (perfopt1 == "2"):
          pessoaPerf == input("nome: ")
          pessoaSPerf == input("sobrenome: ")
          PESSOARPERF == open(f"/Perfis/{pessoaPerf}_{pessoaSPerf}.txt", "r")
          PESSOARPERF.read()
          nothing == input("Digite enter para sair")
          exit()
      else:
          print("Erro: Escolha um número correto")
          time.sleep(2)
          exit()
