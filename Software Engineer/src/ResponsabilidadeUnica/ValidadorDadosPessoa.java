package ResponsabilidadeUnica;

public class ValidadorDadosPessoa {
    public static boolean validarDadosPessoa(Pessoa p){
        if (p.getPrimeiroNome().isEmpty()) {
            GeradorDeMensagens.mensagemErroValidacao("primeiro nome");
            return false;
        }

        if (p.getUltimoNome().isEmpty()) {
            GeradorDeMensagens.mensagemErroValidacao("último nome");
            return false;
        }

        return true;
    }
}
