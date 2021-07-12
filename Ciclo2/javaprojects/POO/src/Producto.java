public class Producto {

    // atributos de la clase
    private int codigo;
    private int precioCompra;
    private int canBodega;
    private int canMinReqBodega;

    // Constructor de la clase
    public Producto(int codigo, int precioCompra, int canBodega, int canMinReqBodega){
        this.codigo = codigo;
        this.precioCompra = precioCompra;
        this.canBodega = canBodega;
        this.canMinReqBodega = canMinReqBodega;
    }

    // métodos de la clase
    public boolean solicitarPedido(){
        //devuelva true si debe solicitar el producto al proveedor y false en caso contrario.
        if (canBodega < this.canMinReqBodega)
            return true;
        else
            return false;
    }
}
