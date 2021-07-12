import java.util.Scanner;

public class App {
    public static Scanner leer = new Scanner(System.in);
    public static void main(String[] args) throws Exception {        
        /*
        Diseñar un programa que:

        • Solicite por consola el 
            código del producto, 
            el precio de compra, 
            la cantidad en bodega 
            y la cantidad mínima requerida.
        • Instancie un producto dentro de la clase principal.
        • Arroje una alerta en caso tal se deba solicitar el pedido al proveedor.
        */
        System.out.print("Código del producto: ");
        int codProducto = leer.nextInt();
        System.out.print("Precio de compra: ");
        int precioCompra = leer.nextInt();
        System.out.print("Cantidad en bodega: ");
        int canBodega = leer.nextInt();
        System.out.print("Cantidad mínima requerida: ");
        int canMinRequerida = leer.nextInt();

        Producto producto1 = new Producto(codProducto,precioCompra,canBodega,canMinRequerida);

        if (producto1.solicitarPedido()){
            System.out.print("¡Alerta! Se debe solicitar pedido al proveedor.");
        }else{
            System.out.print("No se solicitará producto.");
        }


    }
}
