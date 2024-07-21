package PrincipiosDeProjeto;

import java.util.ArrayList;
import java.util.List;

public class Programa {

	public static void main(String[] args) {
		List<Venda> vendas = new ArrayList<Venda>();
		vendas.add(Fabrica.registarVenda("10/05/2023", 11.5));
		vendas.add(Fabrica.registarVenda("12/05/2023", 8.5));
		vendas.add(Fabrica.registarVenda("12/05/2023", 1000.0));
		Fabrica.criarGerenciadorTributario().registraTotalImpostoMes(2023, 5, vendas);
	}

}
