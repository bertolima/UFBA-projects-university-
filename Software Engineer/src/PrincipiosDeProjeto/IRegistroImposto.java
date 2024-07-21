package PrincipiosDeProjeto;

//interface para tratar diferentes mecanismos de registro de impsoto
//por hora, a unica disponivel é por banco de dados

//principio aberto/fechado
//responsabilidade unica
public interface IRegistroImposto {
    public void save(int ano, int mes, Imposto imposto);
}
