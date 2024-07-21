package PrincipiosDeProjeto;

import java.util.List;

//responsabilidade unica
public class GerenciadorTributario {

	public void registraTotalImpostoMes(int ano, int mes, List<Venda> vendasMes) {
		Imposto imposto = Fabrica.criarImposto();
		for (Venda venda : vendasMes) venda.getProduto().obterSomador().somar(venda.getProduto().getValor(), imposto);
		Fabrica.criarRegistroBancoDeDados().save(ano, mes, imposto);
	}

}
