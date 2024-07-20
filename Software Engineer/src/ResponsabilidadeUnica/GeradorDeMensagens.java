package ResponsabilidadeUnica;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class GeradorDeMensagens {

    public static void mensagemBoasVindas(){
        System.out.println("Seja bem-vinda ou bem-vindo.");
    }

    public static void mensangemFimDoPorgrama() throws IOException {
        BufferedReader teclado = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Tecle enter para sair o programa...");
        teclado.readLine();
    }

    public static void mensagemErroValidacao(String campo){
        System.out.println("Você náo forneceu um " + campo + " válido.");
    }

    public static void mensangemSolicitacaoDado(String dado){
        System.out.println("Qual o seu " + dado + "?");
    }

    public static void mensagemContaCriada(String id){
        System.out.println("Seu id de usu�rio � " + id);
    }
}
