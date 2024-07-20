package InversaoDependencias;

public class Tarefa implements ITarefa {
	
	private String nome;
	private IFuncionario responsavel;
	private double horasTrabalhadas;
	private boolean completa = false;

	
    @Override
	public void realizarTrabalho(double horas)
    {
        this.horasTrabalhadas += horas;
        MecanismoLog log = new MecanismoLog();
        log.log("Trabalho realizado em " + nome + ".");
    }

    @Override
	public void completarTarefa()
    {
        completa = true;

        IMecanismoLog log = Fabrica.criarMecanismoLog();
        log.log("Tarefa " + nome + " completa.");

        IMecanismoMensagem mecanismoMensagem = Fabrica.criarMecanismoMensagem();
        mecanismoMensagem.enviarMensagem(responsavel, "A tarefa " + nome + " foi finalizada.");
    }
	
	@Override
	public String getNome() {
		return nome;
	}
	@Override
	public void setNome(String nome) {
		this.nome = nome;
	}
	@Override
	public IFuncionario getResponsavel() {
		return responsavel;
	}
	@Override
	public void setResponsavel(IFuncionario responsavel) {
		this.responsavel = responsavel;
	}
	@Override
	public double getHorasTrabalhadas() {
		return horasTrabalhadas;
	}
	@Override
	public boolean isCompleta() {
		return completa;
	}
	
	
}
