import java.util.Scanner;

public class reto2 {
    static Scanner leer = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        String datoPaciente, cedula, nauseas, vomitos, dolorAbdominal, diarrea, fiebre;
        String[] datos, sintomas = { "nauseas", "vomitos", "dolor abdominal", "diarrea", "fiebre" };
        int[] cantidadSintomas;
        int i, cantidadPacientes, nauseasCount = 0, vomitosCount = 0, dolorAbdominalCount = 0, diarreaCount = 0,
                fiebreCount = 0, diagnostico = 0;
        cantidadPacientes = Integer.parseInt(leer.nextLine()); // leo como string convierto a int para evitar problemas
        String[] cedulas = new String[cantidadPacientes]; // defino una lista cedulas
        String[] enfermedades = new String[cantidadPacientes]; // defino una lista enfermedades

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

            // Conteo de sintomas
            if (nauseas.equals("si")) {
                nauseasCount += 1;
            }
            if (vomitos.equals("si")) {
                vomitosCount += 1;
            }
            if (dolorAbdominal.equals("si")) {
                dolorAbdominalCount += 1;
            }
            if (diarrea.equals("si")) {
                diarreaCount += 1;
            }
            if (fiebre.equals("si")) {
                fiebreCount += 1;
            }
            // Validaciones de enfermedad creamos el objeto enfermedadR y su resultado se guarda en la variable enfermedad
            Paciente enfermedadR = new Paciente();
            String enfermedad = enfermedadR.diagnosticar(nauseas, vomitos, dolorAbdominal, diarrea, fiebre);

            // conteo de los diagnosticos exitosos
            if (enfermedad != "Sin diagnostico") {
                diagnostico += 1;
            }

            cedulas[i] = cedula; // guardamos la cedula en una lista
            enfermedades[i] = enfermedad; // guardamos la enfermed en una lista
        }
        // recorremos la lista cedula e imprimos la cedula mas la enfermedad
        for (i = 0; i < cedulas.length; i++) {
            System.out.println(cedulas[i] + " " + enfermedades[i]);
        }
        // lista con la cantidad de pacientes con cada sintoma
        cantidadSintomas = new int[] { nauseasCount, vomitosCount, dolorAbdominalCount, diarreaCount, fiebreCount };
        System.out.println(sintomas[max(cantidadSintomas)]);
        System.out.println(sintomas[min(cantidadSintomas)]);
        System.out.println(diagnostico);
    }

    public static int max(int[] t) {
        int indice = 0, mayor = t[0];
        for (int i = 1; i < t.length; i++) {
            if (mayor < t[i]) {
                mayor = t[i];
                indice = i;
            }
        }
        return indice;
    }

    public static int min(int[] t) {
        int indice = 0, menor = t[0];
        for (int i = 1; i < t.length; i++) {
            if (menor > t[i]) {
                menor = t[i];
                indice = i;
            }
        }
        return indice;
    }
}
