public class Circle {
    // ATRIBUTOS DE LA CLASE:
    // Las constantes estáticas y públicas:
    public static final double DEFAULT_RADIUS = 1.0;
    public static final String DEFAULT_COLOR = "rojo";

    // Las variables privadas:
    private double radius;
    private String color;


    // CONSTRUCTORES DE LA CLASE:
    // Constructor: para crear un círculo con un radio y color por defecto:
    public Circle(){
        this.radius = DEFAULT_RADIUS;
        this.color = DEFAULT_COLOR;
    }

    // Constructor: para un círculo que recibe un radio y el color por será por defecto:
    public Circle(double radius){
        this.radius = radius;
        this.color = DEFAULT_COLOR;
    }

    // Constructor: para un círculo que recibe un radio y color:
    public Circle(double radius, String color){
        this.radius = radius;
        this.color = color;
    }

    

    // MÉTODOS DE LA CLASE:
    // Devuelve el radio (varible privada):
    public double getRadius(){
        return this.radius;
    }
    // Devuelve el color (varible privada):
    public String getColor(){
        return this.color;
    }
    // Establece el radio (varible privada):
    public void setRadius(double radius){
        this.radius = radius;
    }
    // Establece el color (varible privada):
    public void setColor(String color) {
        this.color = color;
    }

    // Devuelve una cadena autodescriptiva para la instancia Circle:
    public String toString(){
        return "C1(Radius: "+ radius + ", Color: '" + color + "')";
    }

    // Devuelve el Área del círculo:
    public double getArea(){
        return radius * radius * Math.PI;
    }

    // Devuelve el Circunferencia del círculo:
    public double getCircunferencia(){
        return 2.0 * radius * Math.PI;
    }

}