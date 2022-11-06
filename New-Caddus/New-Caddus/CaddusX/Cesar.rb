puts 'olá, bem vindo ao Cesar'
puts "perfilador Caddus.\n"
puts "Opções:\n1-adicionar pessoas\n2-Ver uma pessoa"
print 'Opção: '
perfopt1 = gets.chomp
if perfopt1 == "1"
   system("clear")
   puts 'qual pessoa você deseja Salvar?'
   print 'nome: '
   pessoaPerf = gets.chomp
   print 'sobrenome: '
   pessoaSPerf = gets.chomp
   puts 'digite as características que você conhece'
   print 'caracteristicas: '
   caracPerf = gets.chomp
   PESSOAWPERF = File.open("/Perfis/#{pessoaPerf}_#{pessoaSPerf}.txt", "w")
   PESSOAWPERF.write("\nNome: #{pessoaPerf}\nDados: #{caracPerf}")
   exit
elsif perfopt1 == "2"
   print 'nome: '
   pessoaPerf = gets.chomp
   print 'sobrenome: '
   pessoaSPerf = gets.chomp
   PESSOARPERF = File.open("/Perfis/#{pessoaPerf}_#{pessoaSPerf}.txt", "r")
   PESSOARPERF.read()
   print 'Digite enter para sair'
   nothing = gets.chomp
   exit
else
   puts("Erro: Escolha um número correto")
   sleep 2
   exit
end