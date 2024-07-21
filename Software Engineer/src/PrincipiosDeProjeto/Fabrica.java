package PrincipiosDeProjeto;


//responsabilidade unica
//classe fabrica afim de concentrar os "new" da aplicação
public class Fabrica {
    public static IRegistroImposto criarRegistroBancoDeDados(){
        return new BancoDados();
    }

    public static IProduto registarProduto(double valor){
        return valor < 1000 ? new ProdutoBaixoValor(valor) : new ProdutoAltoValor(valor);
    }

    public static Imposto criarImposto(){
        return new Imposto();
    }

    public static GerenciadorTributario criarGerenciadorTributario(){
        return new GerenciadorTributario();
    }

    public static Venda registarVenda(String data, double valor){
        return new Venda(data, valor);
    }
}
