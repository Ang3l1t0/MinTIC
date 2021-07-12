import java.util.Hashtable;
import java.util.Scanner;
import java.util.Map.Entry;

public class reto1 {
    static Scanner leer = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        String datoPaciente, enfermedad, cedula, nauseas, vomitos, dolorAbdominal, diarrea, fiebre;
        String[] datos, sintomas = { "nauseas", "vomitos", "dolor abdominal", "diarrea", "fiebre" };
        int[] cantidadSintomas;
        int i, cantidadPacientes, nauseasCount = 0, vomitosCount = 0, dolorAbdominalCount = 0, diarreaCount = 0,
                fiebreCount = 0, diagnostico = 0;
        Hashtable<String, String> cedulaEnfermedad = new Hashtable<String, String>();

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
            // Validaciones de enfermedad
            if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("si") && diarrea.equals("si")
                    && fiebre.equals("si")) {
                enfermedad = "Staphylococcus aureus";
                diagnostico += 1;
            } else if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("no")
                    && diarrea.equals("si") && fiebre.equals("si")) {
                enfermedad = "Norovirus";
                diagnostico += 1;
            } else if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("no")
                    && diarrea.equals("no") && fiebre.equals("no")) {
                enfermedad = "Bacillus cereus";
                diagnostico += 1;
            } else if (nauseas.equals("no") && vomitos.equals("no") && dolorAbdominal.equals("si")
                    && diarrea.equals("no") && fiebre.equals("si")) {
                enfermedad = "Taenia saginata";
                diagnostico += 1;
            } else if (nauseas.equals("no") && vomitos.equals("si") && dolorAbdominal.equals("no")
                    && diarrea.equals("si") && fiebre.equals("no")) {
                enfermedad = "Rotavirus";
                diagnostico += 1;
            } else {
                enfermedad = "Sin diagnostico";
            }
            // creamos un diccionario con los datos de la cedula, enfermedad
            cedulaEnfermedad.put(cedula, enfermedad);
        }
        // recorremos el diccionario de la enfermedad e imprimimos los datos key, value
        for (Entry<String, String> entry : cedulaEnfermedad.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
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
