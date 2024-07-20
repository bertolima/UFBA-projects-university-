package AbertoFechado;

public class CandidatoDiretor implements ICandidato{
    private String nome;
    private String sobrenome;

    public CandidatoDiretor(String nome, String sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
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
        return new CriadorContasDiretor();
    }
}
