package ResponsabilidadeUnica;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Programa {

	public static void main(String[] args) throws IOException {
		
		GeradorDeMensagens.mensagemBoasVindas();

		Pessoa pessoa = CapturadorDadosPessoa.obterDados();

		if(ValidadorDadosPessoa.validarDadosPessoa(pessoa) == false){
			GeradorDeMensagens.mensangemFimDoPorgrama();
			return;
		}

		GeradorDeMensagens.mensagemContaCriada(CriadorConta.criarConta(pessoa));
		GeradorDeMensagens.mensangemFimDoPorgrama();
	}

}