package PrincipiosDeProjeto;

public class ProdutoAltoValor implements IProduto{
    private double valor;

    public ProdutoAltoValor(double valor) {
        this.valor = valor;
    }

    @Override
    public double getValor() {
        return this.valor;
    }

    @Override
    public ISomadorImposto obterSomador() {
        return new SomadorAltoValor();
    }
}
