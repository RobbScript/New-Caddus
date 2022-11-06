puts("Bem vindo ao Sredd!")
    while TRUE
        puts("O que você deseja?")
        puts("Opções:\n1-Analisar Código\n2-Adicionar Código\n3-Sair")
        print("Resposta: ")
        sRespone = gets.chomp
        if sRespone == "1"
                print("digite o código: ")
                cUsr1 = gets.chomp
                usuario = File.open("users/#{cUsr1}.txt", "r")
                system("clear")
                print(usuario.readlines())
                print("\ndigite enter para continuar...")
                nd = gets.chomp
                system("clear")
                exit()
        elsif (sRespone == "2")
                print("ID usuário: ")
                cUsr2 = gets.chomp
                nusuario = open("users/#{cUsr2}.txt", "w")
                system("clear")
                códigoSr = ("#{cUsr2}")
                print("nome: ")
                NomeSr = gets.chomp
                print("idade: ")
                IdadeSr = gets.chomp
                print("QI estimado: ")
                qiest = gets.chomp
                print("Status geral: ")
                Status = gets.chomp
                print("Status escolar: ")
                Status_Escolar = gets.chomp
                print("Amizades gerais: ")
                Amizades = gets.chomp
                print("Conteúdo Escolar: ")
                ConteúdoEs = gets.chomp
                print("Nota AkSeb: ")
                Nota_Akeseb = gets.chomp
                nusuario.write("\nCódigo: #{códigoSr}\nNome: #{NomeSr}\nIdade: #{IdadeSr}\nQI: #{qiest}\nStatus: #{Status}\nStatus Escolar: #{Status_Escolar}\nAmizades: #{Amizades}\nConteúdo Escolar #{ConteúdoEs}\nNota Akseb: #{Nota_Akeseb}")
                exit()
        else
            exit()
    end