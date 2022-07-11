import java.util.Date;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class neptif {

	public static void main(String[] args){
	Date Dia = new Date();
	System.out.println("ProbeX-TFPP 2022");
	System.out.printf("Caddus Neptune // %s%n",Dia);
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
    System.out.println("1- Membros");
    System.out.println("2- Projetos");
    System.out.println("/////////");
    System.out.printf("%s@%s: ",nome, user);
    String resp1;
    resp1 = sc.next();
    if (resp1.equals ("1") || resp1.equals ("Membros") || resp1.equals ("membros")){
        System.out.println("-rob");
        System.out.println("-davi");
        System.out.println("-vini");
        System.out.println("-caik");
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


