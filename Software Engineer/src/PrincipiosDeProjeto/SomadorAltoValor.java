package PrincipiosDeProjeto;

public class SomadorAltoValor implements ISomadorImposto {
    public void somar(double valorCompra, Imposto imposto){
        imposto.setValor(imposto.getValor() + valorCompra * imposto.getTaxa() + valorCompra * 0.07);
    }
}
