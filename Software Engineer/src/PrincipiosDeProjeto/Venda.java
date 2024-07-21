package PrincipiosDeProjeto;


public class Venda {
	private String data;
	private IProduto produto;
	
	public Venda(String data, double valor) {
		this.data = data;
		this.produto = Fabrica.registarProduto(valor);
	}

	public IProduto getProduto() {
		return produto;
	}

	public String getData() {
		return data;
	}

}
