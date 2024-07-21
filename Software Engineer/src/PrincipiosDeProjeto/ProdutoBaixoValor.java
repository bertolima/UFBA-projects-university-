package PrincipiosDeProjeto;

public class ProdutoBaixoValor implements IProduto{
    private double valor;

    public ProdutoBaixoValor(double valor) {
        this.valor = valor;
    }

    @Override
    public double getValor() {
        return this.valor;
    }

    @Override
    public ISomadorImposto obterSomador() {
        return new SomadorBaixoValor();
    }
}
