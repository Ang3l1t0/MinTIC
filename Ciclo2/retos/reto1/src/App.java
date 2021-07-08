import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner leer = new Scanner(System.in);
        String datoPaciente, enfermedad, cedula, nauseas, vomitos, dolorAbdominal, diarrea, fiebre;
        String[] datos;
        int i, cantidadPacientes;

        cantidadPacientes = Integer.parseInt(leer.nextLine()); // leo como string convierto a int para evitar problemas
        for (i = 0; i < cantidadPacientes; i++) {

            datoPaciente = leer.nextLine();

            datos = datoPaciente.split("-"); // separador

            // asignacion de valores segun el lugar de la cadena
            cedula = datos[1];
            nauseas = datos[2];
            vomitos = datos[3];
            dolorAbdominal = datos[4];
            diarrea = datos[5];
            fiebre = datos[6];

            // Validaciones
            if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("si") && diarrea.equals("si")
                    && fiebre.equals("si")) {
                enfermedad = "Staphylococcus aureus";
            } else if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("no")
                    && diarrea.equals("si") && fiebre.equals("si")) {
                enfermedad = "Norovirus";
            } else if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("no")
                    && diarrea.equals("no") && fiebre.equals("no")) {
                enfermedad = "Bacillus cereus";
            } else if (nauseas.equals("no") && vomitos.equals("no") && dolorAbdominal.equals("si")
                    && diarrea.equals("no") && fiebre.equals("si")) {
                enfermedad = "Taenia saginata";
            } else if (nauseas.equals("no") && vomitos.equals("si") && dolorAbdominal.equals("no")
                    && diarrea.equals("si") && fiebre.equals("no")) {
                enfermedad = "Rotavirus";
            } else {
                enfermedad = "Sin diagnostico";
            }

            System.out.println(cedula + " " + enfermedad);
        }
    }
}
