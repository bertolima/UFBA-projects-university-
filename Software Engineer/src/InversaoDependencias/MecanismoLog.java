package InversaoDependencias;

public class MecanismoLog implements IMecanismoLog {
	
	@Override
	public void log(String mensagem) {
		System.out.println(mensagem);
	}
}
