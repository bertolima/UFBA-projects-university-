package PrincipiosDeProjeto;

//responsabilidade unica
public class BancoDados implements IRegistroImposto {
	public void save(int ano, int mes, Imposto imposto) {
		System.out.println("Simulando o registro em banco de dados: " + ano + "/" + mes + " " + imposto.getValor());
	}
}
