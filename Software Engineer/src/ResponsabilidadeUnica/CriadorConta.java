package ResponsabilidadeUnica;

public class CriadorConta {
    public static String criarConta(Pessoa p){
        return p.getPrimeiroNome().substring(0, 1) + p.getUltimoNome();
    }
}
