package PrincipiosDeProjeto;

//interface para para tratar as diferentes formas que se pode calcular o valor do imposto
//a partir dos diferentes tipos de produtos.

//principio aberto/fechado
//responsabilidade unica
public interface ISomadorImposto {
    public void somar(double valorCompra, Imposto imposto);
}
