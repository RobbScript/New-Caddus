import java.util.Date;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class neptif {

 public static void main(String[] args){
    Date Dia = new Date();
    System.out.println("RobbScript 2022");
    System.out.printf("Caddus KhiWare (χ) // %s%n",Dia);
    String user = "User";
    System.out.print("Nome: ");
    String nome;
    Scanner sc = new Scanner(System.in);
    nome = sc.next();
    System.out.print("senha: ");
	String senha;
	senha = sc.next();
    if (nome.equals ("rob") && senha.equals ("8642")){
        System.out.println("Olá, Robbscript!");
        user = "Dev";
    } else { 
        System.out.println("invasor detectado");
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.exit(0);
    }
    System.out.println("Opções:");
    System.out.println("1- Integrantes");
    System.out.println("2- Conquistas");
    System.out.println("/////////");
    System.out.printf("%s@%s: ",nome, user);
    String resp1;
    resp1 = sc.next();
    if (resp1.equals ("1") || resp1.equals ("Membros") || resp1.equals ("membros")){
        System.out.println("-Verônica");
        System.out.println("-Mikhail");
        System.out.println("-Valkyrie");
        System.out.println("-Neil");
    }
    if (resp1.equals ("2") || resp1.equals ("Projetos") || resp1.equals ("projetos")){
    	System.out.println("-Caddus/Kattsi");
    	System.out.println("-Biohazard");
    	System.out.println("-Biolab");
    	System.out.println("-Micronetks");
    	System.out.println("-SGD-P/SGBD-P");
    }else{
    	System.out.println("digite uma opção válida");
    }

    sc.close();
}
}

