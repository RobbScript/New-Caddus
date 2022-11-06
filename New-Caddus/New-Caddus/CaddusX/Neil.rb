system("clear")
puts("olá, bem vindo ao Neil")
puts("sistema de salvar resumos de aulas\n")
puts("O que você deseja?\n1-Escrever\n2-Ler")
optone = input("opção: ")
os.system("clear")
if (optone == "1")
    puts("Qual matéria?")
    puts("1-Portugês\n2-Matemática\n3-Ciências\n4-Geografia\n5-História\n6-Educação Física\n7-Inglês\n8-Projeto de vida\n9-Eletivas")
    print "digite o número: "
    mat1 = gets.chomp
    Escarc = File.open("materiasneil/#{mat1}.txt", "w")
    system("clear")
    puts "escrevendo..."
    print 'matéria: '
    materia = gets.chomp
    print 'data: '
    data = gets.chomp
    print 'resumo: '
    conteúdo = gets.chomp
    Escarc.write("\nMatéria: #{materia} | Data: #{data}\nResumo: #{conteúdo}\n")
    print 'pressione Enter para sair...'
    nothing1 = gets.chomp
    exit
elsif (optone == "2")
    puts "Qual matéria?"
    puts("1-Portugês\n2-Matemática\n3-Ciências\n4-Geografia\n5-História\n6-Educação Física\n7-Inglês\n8-Projeto de vida\n9-Eletivas")
    print 'digite o número: '
    mat1 = gets.chomp
    Escarc = File.open("materiasneil/#{mat1}.txt", "r")
    system("clear")
    puts(Escarc.read())
    print 'pressione Enter para sair...'
    nothing2 = gets.chomp
    exit()
else
    exit()