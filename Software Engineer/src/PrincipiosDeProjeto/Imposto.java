package PrincipiosDeProjeto;

//responsabilidade unica
public class Imposto {
    private String estado;
    private double valor = 0d;
    private double taxa = 0d;

    public Imposto(String estado, double taxa) {
        this.estado = estado;
        this.taxa = taxa;
    }
    public Imposto(){}

    public void setValor(double valor){
        this.valor = valor;
    }

    public String getEstado() {
        return estado;
    }

    public double getValor() {
        return valor;
    }

    public double getTaxa() {
        return taxa;
    }
}
