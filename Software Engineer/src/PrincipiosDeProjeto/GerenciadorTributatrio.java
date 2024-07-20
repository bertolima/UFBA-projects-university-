package PrincipiosDeProjeto;

import java.util.List;

public class GerenciadorTributatrio {

	public void registraTotalImpostoMes(int ano, int mes, List<Venda> vendasMes) {
		
		double imposto = 0;
		for (Venda venda : vendasMes)
		{	
			if (venda.getValor() < 1000)
				imposto += 0.05 * venda.getValor();
			else
				imposto += 0.07 * venda.getValor();
		}
		
		//registra valor do imposto total
		BancoDados banco = new BancoDados();
		banco.save(ano, mes, imposto);
		
	}

}
