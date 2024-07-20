package AbertoFechado;

public class CandidatoGerente implements ICandidato{
    private String nome;
    private String sobrenome;

    public CandidatoGerente(String nome, String sobrenome) {
        this.sobrenome = sobrenome;
        this.nome = nome;
    }

    @Override
    public String getNome() {
        return nome;
    }

    @Override
    public String getSobrenome() {
        return sobrenome;
    }

    @Override
    public ICriadorContas obterCriador() {
        return new CriadorContasGerente();
    }
}
