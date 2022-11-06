puts 'Valquíria (Alpha)'
puts "Opções:\n1- verificar um arquivo"
print("opção: ")
optimenuone = gets.chomp
if optimenuone == "1"
    print "Digite o nome do arquivo: "
    arquivoone = gets.chomp
    print "Extensão do arquivo\n-json\n-txt\n" 
    extensarq = gets.chomp
    FileVrf = File.open("#{arquivoone}.#{extensarq}").birthtime
    puts(FileVrf)
end