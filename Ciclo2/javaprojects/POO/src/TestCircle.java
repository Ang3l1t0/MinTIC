public class TestCircle {
    public static void main(String[] args) {
        Circle c1 = new Circle();
        System.out.println(c1);
        System.out.println("c1 área: " + c1.getArea());
        System.out.println("c1 circunferencia: " + c1.getCircunferencia());
        
        Circle c2 = new Circle(3);
        System.out.println(c2);
        System.out.println("c2 área: " + c2.getArea());
        System.out.println("c2 circunferencia: " + c2.getCircunferencia());

        Circle c3 = new Circle(7, "azul");
        System.out.println(c3);
        c3.setRadius(6);
        System.out.println(c3);
        System.out.println("c3 área: " + c3.getArea());
        System.out.println("c3 circunferencia: " + c3.getCircunferencia());


    }
}
