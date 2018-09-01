
public class Calculadora {
	public Double operadorA;
	public Double operadorB;
	//Constructor
	public Calculadora() {
		this.operadorA = 10.0;		
		this.operadorB = 5.0;
	}
	
	public Calculadora(Double a, Double b) {
		this.operadorA = a;
		this.operadorB = b;
	}
	
	public double suma() {
		return operadorA + operadorB;
	}
	
	public double resta() {
		return operadorA - operadorB;
	}
	
	public double division() {
		return operadorA / operadorB;
	}
	
	public double multiplicacion() {
		return operadorA * operadorB;
	}
	
	public void resultado() {

		System.out.println("Suma: "+ suma());
		System.out.println("Resta: "+ resta());
		System.out.println("Division: "+ division());
		System.out.println("Multiplicacion: "+ multiplicacion());
		
	}
}
