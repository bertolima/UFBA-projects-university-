package PrincipiosDeProjeto;

//Interface para tratar tipos diferentes de produto
//dessa forma eu retiro os ifs na hora de fazer os calculos
//responsabilidade unica
public interface IProduto {
    public double getValor();
    public ISomadorImposto obterSomador();

}
