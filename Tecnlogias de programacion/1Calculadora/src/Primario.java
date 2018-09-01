
public class Primario {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Calculadora c = new Calculadora();
		Calculadora cInit = new Calculadora(7.5, 1.2);
	
		System.out.println("Parametros por defecto");
		c.resultado();
		
		System.out.println("\nParametros setteados");
		cInit.resultado();

	}
	
}
