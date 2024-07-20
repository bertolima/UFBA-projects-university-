package ResponsabilidadeUnica;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CapturadorDadosPessoa {
    public static Pessoa obterDados() throws IOException{
        Pessoa p = new Pessoa();
        BufferedReader teclado = new BufferedReader(new InputStreamReader(System.in));

        GeradorDeMensagens.mensangemSolicitacaoDado("primeiro nome");
        p.setPrimeiroNome(teclado.readLine());

        GeradorDeMensagens.mensangemSolicitacaoDado("último nome");
        p.setUltimoNome(teclado.readLine());

        return p;
    }
}
